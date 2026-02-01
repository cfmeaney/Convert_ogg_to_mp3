# MP3 → OGG Batch Converter

A small Python script that batch converts `.mp3` files into `.ogg` files.

## What it does

- Reads `.mp3` files from an input folder
- Converts each file to `.ogg`
- Writes outputs to an output folder
- Optionally:
  - recurse through subfolders
  - overwrite existing `.ogg` files
  - choose quality-based encoding OR constant bitrate

## Usage

1. Put your mp3 files to be converted into

```
Inputs_mp3/
```

2. Run:

```bash
python Convert_mp3_to_ogg.py
```
3. Retrieve your converted .ogg files from

```
Outputs.ogg/
```
