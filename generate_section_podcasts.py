import os
import json
import time
import re
import sys
import tempfile
import asyncio
from pathlib import Path

# Fix Windows console encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    from google import genai
except ImportError:
    sys.exit("pip install google-genai")

try:
    import edge_tts
except ImportError:
    sys.exit("pip install edge-tts")

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    sys.exit("GEMINI_API_KEY environment variable not found.")

client = genai.Client(api_key=GEMINI_API_KEY)
RATE_LIMIT_DELAY = 5

BASE_DIR = Path(".")
PHYSICS_DIR = BASE_DIR / "generated_resources" / "physics"
CHAPTERS = ["chapter_04", "chapter_05"]
LEVELS = ["01_beginner", "02_intermediate", "03_advanced"]


def get_model_candidates():
    return [
        "gemini-2.5-flash-lite",
        "gemini-2.5-mini",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
    ]


def call_gemini(contents, retries=5):
    models = get_model_candidates()
    for model in models:
        for attempt in range(1, retries + 1):
            try:
                resp = client.models.generate_content(model=model, contents=contents)
                text = resp.text.strip()
                if text:
                    return text
                raise ValueError("Empty response from Gemini")
            except Exception as e:
                wait = 15
                print(
                    f"  [WARN] Gemini ({model}) error: {e}, retry {attempt} in {wait}s...",
                    end="",
                    flush=True,
                )
                time.sleep(wait)
        print(f"  [WARN] Model {model} failed, switching to next.")
    return "[ERROR: Gemini API failed]"


# TTS Audio Logic
async def generate_speech(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
    except Exception as e:
        print(f" [TTS Error: {e}]", end="")


def generate_podcast_audio(script_text, output_path):
    print(
        f"\n      [AUDIO] Generating TTS audio for {output_path.name}...",
        end=" ",
        flush=True,
    )
    lines = script_text.split("\n")

    # Female and Male voices
    female_voice = "en-US-JennyNeural"
    male_voice = "en-US-GuyNeural"

    segments = []

    with tempfile.TemporaryDirectory() as temp_dir:
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            voice = None
            text_to_speak = ""

            if line.startswith("Host 1:"):
                voice = female_voice
                text_to_speak = line[len("Host 1:") :].strip()
            elif line.startswith("Host 2:"):
                voice = male_voice
                text_to_speak = line[len("Host 2:") :].strip()

            if voice and text_to_speak:
                # Remove markdown formatting for TTS
                text_to_speak = text_to_speak.replace("*", "").replace("#", "")
                temp_file = Path(temp_dir) / f"{idx}.mp3"
                asyncio.run(generate_speech(text_to_speak, voice, str(temp_file)))

                if temp_file.exists():
                    segments.append(str(temp_file))

        if segments:
            with open(output_path, "wb") as outfile:
                for mp3_path in segments:
                    with open(mp3_path, "rb") as infile:
                        outfile.write(infile.read())
            print(f"[OK] Saved")
        else:
            print("[WARN] No Host dialogue found.")


def main():
    print("=" * 65)
    print("  Podcast Generator | Physics Chapters 4 & 5")
    print("=" * 65)

    for ch_name in CHAPTERS:
        ch_dir = PHYSICS_DIR / ch_name
        if not ch_dir.exists():
            print(f"  [MISSING] {ch_dir} not found.")
            continue

        print(f"\n[>>] Processing {ch_name}")
        mindmap_path = ch_dir / "mindmap.json"
        sections = []

        if mindmap_path.exists():
            try:
                mm_data = json.loads(mindmap_path.read_text(encoding="utf-8"))
                if "children" in mm_data:
                    sections = [
                        child.get("name", "General") for child in mm_data["children"]
                    ]
            except Exception as e:
                print(f"  [WARN] Could not parse mindmap.json: {e}")

        if not sections:
            print("  [WARN] No sections found. Defaulting to 'Entire Chapter'")
            sections = ["Entire Chapter"]

        for level in LEVELS:
            level_dir = ch_dir / level
            if not level_dir.exists():
                level_dir.mkdir(parents=True, exist_ok=True)

            print(f"  [*] Level: {level}")

            for section in sections:
                safe_section = "".join([c if c.isalnum() else "_" for c in section])

                for podcast_type, min_words, length_desc in [
                    ("short_podcast", 800, "5-minute short"),
                    ("long_podcast", 2200, "15-minute long"),
                ]:
                    file_name = f"{podcast_type}_{safe_section}"
                    md_path = level_dir / f"{file_name}.md"
                    mp3_path = level_dir / f"{file_name}.mp3"

                    if md_path.exists() and mp3_path.exists():
                        print(f"      [OK] {file_name} (cached)")
                        continue

                    print(
                        f"      [..] Generating {length_desc} podcast for section: '{section}'...",
                        end=" ",
                        flush=True,
                    )

                    prompt = f"""Write a {length_desc} podcast script for NCERT Class 10 Physics, focusing EXCLUSIVELY on the specific section: "{section}".
Level: {level.split('_')[-1].capitalize()}.
Make it engaging, using analogies and easy-to-understand explanations.

Format STRICTLY as:
Host 1: [dialogue]
Host 2: [dialogue]

Do NOT include any narrators, stage directions, or introductions outside of the Host 1 / Host 2 format."""

                    result = call_gemini(prompt)
                    time.sleep(RATE_LIMIT_DELAY)

                    # Expansion logic to meet length requirements
                    while True:
                        word_count = len(result.split())
                        est_duration = word_count / 150.0

                        print(
                            f"\n      [LOG] {word_count} words, ~{est_duration:.1f} mins",
                            end=" ",
                            flush=True,
                        )
                        if word_count >= min_words:
                            print("- Meets requirement.", end=" ")
                            break

                        print(f"- Expanding...", end=" ", flush=True)
                        context = result[-1000:]
                        expand_prompt = f"""You are continuing a {length_desc} podcast about the section "{section}".
The script needs to be longer to reach the duration requirement.
CONTINUE the script naturally from exactly where it left off. Do not write a new intro. Add more examples, analogies, and back-and-forth dialogue.

Format strictly:
Host 1: [dialogue]
Host 2: [dialogue]

Previous ending:
{context}"""
                        expansion = call_gemini(expand_prompt)
                        result += "\n\n" + expansion.strip()
                        time.sleep(RATE_LIMIT_DELAY)

                    # Save markdown script
                    md_path.write_text(result, encoding="utf-8")
                    print(f"\n      [OK] Script saved: {md_path.name}")

                    # Generate audio
                    generate_podcast_audio(result, mp3_path)


if __name__ == "__main__":
    main()
