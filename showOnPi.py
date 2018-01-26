#!/usr/bin/env python

# Ported from:
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import imp

font = ImageFont.load_default()
device = sh1106(port=1, address=0x3C)

with canvas(device) as draw:
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    x= padding
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
 

    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write two lines of text.
    draw.text((x, top),    'decred',  font=font, fill=255)
    draw.text((x+40 , top), '123!', font=font, fill=255)
