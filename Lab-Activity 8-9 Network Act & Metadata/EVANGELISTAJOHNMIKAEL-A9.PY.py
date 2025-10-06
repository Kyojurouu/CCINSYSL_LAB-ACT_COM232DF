"""
Activity 9 - EXIF Metadata Analysis
"""

import sys
from PIL import Image
import piexif

def read_exif(path):
    img = Image.open(path)
    exif_dict = piexif.load(img.info.get("exif", b""))

    make = exif_dict['0th'].get(piexif.ImageIFD.Make, b"").decode(errors='ignore')
    model = exif_dict['0th'].get(piexif.ImageIFD.Model, b"").decode(errors='ignore')
    dt = exif_dict['0th'].get(piexif.ImageIFD.DateTime, b"").decode(errors='ignore')

    gps = exif_dict.get('GPS', {})

    print("EXIF Metadata Analysis:")
    print(f"Camera Make: {make}")
    print(f"Camera Model: {model}")
    print(f"Date/Time: {dt}")
    if gps:
        print("GPS tags found in EXIF (raw):")
        print(gps)
    else:
        print("No GPS metadata found.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python exif_reader.py image.jpg")
    else:
        read_exif(sys.argv[1])
