## General

    The 6.0 and 9.7 inch displays from waveshare have a different setup than many of the others. The pin usage (see Interfaces) differs from the implementation of the others. This requires developers to adapt their drivers. At the moment, there are only few resources to find.

    This script is fetched from @GregDMeyer https://github.com/GregDMeyer/IT8951 who implemented an IT8951 driver in python3. All kudos go to him!


# Interfaces
    IT8951 Driver HAT   Raspberry Pi (BCM)	Description'
    5V                  5V	                5V power input
    GND 	            GND             	Ground
    MISO	            P9	                MISO Pin of SPI
    MOSI	            P10	                MOSI Pin of SPI
    SCK	                P11	                SCK Pin of SPI
    CS	                P8 	                Chip selection of SPI (Low active)
    RST	                P17	                Reset pin (Low active)
    HRDY	            P24	                Busy stats pin (Low when busy)

![e-paper display](http://www.waveshare.com/img/devkit/general/e-Paper-Modules-CMP.jpg)
