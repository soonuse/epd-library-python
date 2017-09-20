# GDEM0213E26LT 2.13" e-paper library for Raspberry Pi
GDEM0213E26LT 2.13" e-paper library for Raspberry Pi
## Development environment
  * OS: Raspbian
  * Libraries: wiringPi/bcm2835/python
## Raspberry Pi GPIO Pin map 
    +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
    | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
    +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
    |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
    |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
    |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
    |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
    |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
    |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
    |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
    |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
    |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
    |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
    |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
    |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
    |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
    |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
    |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
    |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
    |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
    |  19 |  24 | GPIO.24 |  OUT | 1 | 35 || 36 | 1 | OUT  | GPIO.27 | 27  | 16  |
    |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
    |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
    +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
    | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
    +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
## Hardware connection (OLED => Raspberry Pi)
  * VCC    ->    3.3
  * GND    ->    GND
  * DIN    ->    MOSI
  * CLK    ->    SCLK
  * CS     ->    24 (Physical, BCM: CE0, 8)
  * D/C    ->    22 (Physical, BCM: 25)
  * RES    ->    11 (Physical, BCM: 17)
  * BUSY   ->    18 (Physical, BCM: 24)
## How to use
### based on WiringPi library
1.  install the C libraries of wiringPi,
    see: http://wiringpi.com/download-and-install/
    fortunately, in the latest version of Raspbian, wiringPi libraries are
    pre-installed.
2.  change the current directory to where the Makefile and demo file located.
3.  compile the file with: 
      make
4.  run the demo with: 
      sudo ./epd
### based on BCM2835 library
1.  install the C libraries of bcm2835, see: http://www.airspayce.com/mikem/bcm2835/
2.  change the current directory to where the Makefile and demo files located.
3.  compile the file with: 
      make
4.  run the demo with: 
      sudo ./epd
### based on Python
1.  install the PIL library (Python image library).
2.  run the demo with: 
      python main.py

