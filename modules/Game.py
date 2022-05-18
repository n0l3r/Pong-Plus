import pygame, sys
from modules import Menu
from modules.Paddle import Paddle
from modules.Ball import Ball
from modules.Player import Player
from modules import Loader as L
from modules import Board as B


class Game:
    def __init__(self, screen:pygame.Surface, clock:pygame.time.Clock) -> None:
        self.screen = screen
        self.clock = clock
        self.FPS = 120
        self.loader = L.Loader()
        self.is_playing = False
        self.difficulty = 0
        self.is_paused = False

    def play(self):
        if not self.is_playing:
            # Load Menu
            if not self.loader.menu_assets_loaded:
                self.menu_dict = self.loader.load_menu()

            # Call main menu loop
            self.__main_menu()

        elif self.is_playing:
            # Load Game
            self.__game_cycle()


    def __game_cycle(self):

        # Main game Flow


        board = B.Board()
        game_area = [1091,601]
        # Board screen
        # gameScreen = pygame.Surface([1091,601])
        gameScreen = pygame.Surface([1091,601], pygame.SRCALPHA)
        gameScreen = gameScreen.convert_alpha()

        # Paddles kanan dan kiri
        paddles = [paddle_left, paddle_right] = [Paddle(0, board, 7), Paddle(1, board, 7)]
        
        # Ball
        ball_img = pygame.image.load("assets/game_board/Ball-Reacr.png")
        ball = Ball(ball_img, self.difficulty*2 + 5, 0, 545, 300)

        # Player
        player_1 = Player(0) # Player at left
        player_2 = Player(1) # Player at Right

        self.screen.fill((0,0,0))
        gameScreen.fill((0,0,0,0))
        board.render(self.screen)
        board.score_render(self.screen)

        while True:
            # Cek collision bola dengan tembok kiri
            if ball.rect.left <= 0:
                ball.x = 545
                ball.y = 300
                ball.vec_x = -(self.difficulty*2 + 15)
                ball.vec_y = 0

                # Tambahan skor untuk player
                player_2.update_score()
                board.score_boxes[1].set_value(player_2.score)
                board.score_render(self.screen)
            
            # Cek collision bola dengan tembok kanan
            elif ball.rect.right >= 1096:
                ball.x = 545
                ball.y = 300
                ball.vec_x = (self.difficulty*2 + 15)
                ball.vec_y = 0

                # Tambahan skor untuk player
                player_1.update_score()
                board.score_boxes[0].set_value(player_1.score)
                board.score_render(self.screen)

            # Cek collision bola dengan tembok atas dan bawah
            if ball.rect.top <= 0 or ball.rect.bottom >= 601:
                ball.bounce(0)

            # Cek collision bola dengan paddle
            if ball.rect.colliderect(paddle_left.rect):
                ball.bounce(1, paddle_left)
            elif ball.rect.colliderect(paddle_right.rect):
                ball.bounce(1, paddle_right)

            for i in paddles:
                i.move()
                i.move()
            ball.move()

            self.screen.fill((0,0,0))
            gameScreen.fill((0,0,0,0))
            board.render(self.screen)
            board.score_render(self.screen)
            ball.render(gameScreen)
            for i in paddles:
                i.render(gameScreen) 
            self.screen.blit(gameScreen, [board.x + 30, board.y + 30])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                    if event.key == pygame.K_w:
                        paddle_left.stop()
                    elif event.key == pygame.K_s:
                        paddle_left.stop()
                        
                    # Kontrol paddle kiri
                    if event.key == pygame.K_UP:
                        paddle_right.stop()
                    elif event.key == pygame.K_DOWN:
                        paddle_right.stop()
                        
            if self.is_paused:
                self.__pause_cycle
            pygame.display.update()
            self.clock.tick(self.FPS)

    def __pause_cycle(self):

        # Paused Flow
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        self.clock.tick(self.FPS)

    def __main_menu(self):
        # Default menu
        page_menu = "main_menu"

        # Render menu
        while not self.is_playing:
            self.menu_dict[page_menu].render(self.screen)
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Menu button clicks
                    page_menu = Menu.change_menu(self.menu_dict, page_menu, self.screen)
                    print(page_menu)
                    # Load selected menu
                    if page_menu == "<exit>": 
                        pygame.quit()
                        sys.exit()
                    elif page_menu == "<in-game>":
                        self.is_playing = True
                        self.difficulty = self.menu_dict['play_menu'].difficulty
                        break
            if page_menu == "<in-game>":
                break

            pygame.display.update()
            self.clock.tick(self.FPS)
