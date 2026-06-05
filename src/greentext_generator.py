from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os

output_name = input("Output: ")

FONT1 = ImageFont.truetype("arialbd.ttf", 24)
FONT2 = ImageFont.truetype("arial.ttf", 23)
FONT3 = ImageFont.truetype("arial.ttf", 21)

story = []

with open("story.txt", "r", encoding="utf-8") as file:
    for line in file:
        story.append(line.lower().strip())

IMAGES = os.listdir("assets/")
FILES = [f for f in IMAGES if os.path.isfile(os.path.join('assets/', f))]

CHOSEN_IMAGE_RAW = random.choice(FILES)
CHOSEN_IMG = Image.open(f"assets/{CHOSEN_IMAGE_RAW}").convert("RGBA")

LEFT_IMAGE = ImageOps.contain(CHOSEN_IMG, (200,250))
LEFT_IMAGE_POS = (22,59)

_,h =  LEFT_IMAGE.size

BG_COLOR = "#F8E9E2"
TOP_COLOR = "#EAD6CB"
TOP_OUTLINE = "#D8C7BC"

HEIGHT = 100 + (len(story) * 32)
WIDTH = 594

USER_TEXT = "Anonymous"
USER_TEXT_COLOR = "#3A6F4B"
USER_TEXT_POS = (10, 5)

DETAILS_TEXT_COLOR = "#59342C"
DETAILS_TEXT_POS = (195, 7)

IMG_HEIGHT = LEFT_IMAGE_POS[1]+5+h

IMG_SIZE_TEXT_POS = (22,IMG_HEIGHT)
IMG_SIZE_TEXT_COLOR = "#9C908E"

TEXT_COLOR = "#727B27"

days = ["Mon", "Tue", "Thu", "Sat", "Sun"]

def create():
    text_pos = [245, 59]

    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    shape = [0, 0, WIDTH, 38]

    draw.rectangle(shape, TOP_COLOR, TOP_OUTLINE, width=2)

    draw.text(USER_TEXT_POS, USER_TEXT, USER_TEXT_COLOR, FONT1)

    date, number, day, timestamp, img_size = random_details()

    draw.text(DETAILS_TEXT_POS, f"{date}({day}){timestamp} No.{number}", DETAILS_TEXT_COLOR, FONT2)

    img.paste(LEFT_IMAGE, LEFT_IMAGE_POS)

    draw.text(IMG_SIZE_TEXT_POS, f"{img_size} KB PNG", IMG_SIZE_TEXT_COLOR, FONT3)

    for line in story:
        draw.text((text_pos[0], text_pos[1]), line, TEXT_COLOR, FONT2)

        text_pos[1] += 32.5

        if text_pos[1] >= (IMG_HEIGHT+25):
            text_pos[0] = 22

    img.save(output_name)

def random_details():
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    year = random.randint(15, 24)

    number = random.randint(100000000, 999999999)
    day_word = random.choice(days)

    hour = random.randint(1, 12)
    minutes = random.randint(0, 59)
    second = random.randint(0, 59)

    img_size = random.randint(1,500)

    date = f"{month:02d}/{day:02d}/{year}"
    timestamp = f"{hour:02d}:{minutes:02d}:{second:02d}"

    return date, number, day_word, timestamp, img_size

if __name__ == "__main__":
    create()