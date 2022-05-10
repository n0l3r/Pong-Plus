class Player:
    def __init__ (self, side, score = 0):
        self.score = score
        self.side = side # 0 = kiri, 1 = kanan

    def update_score(self):
        self.score += 1
