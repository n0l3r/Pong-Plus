from modules.Paddle import Paddle
import pygame
from math import atan, sin, cos, sqrt


class Ball():
    def __init__(self, image:pygame.Surface, vec_x, vec_y, x, y) -> None:
        self.image = image
        self.size = 50
        self.vec_x = vec_x
        self.vec_y = vec_y
        self.x = x - self.size/2
        self.y = y - self.size/2
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
        self.image = pygame.transform.scale(image, [self.size + 28, self.size + 28])

    def move(self):
        self.x += self.vec_x
        self.y += self.vec_y
        self.rect.x = self.x
        self.rect.y = self.y


    def bounce(self, with_paddle:bool, paddle:Paddle = None):
        if not with_paddle: # Memantul dari batas atas atau bawah board
            self.vec_y *= -1
        
        else: # Arah pantulan bola bervariasi berdasarkan jarak bola dari titik tengah paddle
            speed = sqrt(self.vec_x**2 + self.vec_y**2)

            focal_point = 2*(paddle.height if paddle.side else -paddle.height)
            height_diff = self.rect.centery - paddle.rect.centery

            if height_diff == 0:
                self.vec_x *= -1
                return

            angle = atan(focal_point/height_diff) # Sudut bidang pantul

            self.vec_x = self.vec_x*cos(2*angle) + self.vec_y*sin(2*angle)
            self.vec_y = self.vec_x*sin(2*angle) - self.vec_y*cos(2*angle)

            v_angle = self.vec_y/self.vec_x # nilai tan vektor akhir bola

            # Jika v_angle lebih besar dari 1.7 (tan(60 derajat)) maka sudut vektor diubah menjadi 60
            # untuk mencegah sudut bola menjadi vertikal
            if v_angle > 1.7 or v_angle < -1.7:
                v_angle = 1.7
                new_angle = atan(v_angle)

                self.vec_x = (-1 if paddle.side == 1 else 1)*speed*cos(new_angle)
                self.vec_y = (-1 if self.vec_y < 0 else 1)*speed*sin(new_angle)

            self.move()
        

    def render(self, screen):
        screen.blit(self.image, (self.x - 15, self.y - 15))
        pygame.draw.rect(screen, (255,0,0), self.rect, 1) # for debugging
