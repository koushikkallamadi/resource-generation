import os
import re
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
    import edge_tts
except ImportError:
    sys.exit("pip install edge-tts")

BASE_DIR = Path(".")
PHYSICS_DIR = BASE_DIR / "generated_resources" / "physics"
CHAPTERS = ["chapter_04", "chapter_05"]
LEVELS = ["01_beginner", "02_intermediate", "03_advanced"]


def clean_latex_for_speech(text):
    # Remove math mode delimiters
    text = text.replace("$", "")

    # Replace common greek letters
    greek_letters = [
        "alpha",
        "beta",
        "gamma",
        "lambda",
        "mu",
        "pi",
        "theta",
        "omega",
        "phi",
        "psi",
        "rho",
    ]
    for letter in greek_letters:
        text = text.replace(f"\\{letter}", letter)

    # Replace specific math operations
    text = text.replace("^2", " squared")
    text = text.replace("^3", " cubed")

    # Fractions: \frac{A}{B} -> "A over B"
    text = re.sub(r"\\frac\{([^}]+)\}\{([^}]+)\}", r"\1 over \2", text)

    # Superscripts: ^{A} -> "to the power of A"
    text = re.sub(r"\^\{([^}]+)\}", r" to the power of \1", text)

    # Subscripts: _{A} -> "subscript A" or just remove underscore
    text = re.sub(r"\_\{([^}]+)\}", r" \1", text)
    text = re.sub(r"\_([a-zA-Z0-9]+)", r" \1", text)

    # Clean up remaining latex commands, braces, etc.
    text = text.replace("\\", " ")
    text = text.replace("{", " ")
    text = text.replace("}", " ")
    text = text.replace("=", " equals ")
    text = text.replace("+", " plus ")
    text = text.replace("-", " minus ")

    # Markdown formatting
    text = text.replace("*", "").replace("#", "")

    # Fix multiple spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


async def generate_speech(text, voice, output_file, sem, retries=3):
    async with sem:
        for attempt in range(retries):
            try:
                communicate = edge_tts.Communicate(text, voice, rate="-25%")
                await communicate.save(output_file)
                # Verify file was actually created and is not empty
                if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                    return True
            except Exception as e:
                pass
            await asyncio.sleep(2**attempt)
        print(" [DROP]", end="", flush=True)
        return False


async def _generate_all_speech(tasks):
    await asyncio.gather(*tasks)


def generate_podcast_audio(script_text, output_path):
    print(
        f"\n      [AUDIO] Regenerating TTS audio for {output_path.name}...",
        end=" ",
        flush=True,
    )
    lines = script_text.split("\n")

    female_voice = "en-US-JennyNeural"
    male_voice = "en-US-GuyNeural"
    segments = []

    # Limit to 3 concurrent connections to avoid edge-tts rate limits and dropping lines
    sem = asyncio.Semaphore(3)

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
                # Apply LaTeX cleanup
                text_to_speak = clean_latex_for_speech(text_to_speak)
                temp_file = Path(temp_dir) / f"{idx}.mp3"
                tasks.append(generate_speech(text_to_speak, voice, str(temp_file), sem))
                segments.append(str(temp_file))
                idx += 1

        if tasks:
            asyncio.run(_generate_all_speech(tasks))

            with open(output_path, "wb") as outfile:
                for mp3_path in segments:
                    if os.path.exists(mp3_path):
                        with open(mp3_path, "rb") as infile:
                            outfile.write(infile.read())
            print(f"[OK] Saved")
        else:
            print("[WARN] No Host dialogue found in script.")


def main():
    print("=" * 65)
    print("  LaTeX Cleaner & Audio Regenerator | Physics Chapters 4 & 5")
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

            print(f"  [*] Level: {level}")

            for podcast_type in ["short_podcast", "long_podcast"]:
                md_path = level_dir / f"{podcast_type}.md"
                mp3_path = level_dir / f"{podcast_type}.mp3"

                if not md_path.exists():
                    continue

                print(f"      [..] Reading {podcast_type}.md...")
                script_text = md_path.read_text(encoding="utf-8")
                generate_podcast_audio(script_text, mp3_path)


if __name__ == "__main__":
    main()
