from modules.Paddle import Paddle
from modules.GameObject import GameObject
import pygame
from math import atan, sin, cos, tan, radians, hypot

# Neon pada image ball
BALL_NEON = 20

class Ball(GameObject):
    def __init__(self, image:pygame.Surface, x, y, speed, angle) -> None:
        self.size = 50
        self.image = pygame.transform.scale(image, [self.size + BALL_NEON*2, self.size + BALL_NEON*2])

        super().__init__(pygame.rect.Rect(0, 0, self.size, self.size))

        self.speed_multiplier = 1
        self.speed = speed
        self.vec_x = speed*cos(radians(angle))
        self.vec_y = speed*sin(radians(angle))
        self.x = x - self.size/2
        self.y = y - self.size/2
        self.angle = 0


    def move(self):
        self.x += self.vec_x * self.speed_multiplier
        self.y += self.vec_y * self.speed_multiplier



    def bounce(self, with_paddle:bool, paddle:Paddle = None):
        if not with_paddle: # Jika bola collide dengan wall, bukan dengan paddle
            if self.check_modifier("striketrough"):
                self.y = 549 if self.vec_y < 0 else 1

            else:
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
                self.vec_x = (-1 if self.vec_x < 0 else 1)*self.speed*cos(max_angle)
                self.vec_y = (-1 if self.vec_y < 0 else 1)*self.speed*sin(max_angle)

            # Mereset kecepatan bola jika kecepatan berubah ketika memantul
            new_speed = hypot(self.vec_x, self.vec_y)
            self.vec_x *= self.speed/new_speed
            self.vec_y *= self.speed/new_speed

            while self.rect.colliderect(paddle.rect):
                self.move()


    def bounce_check(self, top_boundary, bottom_boundary, left_paddle, right_paddle):
        # Cek collision bola dengan tembok atas dan bawah
        if self.rect.top <= top_boundary or self.rect.bottom >= bottom_boundary:
            self.bounce(0)

        # Cek collision bola dengan paddle
        if self.rect.colliderect(left_paddle.rect):
            self.bounce(1, left_paddle)

        elif self.rect.colliderect(right_paddle.rect):
            self.bounce(1, right_paddle)

    
    # Mengatur aktifasi/deaktifasi efek PowerUp objek
    def handle_modifiers(self):
        current_time = pygame.time.get_ticks()//1000

        if self.check_modifier("speed_up"):
            if current_time > self.modifiers_timer["speed_up"]["end"]:
                self.speed_multiplier = 1
                self.remove_modifier("speed_up")

            elif self.speed_multiplier != 1.5:
                self.speed_multiplier = 1.5

        if self.check_modifier("striketrough"):
            if current_time > self.modifiers_timer["striketrough"]["end"]:
                self.remove_modifier("striketrough")


    def render(self, screen):
        self.angle += 0.05
        ball_img = pygame.transform.rotate(self.image, self.angle)
        screen.blit(ball_img, ((self.x - BALL_NEON), self.y - BALL_NEON))
        # pygame.draw.rect(screen, (255,0,0), self.rect, 1) # for debugging
        
