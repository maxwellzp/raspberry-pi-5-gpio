from gpiozero import MotionSensor, Buzzer
from time import sleep

pir = MotionSensor(4) # HC-SR501
buzzer = Buzzer(17) # Active buzzer

print("Waiting for PIR to settle...")
pir.wait_for_no_motion()

while True:
    print("Ready")
    
    pir.wait_for_motion()
    print("Motion detected!")
    buzzer.beep(0.5, 0.25, n=3)
    
    pir.wait_for_no_motion() 
    print("No motion.")

