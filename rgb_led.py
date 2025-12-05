from gpiozero import RGBLED
from time import sleep

led = RGBLED(14,15,18)

led.red = 1
sleep(1)
led.red = 0.5
sleep(1)
led.color = (0, 1, 0)
sleep(1)
led.color = (1, 0, 1)
sleep(1)
led.color = (1, 1, 0)
sleep(1)
led.color = (0, 1, 1)
sleep(1)
led.color = (1, 1, 1)
sleep(1)
led.color = (0, 0, 0)
sleep(1)


# Change brightness for the led via pulse-width modulation
for n in range(100):
    led.blue = n / 100
    sleep(0.1)

led.color = (0, 0, 0)

