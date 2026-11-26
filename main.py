"""Copy the entry image into the requested output directory.

The entry is a finished front-page image, entry.png, which ships in
this repository next to this program. Running this program copies that
image, byte for byte, into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable (default /output), creating
the directory first when it does not exist yet.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(OUTPUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
