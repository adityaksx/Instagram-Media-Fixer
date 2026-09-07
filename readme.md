# Instagram Media Fixer

A simple Python script that detects missing file extensions in Instagram-exported image and video files and renames them with the correct extension.

## About

When photos or videos are exported from Instagram as stories, some files may not have a file extension. This makes them difficult to open, identify, or organize.

**Instagram Media Fixer** reads the file signature (magic bytes) to determine the actual file type and automatically adds the appropriate extension.

It supports common formats including JPG, PNG, GIF, WEBP, MP4, MKV, MOV, and HEIC.

## Features

* Detects file types using file signatures (magic bytes)
* Fixes files that have no extension
* Supports images:

  * JPG
  * PNG
  * GIF
  * WEBP
  * HEIC
* Supports videos:

  * MP4
  * MKV
  * MOV
* Recursively scans folders and subfolders
* Logs successfully renamed files
* Logs files whose type could not be identified
* Does not modify files that already have an extension

## Requirements

* Python 3.x
* No external Python packages required

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/instagram-media-fixer.git
cd instagram-media-fixer
```

## Configuration

Open the Python script and change the `base_dir` variable to the folder containing your Instagram export:

```python
base_dir = Path("G:\\meta")
```

For example:

```python
base_dir = Path("D:\\Instagram Export")
```

## Usage

Run the script:

```bash
python "Instagram Image Fixer.py"
```

The script will:

1. Recursively scan the configured folder.
2. Find files without extensions.
3. Read their file signatures.
4. Identify supported image or video formats.
5. Rename the files with the detected extension.
6. Record renamed and unknown files in log files.

## Example

Before:

```text
Instagram Export/
├── IMG_001
├── IMG_002
├── VID_001
└── IMG_003.jpg
```

After:

```text
Instagram Export/
├── IMG_001.jpg
├── IMG_002.png
├── VID_001.mp4
└── IMG_003.jpg
```

Files that cannot be identified are left unchanged and recorded in:

```text
unknown_files.txt
```

Successfully renamed files are recorded in:

```text
renamed_files.txt
```

## How It Works

The script reads the beginning of each extensionless file and compares its binary signature against known file signatures.

For example:

```text
JPEG  → FF D8 FF
PNG   → 89 50 4E 47
GIF   → GIF8
WEBP  → RIFF + WEBP
MKV   → 1A 45 DF A3
```

The detected format is then used to generate the correct file extension.

## Notes

* Only files with no extension are processed.
* Existing files are renamed rather than copied.
* Always keep a backup of important exports before running file-renaming scripts.
* The supported signatures are defined in the Python script and can be extended if required.

## License

This project is provided for personal and educational use.
