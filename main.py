"""make.fun news-image-20261126: sum up 26 November 2026's world news.

The entry is one front-page image (entry.png, 1024x1024) drawn for this
bounty: six stories from Thursday 26 November 2026, with the date in the
masthead. The program just copies that image to the output path, so both
grader runs write the same bytes. No network, no randomness, no clock.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
IMAGE_NAME = "entry.png"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, IMAGE_NAME),
                os.path.join(OUT_DIR, IMAGE_NAME))
