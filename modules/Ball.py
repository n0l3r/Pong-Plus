from modules.Paddle import Paddle
import pygame
from math import atan, sin, cos


class Ball():
    def __init__(self, image:pygame.Surface, vec_x, vec_y, pos_x, pos_y) -> None:
        self.image = image
        self.size = 50
        self.vec_x = vec_x
        self.vec_y = vec_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = pygame.rect.Rect(self.pos_x, self.pos_y, self.size, self.size)
        self.image = pygame.transform.scale(image, [self.size + 15, self.size + 15])

    def move(self):
        self.pos_x += self.vec_x
        self.pos_y += self.vec_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


    def bounce(self, with_paddle:bool, paddle:Paddle = None):
        if not with_paddle: # Memantul dari batas atas atau bawah board
            self.vec_y *= -1
        
        else: # Arah pantulan bola bervariasi berdasarkan jarak bola dari titik tengah paddle
            # focal_point = 2*(paddle.height if paddle.side else -paddle.height)
            # height_diff = self.rect.centery - paddle.rect.centery

            # if height_diff == 0:
            self.vec_x *= -1
                #return

            # angle = atan(focal_point/height_diff)

            # self.vec_x = self.vec_x*cos(2*angle) + self.vec_y*sin(2*angle)
            # self.vec_y = self.vec_x*sin(2*angle) - self.vec_y*cos(2*angle)
        

    def render(self, screen):
        screen.blit(self.image, (self.pos_x - 15, self.pos_y - 15))
        # pygame.draw.rect(screen, (255,0,0), self.rect, 1) # for debugging
