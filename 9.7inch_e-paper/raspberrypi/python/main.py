##
 #  @filename   :   main.cpp
 #  @brief      :   7.5inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 28 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 ##

from time import sleep
from PIL import Image, ImageDraw, ImageFont
from sys import path
from IT8951 import constants


EPD_WIDTH = 1200
EPD_HEIGHT = 825

def main():

    from sys import path
    path += ['../../']

    from IT8951.display import AutoEPDDisplay

    display = AutoEPDDisplay(vcom=-2.06)
    print('VCOM set to', display.epd.get_vcom())

# 1. Clear Display
    print('Clearing display...')
    display.clear()

# 2. Draw demo

    image = Image.new('1', (display.width, display.height), 1)   
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    draw.rectangle((0, 6, 1200, 30), fill = 0)
    draw.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    draw.rectangle((200, 80, 600, 280), fill = 0)
    draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    draw.rectangle((0, 80, 160, 280), fill = 255)
    draw.arc((40, 80, 180, 220), 0, 360, fill = 0)

    color = 0x10
    display.frame_buf.paste(color, box=image)

    display.draw_full(constants.DisplayModes.GC16)

    sleep(1)

# 3. Clear Display
    print('Clearing display...')
    display.clear()

# 4. Draw Image

    print('Draw Image...')

    image = Image.open('monocolor.bmp')

    dims = (display.width, display.height)

    image.thumbnail(dims)
    paste_coords = [dims[i] - image.size[i] for i in (0,1)]  # align image with bottom of display
    display.frame_buf.paste(image, paste_coords)

    display.draw_full(constants.DisplayModes.GC16)



if __name__ == '__main__':
    main()
