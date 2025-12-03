from gpiozero import LED
from signal import pause

red = LED(25)
red.blink()
# red.blink(on_time=1, off_time=2, n=3)
pause()
