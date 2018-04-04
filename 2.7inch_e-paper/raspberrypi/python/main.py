##
 #  @filename   :   main.cpp
 #  @brief      :   2.7inch e-paper display demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     August 16 2017
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

import epd2in7
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def main():
    epd = epd2in7.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)    # 255: clear the image with white
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 18)
    draw.text((20, 50), 'e-Paper demo', font = font, fill = 0)
    draw.rectangle((0, 76, 176, 96), fill = 0)
    draw.text((18, 80), 'Hello world!', font = font, fill = 255)
    draw.line((10, 130, 10, 180), fill = 0)
    draw.line((10, 130, 50, 130), fill = 0)
    draw.line((50, 130, 50, 180), fill = 0)
    draw.line((10, 180, 50, 180), fill = 0)
    draw.line((10, 130, 50, 180), fill = 0)
    draw.line((50, 130, 10, 180), fill = 0)
    draw.arc((90, 190, 150, 250), 0, 360, fill = 0)
    draw.chord((90, 120, 150, 180), 0, 360, fill = 0)
    draw.rectangle((10, 200, 50, 250), fill = 0)

    epd.display_frame(epd.get_frame_buffer(image))

    # display images
    epd.display_frame(epd.get_frame_buffer(Image.open('monocolor.bmp')))

if __name__ == '__main__':
    main()
