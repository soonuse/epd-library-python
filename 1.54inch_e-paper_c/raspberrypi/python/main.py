##
 #  @filename   :   main.cpp
 #  @brief      :   epd1in54c e-paper demo
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     June 1 2018
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

import time
import epd1in54c
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#import imagedata

COLORED = 1
UNCOLORED = 0

def main():
    epd = epd1in54c.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * (epd.width * epd.height / 8)
    frame_red = [0xFF] * (epd.width * epd.height / 8)

    # For simplicity, the arguments are explicit numerical coordinates
    epd.draw_rectangle(frame_black, 10, 60, 50, 110, COLORED);
    epd.draw_line(frame_black, 10, 60, 50, 110, COLORED);
    epd.draw_line(frame_black, 50, 60, 10, 110, COLORED);
    epd.draw_circle(frame_black, 100, 80, 30, COLORED);
#    epd.draw_filled_rectangle(frame_red, 10, 130, 50, 180, COLORED);
    epd.draw_filled_rectangle(frame_red, 0, 6, 152, 26, COLORED);
#    epd.draw_filled_circle(frame_red, 120, 150, 30, COLORED);

    # write strings to the buffer
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 18)
    epd.display_string_at(frame_black, 10, 30, "e-Paper Demo", font, COLORED)
    epd.display_string_at(frame_red, 18, 10, "Hello world!", font, UNCOLORED)
    # display the frame
    epd.display_frame(frame_black, frame_red)
    time.sleep(2)
    # display images
    frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
    frame_red = epd.get_frame_buffer(Image.open('yellow.bmp'))
    epd.display_frame(frame_black, frame_red)

    epd.sleep()

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_RED)

if __name__ == '__main__':
    main()
