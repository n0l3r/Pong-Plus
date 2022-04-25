import pygame
from modules import Menu

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
play_menu = Menu.Play()
about_menu = Menu.About()
info_menu = Menu.Info()

while PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if page_menu == "main_menu":
                if main_menu.play_btn.check(pygame.mouse.get_pos()):
                    page_menu = "play_menu"
                    play_menu.render(screen)
                elif main_menu.about_btn.check(pygame.mouse.get_pos()):
                    page_menu = "about_menu"
                    about_menu.render(screen)
                elif main_menu.info_btn.check(pygame.mouse.get_pos()):
                    page_menu = "info_menu"
                    info_menu.render(screen)
                elif main_menu.exit_btn.check(pygame.mouse.get_pos()):
                    PLAY = False
            elif page_menu == "about_menu":
                if about_menu.back_btn.check(pygame.mouse.get_pos()):
                    page_menu = "main_menu"
                    main_menu.render(screen)
            elif page_menu == "info_menu":
                if info_menu.back_btn.check(pygame.mouse.get_pos()):
                    page_menu = "main_menu"
                    main_menu.render(screen)
            elif page_menu == "play_menu":
                if play_menu.back_btn.check(pygame.mouse.get_pos()):
                    page_menu = "main_menu"
                    main_menu.render(screen)

    pygame.display.update()

pygame.quit()

