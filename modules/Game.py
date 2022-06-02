import pygame, sys
import random
from modules import Menu
from modules import PowerUp
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player
from modules.Loader import Loader
from modules.Board import Board
from modules.Button import Button



class Game:
    def __init__(self, screen:pygame.Surface, clock:pygame.time.Clock) -> None:
        self.screen = screen
        self.clock = clock
        self.FPS = 240
        self.loader = Loader()
        self.menu_dict = {}
        self.game_dict = {}
        self.difficulty = 0
        self.max_score = 0

        self.items_list = [PowerUp.SpeedUp, PowerUp.Striketrough, PowerUp.Expand, PowerUp.Shrink]


    # Main loop utk sementara
    def play(self):
        current_loop = "menu"

        while True:
            if current_loop == "menu":
                current_loop = self.__main_menu()

            if current_loop == "<in-game>":
                current_loop = self.__game_cycle()

            if current_loop == "<winner>":
                current_loop = self.__winner_page()

            if current_loop == "<exit>":
                return

    
    # Spawn PowerUp acak pada koordinat acak
    def spawn_item(self, active_items_list):
        item_idx = random.randint(0, 3)
        item_rnd = self.items_list[item_idx](random.randint(445, 645), random.randint(100, 501))

        while True:
            for i in active_items_list:
                if(item_rnd.rect.colliderect(i.rect)):
                    item_rnd.x = random.randint(445, 645)
                    item_rnd.y = random.randint(100, 501)
                    break
            else:
                break

        active_items_list.append(item_rnd)


    # Mengurus rendering PowerUp dan check collision dengan bola
    def item_handler(self, active_items_list, screen, ball, paddle_right, paddle_left):
        new_list = []

        for item in active_items_list:
            item.render(screen)
            
            # Jika bola menabrak rect item, aktifkan efek item, setiap efek punya durasi 5 detik
            if ball.rect.colliderect(item.rect):
                if item.item_id == 0 or item.item_id == 1:
                    # print("speed-up" if item.item_id == 0 else "striketrough")
                    item.give_effect(ball)

                if item.item_id == 2:
                    # print("expand")
                    item.give_effect(paddle_left if ball.vec_x > 0 else paddle_right)

                if item.item_id == 3:
                    # print("shrink")
                    item.give_effect(paddle_left if ball.vec_x < 0 else paddle_right)

            else:
                new_list.append(item)
        
        return new_list # Kembalikan list baru yang berisi item yang belum ditabrak bola


    # Game loop
    def __game_cycle(self):
        BALL_BASE_SPEED = (self.difficulty + 1)*2
        self.game_dict = self.loader.load_game(BALL_BASE_SPEED)

        board = self.game_dict["board"]
        ball = self.game_dict["ball"]
        paddle_left = self.game_dict["paddle_left"]
        paddle_right = self.game_dict["paddle_right"]
        player_left = self.game_dict["player_left"]
        player_right = self.game_dict["player_right"]

        active_item_list = []
        can_spawn_item = False

        # Reset screen
        self.screen.fill((0,0,0))

        # Render board
        screen_cpy = self.screen.copy()
        board.render(screen_cpy) # board di render ke copy dari screen agar pas di loop lebih cepat
        pygame.display.flip()

        # Screen baru untuk game
        game_screen = pygame.Surface([1091,601], pygame.SRCALPHA, 32).convert_alpha()
        self.game_dict["game_music"].set_volume(0.1)
        self.game_dict["game_music"].play(-1)

        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "<exit>"

                paddle_left.control(event)
                paddle_right.control(event)

            # Reset screen / render score
            game_screen.fill(pygame.Color(0,0,0,0))
            self.screen.fill(pygame.Color(0,0,0,0))
            self.screen.blit(screen_cpy, [0, 0])
            board.score_render(self.screen)

            # Gerakan objek game
            paddle_left.move(0, 601)
            paddle_right.move(0, 601)
            ball.move()

            # Render objek game
            paddle_left.render(game_screen)
            paddle_right.render(game_screen)
            ball.render(game_screen)

            # Summon item setiap 5 detik
            current_time = pygame.time.get_ticks() - board.timer.start_time
            summon_interval = 5000

            if current_time % summon_interval > 2000 and current_time > 1000:
                can_spawn_item = True

            if can_spawn_item and current_time % summon_interval < 1000 and len(active_item_list) <= 3:
                self.spawn_item(active_item_list)
                can_spawn_item = False

            # Tampilkan Item, cek collision dengan bola, dan perbarui list item aktif jika collision terjadi
            active_item_list = self.item_handler(active_item_list, game_screen, ball, paddle_right, paddle_left)

            # Handler untuk modifier objek game, mengurus aktifasi/deaktifasi efek PowerUp
            paddle_left.handle_modifiers()
            paddle_right.handle_modifiers()
            ball.handle_modifiers()
                    
            # Reset bola jika skor didapatkan
            if ball.rect.centerx < 0:
                ball = Ball(ball.image, 545, 300, (self.difficulty + 1)*2, 180)
                player_right.update_score()
                board.score_boxes[1].set_value(player_right.score)

            if ball.rect.centerx > 1096:
                ball = Ball(ball.image, 545, 300, (self.difficulty + 1)*2, 0)  
                player_left.update_score()
                board.score_boxes[0].set_value(player_left.score)

            # Cek utk menentukan pantulan bola
            ball.bounce_check(0, 601, paddle_left, paddle_right)

            self.screen.blit(game_screen, [board.x + 30, board.y + 30])
            pygame.display.update([board.x, 0, board.width + 55, 720])
            self.clock.tick(self.FPS)

            # Sementara exit setelah menang (Nanti diubah ketika halaman pemenang sudah dibuat)
            if player_left.score >= self.max_score or player_right.score >= self.max_score:
                self.game_dict["game_music"].stop()
                return "<winner>"


    # Pause loop
    def __pause_cycle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        self.clock.tick(self.FPS)


    # Menu Cycle
    def __main_menu(self):
        self.menu_dict = self.loader.load_menu()
        current_menu = "main_menu"

        # Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Menu button clicks
                    current_menu = Menu.change_menu(self.menu_dict, current_menu, self.screen)

                    # Exit menu
                    if current_menu not in self.menu_dict:
                        self.difficulty = self.menu_dict["play_menu"].difficulty
                        self.max_score = self.menu_dict["play_menu"].max_score
                        return current_menu

                # Render menu
                self.menu_dict[current_menu].render(self.screen)
               
            pygame.display.update()
            self.clock.tick(self.FPS)


    # Halaman pemenang
    def __winner_page(self):
        player_left = self.game_dict["player_left"]
        player_right = self.game_dict["player_right"]

        winner_page = pygame.image.load("assets/images/winner_page.png")
        player_win = pygame.image.load("assets/images/winner_player1.png") if player_left.score > player_right.score else pygame.image.load("assets/images/winner_player2.png")
        back_img = pygame.image.load("assets/button/mainmenu_btn.png")
        playagain_img = pygame.image.load("assets/button/playagain_btn.png")

        playagain_btn = Button(image=playagain_img, pos=(505, 477))
        mainmenu_btn = Button(image=back_img, pos=(505, 542))

        # Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Button clicks
                    if playagain_btn.check(pygame.mouse.get_pos()):
                        player_left.reset_score()
                        player_right.reset_score()
                        return "<in-game>"

                    if mainmenu_btn.check(pygame.mouse.get_pos()):
                        return "menu"

            # Render winner page
            self.screen.blit(winner_page, [0, 0])
            self.screen.blit(player_win, (351, 277))
            playagain_btn.render(self.screen)
            mainmenu_btn.render(self.screen)

            pygame.display.update()
            self.clock.tick(self.FPS)
