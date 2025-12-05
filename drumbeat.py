import pygame.mixer
from pygame.mixer import Sound
import time

pygame.mixer.init()
samples = "/usr/share/sonic-pi/samples/"
drum = Sound(f"{samples}/drum_bass_soft.flac")

while True:
    drum.play()
    time.sleep(1)
