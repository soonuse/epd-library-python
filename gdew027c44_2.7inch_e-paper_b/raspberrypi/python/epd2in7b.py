##
 #  @filename   :   epd2in7b.py
 #  @brief      :   Implements for Dual-color e-paper library
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 31 2017
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
 #

import epdif
import Image
import ImageDraw
import ImageFont
import RPi.GPIO as GPIO

# Display resolution
EPD_WIDTH       = 176
EPD_HEIGHT      = 264

# EPD2IN7B commands
PANEL_SETTING                               = 0x00
POWER_SETTING                               = 0x01
POWER_OFF                                   = 0x02
POWER_OFF_SEQUENCE_SETTING                  = 0x03
POWER_ON                                    = 0x04
POWER_ON_MEASURE                            = 0x05
BOOSTER_SOFT_START                          = 0x06
DEEP_SLEEP                                  = 0x07
DATA_START_TRANSMISSION_1                   = 0x10
DATA_STOP                                   = 0x11
DISPLAY_REFRESH                             = 0x12
DATA_START_TRANSMISSION_2                   = 0x13
PARTIAL_DATA_START_TRANSMISSION_1           = 0x14
PARTIAL_DATA_START_TRANSMISSION_2           = 0x15
PARTIAL_DISPLAY_REFRESH                     = 0x16
LUT_FOR_VCOM                                = 0x20
LUT_WHITE_TO_WHITE                          = 0x21
LUT_BLACK_TO_WHITE                          = 0x22
LUT_WHITE_TO_BLACK                          = 0x23
LUT_BLACK_TO_BLACK                          = 0x24
PLL_CONTROL                                 = 0x30
TEMPERATURE_SENSOR_COMMAND                  = 0x40
TEMPERATURE_SENSOR_CALIBRATION              = 0x41
TEMPERATURE_SENSOR_WRITE                    = 0x42
TEMPERATURE_SENSOR_READ                     = 0x43
VCOM_AND_DATA_INTERVAL_SETTING              = 0x50
LOW_POWER_DETECTION                         = 0x51
TCON_SETTING                                = 0x60
TCON_RESOLUTION                             = 0x61
SOURCE_AND_GATE_START_SETTING               = 0x62
GET_STATUS                                  = 0x71
AUTO_MEASURE_VCOM                           = 0x80
VCOM_VALUE                                  = 0x81
VCM_DC_SETTING_REGISTER                     = 0x82
PROGRAM_MODE                                = 0xA0
ACTIVE_PROGRAM                              = 0xA1
READ_OTP_DATA                               = 0xA2

# Display orientation
ROTATE_0                                    = 0
ROTATE_90                                   = 1
ROTATE_180                                  = 2
ROTATE_270                                  = 3

class EPD:
    def __init__(self):
        self.reset_pin = epdif.RST_PIN
        self.dc_pin = epdif.DC_PIN
        self.busy_pin = epdif.BUSY_PIN
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
        self.rotate = ROTATE_0

    lut_vcom_dc = [
        0x00    ,0x00,
        0x00    ,0x1A    ,0x1A    ,0x00    ,0x00    ,0x01,        
        0x00    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,        
        0x00    ,0x0E    ,0x01    ,0x0E    ,0x01    ,0x10,        
        0x00    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,        
        0x00    ,0x04    ,0x10    ,0x00    ,0x00    ,0x05,        
        0x00    ,0x03    ,0x0E    ,0x00    ,0x00    ,0x0A,        
        0x00    ,0x23    ,0x00    ,0x00    ,0x00    ,0x01    
    ]

    # R21H
    lut_ww = [
        0x90    ,0x1A    ,0x1A    ,0x00    ,0x00    ,0x01,
        0x40    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x84    ,0x0E    ,0x01    ,0x0E    ,0x01    ,0x10,
        0x80    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x00    ,0x04    ,0x10    ,0x00    ,0x00    ,0x05,
        0x00    ,0x03    ,0x0E    ,0x00    ,0x00    ,0x0A,
        0x00    ,0x23    ,0x00    ,0x00    ,0x00    ,0x01
    ]

    # R22H    r
    lut_bw = [
        0xA0    ,0x1A    ,0x1A    ,0x00    ,0x00    ,0x01,
        0x00    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x84    ,0x0E    ,0x01    ,0x0E    ,0x01    ,0x10,
        0x90    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0xB0    ,0x04    ,0x10    ,0x00    ,0x00    ,0x05,
        0xB0    ,0x03    ,0x0E    ,0x00    ,0x00    ,0x0A,
        0xC0    ,0x23    ,0x00    ,0x00    ,0x00    ,0x01
    ]

    # R23H    w
    lut_bb = [
        0x90    ,0x1A    ,0x1A    ,0x00    ,0x00    ,0x01,
        0x40    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x84    ,0x0E    ,0x01    ,0x0E    ,0x01    ,0x10,
        0x80    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x00    ,0x04    ,0x10    ,0x00    ,0x00    ,0x05,
        0x00    ,0x03    ,0x0E    ,0x00    ,0x00    ,0x0A,
        0x00    ,0x23    ,0x00    ,0x00    ,0x00    ,0x01
    ]

    # R24H    b
    lut_wb = [
        0x90    ,0x1A    ,0x1A    ,0x00    ,0x00    ,0x01,
        0x20    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x84    ,0x0E    ,0x01    ,0x0E    ,0x01    ,0x10,
        0x10    ,0x0A    ,0x0A    ,0x00    ,0x00    ,0x08,
        0x00    ,0x04    ,0x10    ,0x00    ,0x00    ,0x05,
        0x00    ,0x03    ,0x0E    ,0x00    ,0x00    ,0x0A,
        0x00    ,0x23    ,0x00    ,0x00    ,0x00    ,0x01
    ]

    def digital_write(self, pin, value):
        epdif.epd_digital_write(pin, value)

    def digital_read(self, pin):
        return epdif.epd_digital_read(pin)

    def delay_ms(self, delaytime):
        epdif.epd_delay_ms(delaytime)

    def send_command(self, command):
        self.digital_write(self.dc_pin, GPIO.LOW)
        # the parameter type is list but not int
        # so use [command] instead of command
        epdif.spi_transfer([command])

    def send_data(self, data):
        self.digital_write(self.dc_pin, GPIO.HIGH)
        # the parameter type is list but not int
        # so use [data] instead of data
        epdif.spi_transfer([data])

    def init(self):
        if (epdif.epd_init() != 0):
            return -1
        self.reset()

        self.send_command(POWER_ON)
        self.wait_until_idle()

        self.send_command(PANEL_SETTING)
        self.send_data(0xaf)        #KW-BF   KWR-AF    BWROTP 0f
        
        self.send_command(PLL_CONTROL)
        self.send_data(0x3a)       #3A 100HZ   29 150Hz 39 200HZ    31 171HZ

        self.send_command(POWER_SETTING)
        self.send_data(0x03)                  # VDS_EN, VDG_EN
        self.send_data(0x00)                  # VCOM_HV, VGHL_LV[1], VGHL_LV[0]
        self.send_data(0x2b)                  # VDH
        self.send_data(0x2b)                  # VDL
        self.send_data(0x09)                  # VDHR

        self.send_command(BOOSTER_SOFT_START)
        self.send_data(0x07)
        self.send_data(0x07)
        self.send_data(0x17)

        # Power optimization
        self.send_command(0xF8)
        self.send_data(0x60)
        self.send_data(0xA5)

        # Power optimization
        self.send_command(0xF8)
        self.send_data(0x89)
        self.send_data(0xA5)

        # Power optimization
        self.send_command(0xF8)
        self.send_data(0x90)
        self.send_data(0x00)
        
        # Power optimization
        self.send_command(0xF8)
        self.send_data(0x93)
        self.send_data(0x2A)

        # Power optimization
        self.send_command(0xF8)
        self.send_data(0x73)
        self.send_data(0x41)

        self.send_command(VCM_DC_SETTING_REGISTER)
        self.send_data(0x12)                   
        self.send_command(VCOM_AND_DATA_INTERVAL_SETTING)
        self.send_data(0x87)        # define by OTP

        self.set_lut()

        self.send_command(PARTIAL_DISPLAY_REFRESH)
        self.send_data(0x00)        

        return 0

    def wait_until_idle(self):
        while(self.digital_read(self.busy_pin) == 0):      # 0: busy, 1: idle
            self.delay_ms(100)

    def reset(self):
        self.digital_write(self.reset_pin, GPIO.LOW)         # module reset
        self.delay_ms(200)
        self.digital_write(self.reset_pin, GPIO.HIGH)
        self.delay_ms(200)    

    def set_lut(self):
        self.send_command(LUT_FOR_VCOM)               # vcom
        for count in range(0, 44):
            self.send_data(self.lut_vcom_dc[count])
        
        self.send_command(LUT_WHITE_TO_WHITE)         # ww --
        for count in range(0, 42):
            self.send_data(self.lut_ww[count])
        
        self.send_command(LUT_BLACK_TO_WHITE)         # bw r
        for count in range(0, 42):
            self.send_data(self.lut_bw[count])

        self.send_command(LUT_WHITE_TO_BLACK)         # wb w
        for count in range(0, 42):
            self.send_data(self.lut_bb[count])

        self.send_command(LUT_BLACK_TO_BLACK)         # bb b
        for count in range(0, 42):
            self.send_data(self.lut_wb[count])

    def get_frame_buffer(self, image):
        buf = [0xFF] * (self.width * self.height / 8)
        # Set buffer to value of Python Imaging Library image.
        # Image must be in mode 1.
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))

        pixels = image_monocolor.load()
        for y in range(self.height):
            for x in range(self.width):
                # Set the bits for the column of pixels at the current position.
                if pixels[x, y] != 0:
                    buf[(x + y * self.width) / 8] &= ~(0x80 >> (x % 8))
        return buf

    def display_frame(self, frame_buffer_black, frame_buffer_red):
        self.send_command(TCON_RESOLUTION)
        self.send_data(EPD_WIDTH >> 8)
        self.send_data(EPD_WIDTH & 0xff)        #176      
        self.send_data(EPD_HEIGHT >> 8)        
        self.send_data(EPD_HEIGHT & 0xff)       #264

        if (frame_buffer_black != None):
            self.send_command(DATA_START_TRANSMISSION_1)           
            self.delay_ms(2)
            for i in range(0, self.width * self.height / 8):
                self.send_data(frame_buffer_black[i])  
            self.delay_ms(2)                  
        if (frame_buffer_red != None):
            self.send_command(DATA_START_TRANSMISSION_2)
            self.delay_ms(2)
            for i in range(0, self.width * self.height / 8):
                self.send_data(frame_buffer_red[i])  
            self.delay_ms(2)        

        self.send_command(DISPLAY_REFRESH) 
        self.wait_until_idle()

    # After this command is transmitted, the chip would enter the deep-sleep
    # mode to save power. The deep sleep mode would return to standby by
    # hardware reset. The only one parameter is a check code, the command would
    # be executed if check code = 0xA5. 
    # Use EPD::Reset() to awaken and use EPD::Init() to initialize.
    def sleep(self):
        self.send_command(DEEP_SLEEP)
        self.send_data(0xa5)

    def set_rotate(self, rotate):
        if (rotate == ROTATE_0):
            self.rotate = ROTATE_0
            self.width = EPD_WIDTH
            self.height = EPD_HEIGHT
        elif (rotate == ROTATE_90): 
            self.rotate = ROTATE_90
            self.width = EPD_HEIGHT
            self.height = EPD_WIDTH
        elif (rotate == ROTATE_180): 
            self.rotate = ROTATE_180
            self.width = EPD_WIDTH
            self.height = EPD_HEIGHT
        elif (rotate == ROTATE_270): 
            self.rotate = ROTATE_270
            self.width = EPD_HEIGHT
            self.height = EPD_WIDTH

    def set_pixel(self, frame_buffer, x, y, colored):
        if (x < 0 or x >= self.width or y < 0 or y >= self.height):
            return
        if (self.rotate == ROTATE_0):
            self.set_absolute_pixel(frame_buffer, x, y, colored)
        elif (self.rotate == ROTATE_90):
            point_temp = x
            x = EPD_WIDTH - y
            y = point_temp
            self.set_absolute_pixel(frame_buffer, x, y, colored)
        elif (self.rotate == ROTATE_180):
            x = EPD_WIDTH - x
            y = EPD_HEIGHT- y
            self.set_absolute_pixel(frame_buffer, x, y, colored)
        elif (self.rotate == ROTATE_270):
            point_temp = x
            x = y
            y = EPD_HEIGHT - point_temp
            self.set_absolute_pixel(frame_buffer, x, y, colored)
    
    def set_absolute_pixel(self, frame_buffer, x, y, colored):
        # To avoid display orientation effects
        # use EPD_WIDTH instead of self.width
        # use EPD_HEIGHT instead of self.height
        if (x < 0 or x >= EPD_WIDTH or y < 0 or y >= EPD_HEIGHT):
            return
        if (colored):
            frame_buffer[(x + y * EPD_WIDTH) / 8] |= 0x80 >> (x % 8)
        else:
            frame_buffer[(x + y * EPD_WIDTH) / 8] &= ~(0x80 >> (x % 8))

    def draw_string_at(self, frame_buffer, x, y, text, font, colored):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.text((x, y), text, font = font, fill = 255)
        # Set buffer to value of Python Imaging Library image.
        # Image must be in mode 1.
        pixels = image.load()
        for y in range(self.height):
            for x in range(self.width):
                # Set the bits for the column of pixels at the current position.
                if pixels[x, y] != 0:
                    self.set_pixel(frame_buffer, x, y, colored)

    def draw_line(self, frame_buffer, x0, y0, x1, y1, colored):
        # Bresenham algorithm
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while((x0 != x1) and (y0 != y1)):
            self.set_pixel(frame_buffer, x0, y0 , colored)
            if (2 * err >= dy):
                err += dy
                x0 += sx
            if (2 * err <= dx):
                err += dx
                y0 += sy

    def draw_horizontal_line(self, frame_buffer, x, y, width, colored):
        for i in range(x, x + width):
            self.set_pixel(frame_buffer, i, y, colored)

    def draw_vertical_line(self, frame_buffer, x, y, height, colored):
        for i in range(y, y + height):
            self.set_pixel(frame_buffer, x, i, colored)

    def draw_rectangle(self, frame_buffer, x0, y0, x1, y1, colored):
        min_x = x0 if x1 > x0 else x1
        max_x = x1 if x1 > x0 else x0
        min_y = y0 if y1 > y0 else y1
        max_y = y1 if y1 > y0 else y0
        self.draw_horizontal_line(frame_buffer, min_x, min_y, max_x - min_x + 1, colored)
        self.draw_horizontal_line(frame_buffer, min_x, max_y, max_x - min_x + 1, colored)
        self.draw_vertical_line(frame_buffer, min_x, min_y, max_y - min_y + 1, colored)
        self.draw_vertical_line(frame_buffer, max_x, min_y, max_y - min_y + 1, colored)

    def draw_filled_rectangle(self, frame_buffer, x0, y0, x1, y1, colored):
        min_x = x0 if x1 > x0 else x1
        max_x = x1 if x1 > x0 else x0
        min_y = y0 if y1 > y0 else y1
        max_y = y1 if y1 > y0 else y0
        for i in range(min_x, max_x + 1):
            self.draw_vertical_line(frame_buffer, i, min_y, max_y - min_y + 1, colored)

    def draw_circle(self, frame_buffer, x, y, radius, colored):
        # Bresenham algorithm
        x_pos = -radius
        y_pos = 0
        err = 2 - 2 * radius
        if (x >= self.width or y >= self.height):
            return
        while True:
            self.set_pixel(frame_buffer, x - x_pos, y + y_pos, colored)
            self.set_pixel(frame_buffer, x + x_pos, y + y_pos, colored)
            self.set_pixel(frame_buffer, x + x_pos, y - y_pos, colored)
            self.set_pixel(frame_buffer, x - x_pos, y - y_pos, colored)
            e2 = err
            if (e2 <= y_pos):
                y_pos += 1
                err += y_pos * 2 + 1
                if(-x_pos == y_pos and e2 <= x_pos):
                    e2 = 0
            if (e2 > x_pos):
                x_pos += 1
                err += x_pos * 2 + 1
            if x_pos > 0:
                break

    def draw_filled_circle(self, frame_buffer, x, y, radius, colored):
        # Bresenham algorithm
        x_pos = -radius
        y_pos = 0
        err = 2 - 2 * radius
        if (x >= self.width or y >= self.height):
            return
        while True:
            self.set_pixel(frame_buffer, x - x_pos, y + y_pos, colored)
            self.set_pixel(frame_buffer, x + x_pos, y + y_pos, colored)
            self.set_pixel(frame_buffer, x + x_pos, y - y_pos, colored)
            self.set_pixel(frame_buffer, x - x_pos, y - y_pos, colored)
            self.draw_horizontal_line(frame_buffer, x + x_pos, y + y_pos, 2 * (-x_pos) + 1, colored);
            self.draw_horizontal_line(frame_buffer, x + x_pos, y - y_pos, 2 * (-x_pos) + 1, colored);
            e2 = err
            if (e2 <= y_pos):
                y_pos += 1
                err += y_pos * 2 + 1
                if(-x_pos == y_pos and e2 <= x_pos):
                    e2 = 0
            if (e2 > x_pos):
                x_pos  += 1
                err += x_pos * 2 + 1
            if x_pos > 0:
                break

### END OF FILE ###




























