import pygame

# Neon pada image paddle
PADDLE_NEON = 15

class Paddle:
    def __init__(self, side:str, board:str, speed:int):
        self.image = pygame.image.load("assets/game_board/Paddle-Template.png")
        self.image = pygame.transform.scale(self.image,[50, 200])
        self.side = side # 0 = kiri, 1 = kanan
        self.width = 20
        self.height = 170
        if side == 0:
            self.x = 30
        else:
            self.x = 1041
        self.y = 240 - PADDLE_NEON
        self.base_speed = speed # Kecepatan gerak basis paddle (tergantung difficulty)
        self.speed = 0 # Kecepatan real paddle
        self.board = board
        # Rect paddle
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    # Move logic function
    def move(self):
        self.y += self.speed

        # Jika paddle berada pada ujung board, paddle tidak akan
        # terus berjalan kebawah
        self.rect.y = self.y
        if self.rect.bottom >=  self.board.height:
            self.rect.bottom =  self.board.height
            self.y = self.rect.top
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.y = self.rect.top

    # Render function
    def render(self, screen:pygame.surface.Surface):
        self.move()
        # pygame.draw.rect(screen, (255,0,0), self.rect) # for debugging
        screen.blit(self.image, [self.x -15, self.y -15])