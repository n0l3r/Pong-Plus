class Paddle:
    def __init__(self, image, side, length, pos_x, pos_y, speed):
        self.image = image
        self.side = side # 0 = kiri, 1 = kanan
        self.lenght = length
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed # Kecepatan gerak


    def move(self, down:bool):
        self.pos_y += (self.speed if down else -self.speed)


    def render(self):
        pass