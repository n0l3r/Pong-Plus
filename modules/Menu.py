from abc import ABC, abstractmethod
import pygame, sys
from modules.Button import Button
pygame.mixer.init(buffer=64)
TITLE = "Pong Plus"

MENU_BG = (8, 32, 50)
GAME_BG = (1, 0, 6)
class Menu(ABC):

    click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
    click_sound.set_volume(0.5)

    def __init__(self, name):
        self.name = name

        # Logo dijadikan atribut kelas parent
        self.logo_pbb = pygame.image.load("assets/images/logo_pbb.png")
        self.logo_img = pygame.image.load("assets/images/Pong_Logo.png")
        

    @abstractmethod
    def render(self):
        pass


class Main(Menu):
    def __init__(self):
        super().__init__("main_menu")

        info_img = pygame.image.load("assets/button/info_btn.png")
        play_img = pygame.image.load("assets/button/play_btn.png")
        about_img = pygame.image.load("assets/button/about_btn.png")
        exit_img = pygame.image.load("assets/button/exit_btn.png")

        self.info_btn = Button(image=info_img, pos=(1220, 15))
        self.play_btn = Button(image=play_img, pos=(505, 400))
        self.about_btn = Button(image=about_img, pos=(505, 465))
        self.exit_btn = Button(image=exit_img, pos=(505, 530))


    def render(self, screen):
        screen.fill(MENU_BG)

        self.logo_pbb.set_alpha(255)
        screen.blit(self.logo_pbb, (15, 15))

        self.logo_img.set_alpha(255)
        screen.blit(self.logo_img, (494, 173))

        self.info_btn.render(screen)
        self.play_btn.render(screen)
        self.about_btn.render(screen)
        self.exit_btn.render(screen)


class About(Menu):
    def __init__(self, text_img_path):
        super().__init__("about_menu")

        back_img = pygame.image.load("assets/button/back_btn.png")
        self.back_btn = Button(image=back_img, pos=(505, 575))
        
        self.about_text = pygame.image.load(text_img_path)


    def render(self, screen):
        screen.fill(MENU_BG)

        self.logo_img.set_alpha(255)
        screen.blit(self.logo_pbb, (15, 15))
        
        self.logo_img.set_alpha(255)
        screen.blit(self.logo_img, (494, 173))
        
        self.about_text.set_alpha(255)
        screen.blit(self.about_text, (215, 125))

        self.back_btn.render(screen)


class Play(Menu):
    def __init__(self):
        super().__init__("play_menu")

        easy_img = pygame.image.load("assets/button/easy_btn.png")
        medium_img = pygame.image.load("assets/button/medium_btn.png")
        hard_img = pygame.image.load("assets/button/hard_btn.png")
        increase_img = pygame.image.load("assets/button/increase_btn.png")
        decrease_img = pygame.image.load("assets/button/decrease_btn.png")
        back_img = pygame.image.load("assets/button/back_btn.png")

        self.easy_btn = Button(image=easy_img, pos=(505, 203))
        self.medium_btn = Button(image=medium_img, pos=(505, 268)) 
        self.hard_btn = Button(image=hard_img, pos=(505, 333)) 
        self.increase_btn = Button(image=increase_img, pos=(734, 426)) 
        self.decrease_btn = Button(image=decrease_img, pos=(728, 450)) 
        self.back_btn = Button(image=back_img, pos=(505, 575))

        self.difficulty = None
        self.max_score = 1 # Attribut tambahan untuk skor maksimum


    def render(self, screen):
        screen.fill(MENU_BG)

        self.logo_pbb.set_alpha(255)
        screen.blit(self.logo_pbb, (15, 15))   
        
        self.easy_btn.render(screen)
        self.medium_btn.render(screen)
        self.hard_btn.render(screen)
        self.increase_btn.render(screen)
        self.decrease_btn.render(screen)
        self.back_btn.render(screen)

        score_img = pygame.image.load("assets/images/score_text.png")
        score_img.set_alpha(255)
        screen.blit(score_img, (494, 422))

        score_font = pygame.font.Font("assets/font/Montserrat-Regular.ttf", 32)
        score_text = score_font.render(str(self.max_score), True, (255, 255, 255), None)
        screen.blit(score_text, (660, 430))
        

def change_menu(menu:dict, crnt_page:str, screen):
    # Main Menu Page
    if crnt_page == "main_menu":
        if menu["main_menu"].play_btn.check(pygame.mouse.get_pos()):
            menu["play_menu"].render(screen)
            Menu.click_sound.play()
            return "play_menu"

        elif menu["main_menu"].about_btn.check(pygame.mouse.get_pos()):
            menu["about_menu"].render(screen)
            Menu.click_sound.play()
            return "about_menu"

        elif menu["main_menu"].info_btn.check(pygame.mouse.get_pos()):
            menu["info_menu"].render(screen)
            Menu.click_sound.play()
            return "info_menu"

        elif menu["main_menu"].exit_btn.check(pygame.mouse.get_pos()):
            Menu.click_sound.play()
            return "<exit>"

    # About Menu
    elif crnt_page == "about_menu":
        if menu["about_menu"].back_btn.check(pygame.mouse.get_pos()):
            menu["main_menu"].render(screen)
            Menu.click_sound.play()
            return "main_menu"

    # Info Menu
    elif crnt_page == "info_menu":
        if menu["info_menu"].back_btn.check(pygame.mouse.get_pos()):
            menu["main_menu"].render(screen)
            Menu.click_sound.play()
            return "main_menu"
            
    # Play Menu
    elif crnt_page == "play_menu":
        if menu["play_menu"].back_btn.check(pygame.mouse.get_pos()):
            menu["main_menu"].render(screen)
            Menu.click_sound.play()
            return "main_menu"
        
        if menu["play_menu"].increase_btn.check(pygame.mouse.get_pos()):
            menu["play_menu"].max_score += 1
            menu["play_menu"].render(screen)
            Menu.click_sound.play()
                    
        if menu["play_menu"].decrease_btn.check(pygame.mouse.get_pos()) and menu["play_menu"].max_score > 1:
            menu["play_menu"].max_score -= 1
            menu["play_menu"].render(screen)
            Menu.click_sound.play()

        if menu["play_menu"].easy_btn.check(pygame.mouse.get_pos()):
            menu["play_menu"].difficulty = 0
            return "<in-game>"

        if menu["play_menu"].medium_btn.check(pygame.mouse.get_pos()):
            menu["play_menu"].difficulty = 1
            return "<in-game>"

        if menu["play_menu"].hard_btn.check(pygame.mouse.get_pos()):
            menu["play_menu"].difficulty = 2
            return "<in-game>"

    # Else return default state
    return crnt_page
