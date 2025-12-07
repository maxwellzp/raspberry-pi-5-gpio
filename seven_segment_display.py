from gpiozero import LEDBoard
from time import sleep
import sys

segments = LEDBoard(a=17, b=27, c=24, d=23, e=22, f=18, g=25, pwm=False) #  5161AS (Common Cathode)

if len(sys.argv) > 1 and sys.argv[1] == 'clear':
    segments.off()
    exit()

digits = {
    0: ('a','b','c','d','e','f'),
    1: ('b','c'),
    2: ('a','b','d','e','g'),
    3: ('a','b','c','d','g'),
    4: ('b','c','f','g'),
    5: ('a','c','d','f','g'),
    6: ('a','c','d','e','f','g'),
    7: ('a','b','c'),
    8: ('a','b','c','d','e','f','g'),
    9: ('a','b','c','d','f','g')
}


def display_digit(num):
    # turn off all segments
    segments.off()

    for seg in digits[num]:
        getattr(segments, seg).on()

while True:
    for dig in range(10):
        print("Display: ", dig)
        display_digit(dig)
        sleep(1)
    
