import pygame, sys
from src.settings import *
from src.utils import *
from src.model import *


class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.clock = pygame.time.Clock()
        self.board = [' ' for x in range(10)]
        self.first_move_to_you = None
        self.user_made_move = False
        self.init()

    def init(self):
        pygame.init()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                #self.playing_update()
                #self.playing_draw()
            elif self.state == 'game over':
                pass
                #self.game_over_win_events()
                #self.game_over_update()
                #self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    # Start functions
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            self.first_move_to_you = True
            self.state = 'playing'
        elif keys[pygame.K_p]:
            self.first_move_to_you = False
            self.state = 'playing'
            self.user_made_move = True

    def start_draw(self):
        self.screen.fill(WHITE)
        self.background = pygame.image.load("../media/modified_cover.png")
        self.x_img = pygame.image.load("../media/X_modified.png")
        self.y_img = pygame.image.load("../media/o_modified.png")
        # resizing images
        self.background = pygame.transform.scale(self.background, (200, 200))
        self.screen.blit(self.background, (WIDTH // 4, HEIGHT // 8 + 30))
        self.x_img = pygame.transform.scale(self.x_img, (80, 80))
        self.o_img = pygame.transform.scale(self.y_img, (80, 80))
        Utils.draw_text('Who is gonna do the first move?', self.screen, (WIDTH // 2, HEIGHT // 2 + 130), START_TEXT_SIZE, OCHER,
                        START_FONT, True)
        Utils.draw_text('Press Y for you, P for pc', self.screen, (WIDTH // 2, HEIGHT // 2 + 160), START_TEXT_SIZE, LIGHT_BLUE,
                        START_FONT, True)
        pygame.display.update()

    # Playing functions
    def playing_events(self):
        if self.board.count(' ')==len(self.board):
            self.draw_board()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         self.running = False
        #     else:
        if self.first_move_to_you:
            self.user_move()
            self.pc_move()
            # self.win_check()
        elif not self.first_move_to_you:
            self.pc_move()
            # self.win_check()
            self.user_move()


    def draw_board(self):
        # time.sleep(3)
        self.screen.fill(WHITE)
        # drawing vertical lines
        pygame.draw.line(self.screen, line_color, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
        pygame.draw.line(self.screen, line_color, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)

        # drawing horizontal lines
        pygame.draw.line(self.screen, line_color, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
        pygame.draw.line(self.screen, line_color, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
        pygame.display.update()
        # draw_status()

    def user_move(self):
        for event in pygame.event.get():
            if event.type is MOUSEBUTTONDOWN:
                # get coordinates of mouse click
                x, y = pygame.mouse.get_pos()
                if (x < WIDTH / 3) and (y < HEIGHT / 3):
                    pos = 1
                elif (x < WIDTH / 3 * 2) and (y < HEIGHT / 3):
                    pos = 2
                elif (x < WIDTH) and (y < HEIGHT / 3):
                    pos = 3
                elif (x < WIDTH / 3) and (y < HEIGHT / 3 * 2):
                    pos = 4
                elif (x < WIDTH / 3 * 2) and (y < HEIGHT / 3 * 2):
                    pos = 5
                elif (x < WIDTH) and (y < HEIGHT / 3 * 2):
                    pos = 6
                elif (x < WIDTH / 3) and (y < HEIGHT):
                    pos = 7
                elif (x < WIDTH / 3 * 2) and (y < HEIGHT):
                    pos = 8
                elif (x < WIDTH) and (y < HEIGHT):
                    pos = 9
                else:
                    pos = None
                if 1 <= pos <= 9:
                    self.board = updateBoard('X', pos, self.board)
                    print('You placed an \'X\' in position', pos, ':')
                    self.playing_draw(pos,'X')
                    self.win_check()
                    self.user_made_move = True

    def win_check(self):
        if isBoardFull(self.board):
            print('Tie Game!')
            self.state = 'game over'
        else:
            # if pc is the winner
            if isWinner(self.board, 'O'):
                print('Sorry, PC won this time!')
                self.state = 'game over'
            # if player is the winner
            elif isWinner(self.board, 'X'):
                print('You won this time! Good Job!')
                self.state = 'game over'

    def pc_move(self):
        if self.user_made_move:
            # pc makes move
            move = pcMove(self.board)
            self.playing_draw(move, 'O')
            self.user_made_move = False
            if move == 0:
                print('Tie Game!')
                self.state = 'game over'
            else:
                self.board = updateBoard('O', move, self.board)
                print('Computer placed an \'O\' in position', move, ':')
                self.win_check()
                # printBoard(board)

    def playing_draw(self,index,letter):
        if index == 1:
            posx, posy = 30, 30
        elif index == 2:
            posx, posy = WIDTH / 3 + 30, 30
        elif index == 3:
            posx, posy = WIDTH / 3 * 2.2, 30
        elif index == 4:
            posx, posy = 30, HEIGHT / 3 + 30
        elif index == 5:
            posx, posy = WIDTH / 3 + 30, HEIGHT / 3 + 30
        elif index == 6:
            posx, posy = WIDTH / 3 * 2.2, HEIGHT / 3 + 30
        elif index == 7:
            posx, posy = 30, HEIGHT / 3 * 2 + 30
        elif index == 8:
            posx, posy = WIDTH / 3 + 30, HEIGHT / 3 * 2 + 30
        elif index == 9:
            posx, posy = WIDTH / 3 * 2.2, HEIGHT / 3 * 2 + 30
        if letter == 'X':
            self.screen.blit(self.x_img, (posx, posy))
        elif letter == 'O':
            self.screen.blit(self.o_img, (posx, posy))
        pygame.display.update()
