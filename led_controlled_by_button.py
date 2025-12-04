from gpiozero import LED, Button
from signal import pause

led = LED(25)
btn = Button(21)

btn.when_pressed = led.on
btn.when_released = led.off

pause()