# Faça um Programa que reproduza um audio Mp3
import pygame

pygame.init()
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load("021.mp3")

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda a conclusão da reprodução
while pygame.mixer.music.get_busy() == True:
    continue

# Finaliza o pygame
pygame.quit()
