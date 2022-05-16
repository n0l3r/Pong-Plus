# Modules
import pygame,sys
from modules.Game import Game

# PYGAME INIT
pygame.init()
fps_clock = pygame.time.Clock()

# Display Setting
SIZE = (1280, 720)
icon = pygame.image.load("assets/images/icon.png")
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

g = Game(screen, fps_clock)

# Mainloop
while True:
    g.play()