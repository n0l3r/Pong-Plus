class Scores:
    def _init_(self, left:bool, board:Board, score_val = 0) -> None:
        # Posisi scorebox kiri atau kanan
        self.is_left = left

        # Board induknya
        self.cor_board = board
        self.width = 80
        self.height = 55

        # Cari posisi x dan y
        self.__set_pos()

        self.image = pygame.image.load("assets/game_board/Score box.png")
        # Scale image sesuai width x height
        self.image = pygame.transform.scale(self.image, [self.width, self.height])

        # Value dari isi scorebox
        self.__value = self.set_value( score_val )

    # Nentuin isi dari value
    def set_value(self, amount:int):
        return amount

    # Ngambil nilai value hasilnya string
    def get_value(self) -> str:
        if self.__value > 999:
            return "---"
        return str(self.__value)

    def render(self, screen):
        # Render scorebox
        screen.blit(self.image, [self.x, self.y])
        
        # Render score
        score_font = pygame.font.Font("assets/font/Montserrat-Regular.ttf", 32)
        score_text = score_font.render(self.get_value(), True, (255, 255, 255), None)
        
        # Render score ke tengah scorebox
        screen.blit(score_text, (
            self.x + (self.width - score_text.get_width())/2,
            self.y + (self.height - score_text.get_height())/2
            ))

    def __set_pos(self):
        self.y = 5
        # Nilai x dari tengah
        diff_x = 100
        if self.is_left:
            # Jika di kiri, nilai tengah dikurang jarak ke mid dan width scoreboxnya
            self.x = (1280/2) - diff_x - self.width
        else:
            # Jika di kiri, nilai tengah ditambah width scoreboxnya
            self.x = (1280/2) + diff_x

class Timer:
    def _init_(self, board:Board) -> None:
        # Isi dari text timer
        self.timer_time = "01:14"
        self.cor_board = board

    def render(self, screen):
        
        timer_font = pygame.font.Font("assets/font/Montserrat-Regular.ttf", 36)
        timer_text = timer_font.render(self.timer_time, True, (255, 255, 255), None)
        # Render ke tengah window
        screen.blit(timer_text, [ 640 - (timer_text.get_width()/2), 10 ] )