import pathlib, subprocess, sys
import imageio_ffmpeg as ioff

INPUT_DIR = r"Inputs_mp3"
OUTPUT_DIR = r"Outputs_ogg"
RECURSIVE = False
OVERWRITE = False
QUALITY = 4
BITRATE = None

def convert_dir(src_dir, dst_dir, recursive=False, overwrite=False, quality=4, bitrate=None):
    ffmpeg = ioff.get_ffmpeg_exe()
    src = pathlib.Path(src_dir)
    dst = pathlib.Path(dst_dir)
    if not src.exists(): sys.exit(f"Input directory not found: {src}")
    dst.mkdir(parents=True, exist_ok=True)
    files = (p for p in (src.rglob("*") if recursive else src.iterdir()) if p.is_file() and p.suffix.lower()==".mp3")
    total=0; converted=0
    for mp3 in files:
        total+=1
        rel = mp3.relative_to(src) if recursive else pathlib.Path(mp3.name)
        out_dir = (dst / rel).parent
        out_dir.mkdir(parents=True, exist_ok=True)
        ogg = out_dir / (mp3.stem + ".ogg")
        if ogg.exists() and not overwrite:
            print(f"[skip] exists: {ogg}")
            continue
        cmd=[ffmpeg,"-hide_banner","-nostdin","-loglevel","error","-stats","-y" if overwrite else "-n","-i",str(mp3),"-vn","-map_metadata","0","-c:a","libvorbis"]
        if bitrate: cmd+=["-b:a",str(bitrate)]
        else: cmd+=["-q:a",str(quality)]
        cmd.append(str(ogg))
        proc=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if proc.returncode==0:
            print(f"[ok] {mp3} -> {ogg}")
            converted+=1
        else:
            print(f"[error] {mp3}\n{proc.stdout}")
    print(f"Done. Converted {converted}/{total} file(s).")

if __name__ == "__main__":
    convert_dir(INPUT_DIR, OUTPUT_DIR, RECURSIVE, OVERWRITE, QUALITY, BITRATE)
