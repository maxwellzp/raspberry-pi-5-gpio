from gpiozero import LEDCharDisplay
from time import sleep
import sys

display = LEDCharDisplay(
    17, 27, 24, 23, 22, 18, 25,  # a,b,c,d,e,f,g
    active_high=True   # 5161AS — common cathode
)

if len(sys.argv) > 1 and sys.argv[1] == 'clear':
    display.off()
    exit()

while True:
    for dig in "0123456789":
        print("Display:", dig)
        display.value = dig
        sleep(1)

