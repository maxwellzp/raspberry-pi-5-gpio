from gpiozero import Button

btn = Button(21)

while True:
    if btn.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

