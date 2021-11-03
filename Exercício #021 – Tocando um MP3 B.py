"""Exercício Python 21: Faça um programa em Python que abra e
reproduza o áudio de um arquivo MP3."""

import pygame

# --------------------------------------------------------------------------


print(f"\n\n\033[1;91m'☼☼☼☼☼☼☼☼☼☼ Tocando um mp3 ☼☼☼☼☼☼☼☼☼☼'\033[m\n")

pygame.mixer.init()
pygame.mixer.music.load('Messa - Blood.mp3')
pygame.mixer.music.play()

# --------------------------------------------------------------------------


# import playsound
# playsound.playsound('Messa - Blood.mp3')
#
# print("""fim do Exercício!
#         Boa Aula!""")
