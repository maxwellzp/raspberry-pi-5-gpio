from gpiozero import LED
from time import sleep

red = LED(25)
yellow = LED(8)
green = LED(7)

green.on()
yellow.off()
red.off()

while True:
    sleep(10)
    green.off()
    yellow.on()
    sleep(1)
    yellow.off()
    red.on()
    sleep(10)
    yellow.on()
    sleep(1)
    green.on()
    yellow.off()
    red.off()
