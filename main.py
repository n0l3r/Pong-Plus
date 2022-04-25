import pygame
import sys
from modules import Button, Menu

pygame.init()

# size of the window
SIZE = (1280, 720)
PLAY = True
icon = pygame.image.load("assets/images/icon.png")

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong Plus")
pygame.display.set_icon(icon)

page_menu = "main_menu"

main_menu = Menu.Main()
main_menu.render(screen)
about_menu = Menu.About()
info_menu = Menu.Info()

menu_dict = {
    "main_menu":main_menu,
    "about_menu":about_menu,
    "info_menu":info_menu
}

while PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Menu button clicks
            page_menu = Menu.change_menu(menu_dict, page_menu, screen)
            if page_menu == "<exit>": PLAY=False
               
    pygame.display.update()

pygame.quit()


