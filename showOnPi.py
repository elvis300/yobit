#!/usr/bin/env python
from YoBit import YoBit
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont



def formated_ticker2(yo, pair):
    print "in formated_ticker"
    ticker = yo.ticker(pair)
    for key, val in ticker[pair].iteritems():
        if key == "last":
            return val


def main():
    
  font = ImageFont.load_default()
  device = sh1106(port=1, address=0x3C)
  yo = YoBit() 
  with canvas(device) as draw:
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    x= padding
    shape_width = 20
    top = padding
    raw = top
    bottom = device.height - padding - 1
    font = ImageFont.load_default()

    pair = "dcr_btc"
    last = formated_ticker2(yo,pair)
    #print last


    draw.text((x, raw),    'decred',  font=font, fill=255)
    draw.text((x+40 , raw), str(last), font=font, fill=255)
    
    pair = "etc_btc"
    last = formated_ticker2(yo,pair)
    x = padding
    raw = raw + 40
    draw.text((x, raw),    'ETC',  font=font, fill=255)
    draw.text((x+40 , raw), str(last), font=font, fill=255)

if __name__ == '__main__':
    main()
