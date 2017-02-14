from PIL import Image, ImageFont, ImageDraw
import textwrap


CLIPPY_TOP = '/top.png'
CLIPPY_MID = '/mid.png'
CLIPPY_LOW = '/low.png'

line_count = 0
current_height = 0
line_height = 35
font = ImageFont.truetype("COURIER.TTF", size=30, encoding="utf-8")
i = Image.new('RGB', (555, 1000))
draw = ImageDraw.Draw(i)


def add_top(im: Image):
    global current_height
    global line_count
    top = Image.open(CLIPPY_TOP)
    current_height += top.size[1]
    line_count = 1
    im.paste(top, (0, 0))
    return im


def add_line(im: Image):
    global line_count
    global current_height
    mid = Image.open(CLIPPY_MID)
    im.paste(mid, (0, current_height))
    line_count += 1
    current_height += mid.size[1]
    return im


def add_bottom(im: Image):
    global current_height
    low = Image.open(CLIPPY_LOW)
    im.paste(low, (0, current_height))
    current_height += low.size[1]
    return im


def drawline(im: Image, text):
    global line_height
    global draw
    global font
    draw.text((30, line_height), text, (0, 0, 0), font=font)
    line_height += 65


def cut_bottom(im: Image):
    global current_height
    crop = im.crop((0, 0, 555, current_height))
    return crop

if __name__ == '__main__':
    i = add_top(i)
    input_text = "Has anyone ever been far as decided to look even more like?"
    text_lines = textwrap.wrap(input_text, 28)
    for line in text_lines:
        i = add_line(i)
        drawline(i, line)
    i = add_bottom(i)
    i = cut_bottom(i)
    i.show()



