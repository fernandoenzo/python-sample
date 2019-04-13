#!/usr/bin/env python3
# encoding:utf-8


from pathlib import Path

from PIL import Image

FOLDER = Path(__file__).absolute().parent.parent


def show_star_wars():
    image = Image.open(f'{FOLDER}/static/sw.png')
    image.show()
