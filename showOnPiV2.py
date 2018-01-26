#!/usr/bin/env python
from yobit import YoBit
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

padding = 2
spacing = 30
x= padding
shape_width = 20
top = padding
raw = padding	

device = sh1106(port=1, address=0x3C)
bottom = device.height - padding - 1 
font = ImageFont.load_default()
yo = YoBit()

def formated_ticker2(yo, pair):
    print "formated_ticker with ",pair
    ticker = yo.ticker(pair)
    for key, val in ticker[pair].iteritems():
        if key == "last":
            return val

def printer(yo, pair):
	global raw
	with canvas(device) as draw:
		lastPrice = formated_ticker2(yo,pair)  
		draw.text((x, raw),    'BTC',  font=font, fill=255)
		draw.text((x+spacing , raw), str(lastPrice), font=font, fill=255)
		raw = raw + 10

def main():
 

  printer(yo,"btc_usd")
  printer(yo,"dcr_btc")
  printer(yo,"etc_btc")
  printer(yo,"cme_btc")

    

if __name__ == '__main__':
    main()
