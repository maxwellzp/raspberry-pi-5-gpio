from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(25)
btn = Button(21)

def button_released():
    print("Button was released")
    sleep(3)
    led.off()

btn.when_pressed = led.on
btn.when_released = button_released
pause()

