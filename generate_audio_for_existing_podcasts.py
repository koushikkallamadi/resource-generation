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
    import edge_tts
except ImportError:
    sys.exit("pip install edge-tts")

BASE_DIR = Path(".")
PHYSICS_DIR = BASE_DIR / "generated_resources" / "physics"
CHAPTERS = ["chapter_04", "chapter_05"]
LEVELS = ["01_beginner", "02_intermediate", "03_advanced"]
PODCAST_FILES = ["short_podcast.md", "long_podcast.md"]


# TTS Audio Logic
async def generate_speech(text, voice, output_file):
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
    except Exception as e:
        print(f" [TTS Error: {e}]", end="")


def generate_podcast_audio(script_text, output_path):
    print(
        f"      [AUDIO] Generating TTS audio for {output_path.name}...",
        end=" ",
        flush=True,
    )
    lines = script_text.split("\n")

    female_voice = "en-US-JennyNeural"
    male_voice = "en-US-GuyNeural"
    segments = []

    with tempfile.TemporaryDirectory() as temp_dir:
        idx = 0
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
                # Remove markdown formatting for TTS
                text_to_speak = text_to_speak.replace("*", "").replace("#", "")
                temp_file = Path(temp_dir) / f"{idx}.mp3"
                asyncio.run(generate_speech(text_to_speak, voice, str(temp_file)))

                if temp_file.exists():
                    segments.append(str(temp_file))
                idx += 1

        if segments:
            with open(output_path, "wb") as outfile:
                for mp3_path in segments:
                    with open(mp3_path, "rb") as infile:
                        outfile.write(infile.read())
            print(f"[OK] Saved")
        else:
            print("[WARN] No Host dialogue found in script.")


def main():
    print("=" * 65)
    print("  TTS Audio Generator for Existing Podcasts | Physics Ch 4 & 5")
    print("=" * 65)

    for ch_name in CHAPTERS:
        ch_dir = PHYSICS_DIR / ch_name
        if not ch_dir.exists():
            print(f"  [MISSING] {ch_dir} not found.")
            continue

        print(f"\n[>>] Processing {ch_name}")

        for level in LEVELS:
            level_dir = ch_dir / level
            if not level_dir.exists():
                print(f"  [WARN] Level directory {level_dir} missing.")
                continue

            print(f"  [*] Level: {level}")

            for md_filename in PODCAST_FILES:
                md_path = level_dir / md_filename
                mp3_path = level_dir / md_filename.replace(".md", ".mp3")

                if not md_path.exists():
                    print(f"      [SKIP] {md_filename} not found.")
                    continue

                if mp3_path.exists():
                    print(f"      [SKIP] {mp3_path.name} already exists.")
                    continue

                print(f"      [..] Reading {md_filename}...")
                script_text = md_path.read_text(encoding="utf-8")
                generate_podcast_audio(script_text, mp3_path)


if __name__ == "__main__":
    main()
