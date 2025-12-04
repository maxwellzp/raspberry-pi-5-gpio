from gpiozero import Button, LED
from time import sleep
import random

led = LED(25)
player1 = Button(21)
player2 = Button(2)

time = random.uniform(5, 10)
sleep(time)
led.on()

while True:
    if player1.is_pressed:
        print("Player #1 wins!")
        break
    if player2.is_pressed:
        print("Player #2 wins!")
        break
led.off()
