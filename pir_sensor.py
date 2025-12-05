from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4) # HC-SR501

print("Waiting for HC-SR501 to settle")
pir.wait_for_no_motion()

while True:
    print("Ready")
    pir.wait_for_motion()
    print("Motion detected!")
    sleep(1)
