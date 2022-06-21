# Board usage
# Note : '<>' = optional

# Class board
# Board()
# render( surface ) : render ke surface
#   -> width / height adalah area dalam board (inner board size) yang nanti
#      jadi acuan WALL COLLISION. (disatukan dalam list size[width, height])

# Class Scores
# Scores( is_left, corresponding_board, <score_value> ) : is_left menentukan score box kiri atau kanan
# set_value( amount ) : set value dari score box dimana aturan max = 99 dilakukan
# get_value() : get value -> str

# Class Time (*work in progress)
# Time(corresponding_board)
# *get_value() : get time -> str

import pygame

# Rasterized neon size = 15px
BOARD_NEON = 15

# Board
class Board:
    # Board aspect ratio = 16 : 9
    # Board : Screen_area ratio = 7 : 8
    default_width = 1120
    default_height = 630

    def __init__(self):

        #    -> img_width / img_heigth adalah size dari GAMBAR board (tanpa size neon).
        #    -> width / height adalah area dalam board (inner board size) yang nanti
        #       jadi acuan WALL COLLISION. (disatukan dalam list size[width, height])

        self.img_width = 1120
        self.img_height = 630
        self.x = 80 - BOARD_NEON
        self.y = 67 - BOARD_NEON
        self.image = pygame.image.load("assets/game_board/board_stars.png")
        self.image = pygame.transform.scale(self.image, [self.img_width + 2*BOARD_NEON, self.img_height + 2*BOARD_NEON])
        
        # Size board : 1091 x 601
        self.size = self.width,self.height = [ (self.img_width*549)/560 - 8, (self.img_height*304)/315 - 8]
        self.score_boxes = [Scores(True, self), Scores(False, self)]
        self.timer = Timer(self, pygame.time.get_ticks())

    
    def render(self, screen):
        # Board (self)
        screen.blit(self.image, [self.x,self.y]) 

        
    def score_render(self, screen):
        # Score boxes
        self.score_boxes[0].render(screen)
        self.score_boxes[1].render(screen)

        # Timer
        self.timer.render(screen)

# Score pada board
class Scores:
    def __init__(self, left:bool, board:Board, score_val = 0, win_width = 1280, win_height = 720) -> None:
        self.is_left = left
        self.cor_board = board
        self.width = (board.width*40) / 549
        self.height = (board.height*55)/608
        self.__set_pos(win_width,win_height)
        self.image = pygame.image.load("assets/game_board/score_box.png")
        # self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.__value = score_val


    def set_value(self, amount:int):
        self.__value = amount


    def get_value(self) -> str:
        if self.__value > 999:
            return "---"
        return str(self.__value)


    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])
        score_font = pygame.font.Font("assets/font/montserrat_regular.ttf", 32)
        score_text = score_font.render(self.get_value(), True, (255, 255, 255), None)
        screen.blit(score_text, (
            self.x + (self.width - score_text.get_width())/2,
            self.y + (self.height - score_text.get_height())/2
            ))


    def __set_pos(self, win_width = 1280, win_height = 720):
        self.y = win_height/126
        temp_x = (win_width * 5)/64
        if self.is_left:
            self.x = (win_width/2) - temp_x - self.width
        else:
            self.x = (win_width/2) + temp_x


# Timer (unfinished)
class Timer:
    def __init__(self, board:Board, start_time) -> None:
        self.start_time = start_time
        self.is_counting = False
        self.cor_board = board


    def render(self, screen):
        timer_font = pygame.font.Font("assets/font/montserrat_regular.ttf", 36)
        timer_text = timer_font.render(self.get_time(), True, (255, 255, 255), None)
        screen.blit(timer_text, (
            self.cor_board.image.get_rect().centerx + self.cor_board.x - (timer_text.get_width()/2),
            10
            ))


    def get_time(self):
        time_left = (300000 - (pygame.time.get_ticks() - self.start_time)) // 1000

        if time_left <= 0:
            return "00:00"

        time_str = str(time_left // 60) + ':' + str(time_left % 60)

        return time_str
