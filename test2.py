import pygame
import tkinter as tk
from tkinter import *
import os


pygame.init()
window = pygame.display.set_mode((500,500))
window.fill(pygame.Color(255,255,255))
pygame.display.init()
pygame.display.update()




run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    pygame.display.flip()
