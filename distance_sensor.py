from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2)

while True:
    distance = sensor.distance * 100
    print(f"Distance: {distance:.1f} cm")
    sleep(0.1)

# R1 = 1 kΩ
# R2 = 2 kΩ
# 5V / (1k + 2k) = 5V / 3000 Ω = 0.001666667×1000 = 1.66 mA

