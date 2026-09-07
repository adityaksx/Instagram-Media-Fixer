import os
from pathlib import Path

# ✅ Supported file type signatures
magic_signatures = {
    b'\xFF\xD8\xFF\xE0': '.jpg',
    b'\xFF\xD8\xFF\xE1': '.jpg',
    b'\x89PNG': '.png',
    b'GIF8': '.gif',
    b'RIFF': '.webp',              # With WEBP near byte 8
    b'\x00\x00\x00\x18': '.mp4',
    b'\x00\x00\x00\x20': '.mp4',
    b'\x1A\x45\xDF\xA3': '.mkv',
    b'\x00\x00\x00\x14ftypqt': '.mov',
    b'\x00\x00\x00\x1Cftypheic': '.heic',
    b'\x00\x00\x00\x1Cftypheix': '.heic'
}

# ✅ Set your export base folder here
base_dir = Path("G:\meta")  # 👈 Change to match your export root

# ✅ Logs
renamed_log = []
unknown_log = []

def detect_extension(file_path: Path) -> str | None:
    try:
        with open(file_path, 'rb') as f:
            header = f.read(20)
            # JPEG first
            if header.startswith(b'\xFF\xD8\xFF\xE0') or header.startswith(b'\xFF\xD8\xFF\xE1'):
                return '.jpg'
            # Special case for WEBP
            if header.startswith(b'RIFF') and b'WEBP' in header[8:16]:
                return '.webp'
            # General match
            for sig, ext in magic_signatures.items():
                if header.startswith(sig):
                    return ext
    except Exception as e:
        print(f"⚠️ Error reading {file_path}: {e}")
    return None

def process_all_files(folder: Path):
    print(f"\n🔍 Scanning: {folder}")
    count = 0
    for root, _, files in os.walk(folder):
        for name in files:
            file = Path(root) / name
            if file.suffix == '':  # Only process files with no extension
                ext = detect_extension(file)
                if ext:
                    new_path = file.with_suffix(ext)
                    try:
                        file.rename(new_path)
                        renamed_log.append(f"{file} → {new_path}")
                        print(f"✅ {file.name} → {new_path.name}")
                        count += 1
                    except Exception as e:
                        print(f"⚠️ Rename failed: {file} → {e}")
                else:
                    unknown_log.append(str(file))
                    print(f"❓ Unknown: {file}")
    print(f"✔️ Finished folder: {folder}, Renamed: {count} files")

# Run main
if __name__ == "__main__":
    process_all_files(base_dir)

    # Write logs
    if renamed_log:
        with open("renamed_files.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(renamed_log))
        print(f"\n📝 Renamed log saved to renamed_files.txt")

    if unknown_log:
        with open("unknown_files.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(unknown_log))
        print(f"\n🛑 Unknown files logged to unknown_files.txt")
