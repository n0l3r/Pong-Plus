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

        self.x = (1041 if side else 30)
        self.y = 240 - PADDLE_NEON
        self.speed = 0 # Kecepatan paddle

        self.board = board
        # Rect paddle
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    
    def go_up(self):
        self.speed = -5


    def go_down(self):
        self.speed = 5


    def stop(self):
        self.speed = 0


    def move(self):
        if self.rect.bottom >=  self.board.height and self.speed > 0:
            return
        
        if self.rect.top <= 0 and self.speed < 0:
            return

        self.y += self.speed
        self.rect.y = self.y


    # Render function
    def render(self, screen:pygame.surface.Surface):
        self.move()
        # pygame.draw.rect(screen, (255,0,0), self.rect) # for debugging
        screen.blit(self.image, [self.x -15, self.y -15])