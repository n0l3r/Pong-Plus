from modules.Paddle import Paddle
import math


class Ball():
    def __init__(self, image, size, vec_x, vec_y, pos_x, pos_y) -> None:
        self.image= image
        self.size = size
        self.vec_x = vec_x
        self.vec_y = vec_y
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    
    def move(self):
        self.pos_x += self.vec_x
        self.pos_y += self.vec_y


    def bounce(self, with_paddle:bool, paddle:Paddle = None):
        if not with_paddle: # Memantul dari batas atas atau bawah board
            self.vec_y *= -1
        
        else: # Arah pantulan bola bervariasi berdasarkan jarak bola dari titik tengah paddle
            focal_point = 200 if paddle.side else -200
            height_diff = (self.pos_y + self.size)/2 - (paddle.pos_y + paddle.length)/2
            angle = math.atan(focal_point/height_diff)

            self.vec_x = self.vec_x*math.cos(2*angle) + self.vec_y*math.sin(2*angle)
            self.vec_y = self.vec_x*math.sin(2*angle) - self.vec_y*math.cos(2*angle)
        

    def render(self):
        pass
