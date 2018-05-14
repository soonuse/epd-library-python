##
 #  @filename   :   main.cpp
 #  @brief      :   2.13inch e-paper display (B) demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     August 15 2017
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

import epd2in13b
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#import imagedata

COLORED = 1
UNCOLORED = 0

def main():
    epd = epd2in13b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * (epd.width * epd.height / 8)
    frame_red = [0xFF] * (epd.width * epd.height / 8)

    # For simplicity, the arguments are explicit numerical coordinates
    epd.draw_rectangle(frame_black, 10, 60, 50, 100, COLORED);
    epd.draw_line(frame_black, 10, 60, 50, 100, COLORED);
    epd.draw_line(frame_black, 50, 60, 10, 100, COLORED);
    epd.draw_circle(frame_black, 80, 80, 15, COLORED);
    epd.draw_filled_rectangle(frame_red, 10, 120, 50, 180, COLORED);
    epd.draw_filled_rectangle(frame_red, 0, 6, 128, 26, COLORED);
    epd.draw_filled_circle(frame_red, 80, 150, 15, COLORED);

    # write strings to the buffer
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 12)
    epd.draw_string_at(frame_black, 4, 30, "e-Paper Demo", font, COLORED)
    epd.draw_string_at(frame_red, 6, 10, "Hello world!", font, UNCOLORED)
    # display the frames
    epd.display_frame(frame_black, frame_red)

    # display images
    frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
    frame_red = epd.get_frame_buffer(Image.open('red.bmp'))
    epd.display_frame(frame_black, frame_red)

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_RED)

if __name__ == '__main__':
    main()
