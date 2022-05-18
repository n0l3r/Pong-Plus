from modules.Paddle import Paddle
from modules.GameObject import GameObject
import pygame
from math import atan, sin, cos, tan, radians, hypot

# Neon pada image ball
BALL_NEON = 15

class Ball(GameObject):
    def __init__(self, image:pygame.Surface, x, y, speed, angle) -> None:
        self.size = 50
        self.image = pygame.transform.scale(image, [self.size + 28, self.size + 28])

        super().__init__(pygame.rect.Rect(0, 0, self.size, self.size))

        self.speed = speed
        self.vec_x = speed*cos(radians(angle))
        self.vec_y = speed*sin(radians(angle))
        self.x = x - self.size/2
        self.y = y - self.size/2
        

    def move(self):
        self.x += self.vec_x
        self.y += self.vec_y


    def bounce(self, with_paddle:bool, paddle:Paddle = None):
        if not with_paddle: # Memantul dari batas atas atau bawah board
            self.vec_y *= -1
            self.move()
        
        else: # Arah pantulan bola bervariasi berdasarkan jarak bola dari titik tengah paddle
            height_diff = self.rect.centery - paddle.rect.centery

            if height_diff == 0:
                self.vec_x *= -1

                while self.rect.colliderect(paddle.rect):
                    self.move()

                return

            focal_point = 2*(-paddle.height if paddle.side else paddle.height)
            ref_angle = atan(focal_point/height_diff) # Sudut garis pantul (rad)

            self.vec_x = self.vec_x*cos(2*ref_angle) + self.vec_y*sin(2*ref_angle)
            self.vec_y = self.vec_x*sin(2*ref_angle) - self.vec_y*cos(2*ref_angle)

            slope = self.vec_y/self.vec_x # kemiringan lintasan bola
            max_angle = radians(60)

            # Membatasi sudut maksimal kemiringan lintasan bola
            if abs(slope) > tan(max_angle):
                self.vec_x = (-1 if paddle.side else 1)*self.speed*cos(max_angle)
                self.vec_y = (-1 if self.vec_y < 0 else 1)*self.speed*sin(max_angle)

            # Mereset kecepatan bola jika kecepatan berubah ketika memantul
            new_speed = hypot(self.vec_x, self.vec_y)
            self.vec_x *= self.speed/new_speed
            self.vec_y *= self.speed/new_speed

            while self.rect.colliderect(paddle.rect):
                self.move()


    def check_collision(self, top_boundary, bottom_boundary, left_paddle, right_paddle):
        # Cek collision bola dengan tembok atas dan bawah
        if self.rect.top <= top_boundary or self.rect.bottom >= bottom_boundary:
            self.bounce(0)

        # Cek collision bola dengan paddle
        if self.rect.colliderect(left_paddle.rect):
            self.bounce(1, left_paddle)
        elif self.rect.colliderect(right_paddle.rect):
            self.bounce(1, right_paddle)
        

    def render(self, screen):
        screen.blit(self.image, (self.x - BALL_NEON, self.y - BALL_NEON))
        #pygame.draw.rect(screen, (255,0,0), self.rect, 1) # for debugging
        
