from PIL import Image, ImageFont, ImageDraw
import textwrap
import os


CLIPPY_TOP = Image.open(os.path.join(os.path.dirname(__file__), 'top.png'))
CLIPPY_MID = Image.open(os.path.join(os.path.dirname(__file__), 'mid.png'))
CLIPPY_LOW = Image.open(os.path.join(os.path.dirname(__file__), 'low.png'))
TOP_H = CLIPPY_TOP.size[1]
MID_H = CLIPPY_MID.size[1]
LOW_H = CLIPPY_LOW.size[1]
LINE_H = 65
FONT_PATH = os.path.join(os.path.dirname(__file__), 'COURIER.TTF')
FONT = ImageFont.truetype(FONT_PATH, size=30, encoding="utf-8")


def get_img(text: str):
    current_height = 0
    line_height = 35
    i = Image.new('RGB', (555, 1000))
    draw = ImageDraw.Draw(i)

    i.paste(CLIPPY_TOP, (0, 0))

    current_height += TOP_H
    line_count = 1

    text_lines = textwrap.wrap(text, 28)
    for line in text_lines:
        i.paste(CLIPPY_MID, (0, current_height))
        line_count += 1
        current_height += MID_H
        draw.text((30, line_height), line, (0, 0, 0), font=FONT)
        line_height += LINE_H

    i.paste(CLIPPY_LOW, (0, current_height))
    current_height += LOW_H
    crop = i.crop((0, 0, 555, current_height))

    return crop

if __name__ == '__main__':
    input_text = input("Insert the text: ")
    get_img(text=input_text).show()
