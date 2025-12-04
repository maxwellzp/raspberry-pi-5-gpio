from gpiozero import Button

btn = Button(21)
btn.wait_for_press()
print("Button was pressed")
