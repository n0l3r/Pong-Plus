import pygame
import sys
from modules import Button, Menu

pygame.init()

# size of the window
SIZE = (1280, 720)
MENU_BG = (8, 32, 50)



screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")

PLAY = True
main_menu = Menu.MainMenu()
main_menu.render(screen)