# Faça um programa em python que leia e reeproduza um audio de um aquivo mp3

# Desatualizado
'''import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()'''

# Atualizado
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
