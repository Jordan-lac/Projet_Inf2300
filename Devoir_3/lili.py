import pygame
import time

pygame.init()
pygame.mixer.init()

print("Chargement de la musique...")
pygame.mixer.music.load("assets/musique_1.mp3")  # Change le chemin si besoin
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
print("Lecture en cours :", pygame.mixer.music.get_busy())

# Attendre 10 secondes pour écouter
time.sleep(10)

pygame.quit()
