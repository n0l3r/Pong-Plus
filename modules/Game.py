import pygame, sys
from modules import Menu
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player
from modules.Loader import Loader
from modules.Board import Board


class Game:
    def __init__(self, screen:pygame.Surface, clock:pygame.time.Clock) -> None:
        self.screen = screen
        self.clock = clock
        self.FPS = 120
        self.loader = Loader()
        self.menu_dict = {}
        self.game_dict = {}
        self.difficulty = 0
        self.max_score = 0


    # Main loop utk sementara
    def play(self):
        current_loop = "menu"

        while True:
            if current_loop == "menu":
                current_loop = self.__main_menu()

            if current_loop == "<in-game>":
                current_loop = self.__game_cycle()

            if current_loop == "<exit>":
                return


    # Game loop
    def __game_cycle(self):
        self.game_dict = self.loader.load_game(self.difficulty)

        board = self.game_dict["board"]
        ball = self.game_dict["ball"]
        paddle_left = self.game_dict["paddle_left"]
        paddle_right = self.game_dict["paddle_right"]
        player_left = self.game_dict["player_left"]
        player_right = self.game_dict["player_right"]

        # Reset screen
        self.screen.fill((0,0,0))

        # Render board
        screen_cpy = self.screen.copy()
        board.render(screen_cpy) # board di render ke copy dari screen agar pas di loop lebih cepat
        pygame.display.flip()

        # Screen baru untuk game
        game_screen = pygame.Surface([1091,601], pygame.SRCALPHA, 32).convert_alpha()

        # game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "<exit>"

                # Check Keydown
                if event.type == pygame.KEYDOWN:
                    # Kontrol paddle kiri
                    if event.key == pygame.K_w:
                        paddle_left.go_up()
                    elif event.key == pygame.K_s:
                        paddle_left.go_down()

                    # Kontrol paddle kanan
                    if event.key == pygame.K_UP:
                        paddle_right.go_up()
                    elif event.key == pygame.K_DOWN:
                        paddle_right.go_down()

                # Check keyup
                if event.type == pygame.KEYUP:
                    # Kontrol paddle kiri
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        paddle_left.stop()
                        
                    # Kontrol paddle kiri
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        paddle_right.stop()

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
                    
            # Reset bola jika skor didapatkan
            if ball.rect.centerx < 0:
                ball = Ball(ball.image, 545, 300, (self.difficulty + 1)*2, 180)
                player_right.update_score()
                board.score_boxes[1].set_value(player_right.score)

            if ball.rect.centerx > 1096:
                ball = Ball(ball.image, 545, 300, (self.difficulty + 1)*2, 0)  
                player_right.update_score()
                board.score_boxes[1].set_value(player_right.score)

            # Cek utk menentukan pantulan bola
            ball.bounce_check(0, 601, paddle_left, paddle_right)

            self.screen.blit(game_screen, [board.x + 30, board.y + 30])
            pygame.display.update([board.x, 0, board.width + 55, 720])
            self.clock.tick(self.FPS)

            # Sementara exit setelah menang (Nanti diubah ketika halaman pemenang sudah dibuat)
            # if player_left.score >= self.max_score or player_right.score >= self.max_score:
            #     return "<exit>"


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
        pass
