from modules.GameObject import GameObject
import pygame

# Neon pada image paddle
PADDLE_NEON = 15

class Paddle(GameObject):
    def __init__(self, side:bool, base_speed:int):
        self.image = pygame.image.load("assets/game_board/Paddle-Template.png")
        self.image = pygame.transform.scale(self.image,[50, 200])
        self.side = side # 0 = kiri, 1 = kanan
        self.width = 20
        self.height = 170

        # Rect paddle
        super().__init__(pygame.rect.Rect(0, 0, self.width, self.height))

        self.x = (1041 if side else 30)
        self.y = 240
        self.base_speed = base_speed
        self.speed = 0 # Kecepatan paddle

    
    def go_up(self):
        self.speed = -self.base_speed


    def go_down(self):
        self.speed = self.base_speed


    def stop(self):
        self.speed = 0


    def move(self, top_boundary, bottom_boundary):
        if self.rect.bottom >=  bottom_boundary and self.speed > 0:
            return
        
        if self.rect.top <= top_boundary and self.speed < 0:
            return

        self.y += self.speed

        if self.rect.bottom >  bottom_boundary:
            self.y -= self.rect.bottom - bottom_boundary
            return
        
        if self.rect.top < top_boundary:
            self.y -= self.rect.top - top_boundary
            return


    # Render function
    def render(self, screen:pygame.surface.Surface):
        # pygame.draw.rect(screen, (255,0,0), self.rect) # for debugging
        screen.blit(self.image, [self.x - PADDLE_NEON, self.y - PADDLE_NEON])