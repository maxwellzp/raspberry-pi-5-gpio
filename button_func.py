from gpiozero import Button
from signal import pause

btn = Button(21)

def button_pressed():
    print("Button was pressed")

btn.when_pressed = button_pressed
pause()