from abc import ABC, abstractmethod
import pygame
from modules.Button import Button

TITLE = "Pong Plus"

MENU_BG = (8, 32, 50)
GAME_BG = (1, 0, 6)

PLAY_BTN_IMG = pygame.image.load("assets/main_menu/play_btn.png")
ABOUT_BTN_IMG = pygame.image.load("assets/main_menu/about_btn.png")
EXIT_BTN_IMG = pygame.image.load("assets/main_menu/exit_btn.png")


class Menu(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def render(self):
        pass


class MainMenu(Menu):
    def __init__(self):
        super().__init__("Main Menu")

    def render(self, screen):
        screen.fill(MENU_BG)

        logo_pbb = pygame.image.load("assets/main_menu/logo_pbb.png")
        logo_pbb.set_alpha(255)
        screen.blit(logo_pbb, (15, 15))

        info_btn = pygame.image.load("assets/main_menu/info_btn.png")
        info_btn.set_alpha(255)
        screen.blit(info_btn, (1220, 15))

        logo_img = pygame.image.load("assets/main_menu/Pong_Logo.png")
        logo_img.set_alpha(255)
        screen.blit(logo_img, (494, 173))

        play_btn = Button(image=PLAY_BTN_IMG, pos=(505, 400))
        play_btn.render(screen)

        about_btn = Button(ABOUT_BTN_IMG, (505, 465))
        about_btn.render(screen)

        exit_btn = Button(EXIT_BTN_IMG, (505, 530))
        exit_btn.render(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


        