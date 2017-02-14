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

# line_count = 0
# current_height = 0
# line_height = 35
FONT_PATH = os.path.join(os.path.dirname(__file__), 'COURIER.TTF')
FONT = ImageFont.truetype(FONT_PATH, size=30, encoding="utf-8")
# i = Image.new('RGB', (555, 1000))
# draw = ImageDraw.Draw(i)


def add_top(im: Image):
    im.paste(CLIPPY_TOP, (0, 0))
    return im


def add_line(im: Image, height):
    im.paste(CLIPPY_MID, (0, height))
    return im


def add_bottom(im: Image, height):
    im.paste(CLIPPY_LOW, (0, height))
    return im


def drawline(draw: ImageDraw.Draw, text, height):
    draw.text((30, height), text, (0, 0, 0), font=FONT)


def cut_bottom(im: Image, height):
    crop = im.crop((0, 0, 555, height))
    return crop


def get_img(text: str):
    current_height = 0
    line_height = 35
    i = Image.new('RGB', (555, 1000))
    draw = ImageDraw.Draw(i)

    i = add_top(i)
    current_height += TOP_H
    line_count = 1

    text_lines = textwrap.wrap(text, 28)
    for line in text_lines:
        i = add_line(i, current_height)
        line_count += 1
        current_height += MID_H

        drawline(draw, line, line_height)
        line_height += LINE_H

    i = add_bottom(i, current_height)
    current_height += LOW_H
    i = cut_bottom(i, current_height)

    return i

if __name__ == '__main__':
    input_text = input("Insert the text: ")
    get_img(text=input_text).show()
