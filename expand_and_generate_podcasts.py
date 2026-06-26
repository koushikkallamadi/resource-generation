import os
import time
import tempfile
import asyncio
from pathlib import Path

# Fix Windows console encoding
import sys

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
                    f"  [WARN] Gemini error: {e}, retry {attempt}...",
                    end="",
                    flush=True,
                )
                time.sleep(wait)
    return ""


async def generate_speech(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
    except Exception as e:
        pass


async def _generate_all_speech(tasks):
    await asyncio.gather(*tasks)


def generate_podcast_audio(script_text, output_path):
    print(f"\n      [AUDIO] Generating TTS audio concurrently...", end=" ", flush=True)
    lines = script_text.split("\n")

    female_voice = "en-US-JennyNeural"
    male_voice = "en-US-GuyNeural"
    segments = []

    with tempfile.TemporaryDirectory() as temp_dir:
        idx = 0
        tasks = []
        for line in lines:
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
                text_to_speak = text_to_speak.replace("*", "").replace("#", "")
                temp_file = Path(temp_dir) / f"{idx}.mp3"
                tasks.append(generate_speech(text_to_speak, voice, str(temp_file)))
                segments.append(str(temp_file))
                idx += 1

        if tasks:
            asyncio.run(_generate_all_speech(tasks))

            with open(output_path, "wb") as outfile:
                for mp3_path in segments:
                    if os.path.exists(mp3_path):
                        with open(mp3_path, "rb") as infile:
                            outfile.write(infile.read())
            print(f"[OK] Saved {output_path.name}")
        else:
            print("[WARN] No Host dialogue found in script.")


def main():
    print("=" * 65)
    print("  Expander & Audio Generator | Physics Chapters 4 & 5")
    print("=" * 65)

    for ch_name in CHAPTERS:
        ch_dir = PHYSICS_DIR / ch_name
        if not ch_dir.exists():
            continue

        print(f"\n[>>] Processing {ch_name}")

        for level in LEVELS:
            level_dir = ch_dir / level
            if not level_dir.exists():
                continue

            print(f"  [*] Level (Section): {level}")

            for podcast_type, min_words in [
                ("short_podcast", 800),
                ("long_podcast", 2200),
            ]:
                md_path = level_dir / f"{podcast_type}.md"
                mp3_path = level_dir / f"{podcast_type}.mp3"

                if not md_path.exists():
                    print(f"      [SKIP] {podcast_type}.md not found.")
                    continue

                if mp3_path.exists():
                    print(f"      [SKIP] {podcast_type}.mp3 already exists.")
                    continue

                print(
                    f"      [..] Checking {podcast_type}.md length...",
                    end=" ",
                    flush=True,
                )
                script_text = md_path.read_text(encoding="utf-8")

                while True:
                    word_count = len(script_text.split())
                    est_duration = word_count / 150.0
                    print(
                        f"\n      [LOG] {word_count} words, ~{est_duration:.1f} mins",
                        end=" ",
                        flush=True,
                    )

                    if word_count >= min_words:
                        print("- Meets requirement.", end=" ")
                        break

                    print("- Expanding...", end=" ", flush=True)
                    context = script_text[-1000:]

                    expand_prompt = f"""You are continuing a {podcast_type.replace('_', ' ')}.
The script is currently {word_count} words long, but needs to be at least {min_words} words.
CONTINUE the script naturally from exactly where it left off. Do not write a new intro.
Add more engaging examples, analogies, and back-and-forth dialogue between the hosts.

Format strictly as:
Host 1: [dialogue]
Host 2: [dialogue]

Previous ending for context:
{context}"""
                    expansion = call_gemini(expand_prompt)
                    if expansion:
                        script_text += "\n\n" + expansion.strip()
                        time.sleep(RATE_LIMIT_DELAY)
                        # Save the updated script text immediately
                        md_path.write_text(script_text, encoding="utf-8")
                    else:
                        print(" [ERROR] Failed to expand.")
                        break

                generate_podcast_audio(script_text, mp3_path)


if __name__ == "__main__":
    main()
