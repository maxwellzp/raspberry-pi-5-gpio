from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()
btn = Button(2)
samples = "/usr/share/sonic-pi/samples/"
drum = Sound(f"{samples}/drum_bass_soft.flac")

def play_sound():
    print("Playing sound...")
    drum.play()

btn.when_pressed = play_sound
pause()
