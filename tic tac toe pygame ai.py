import pygame
import time
from minimax.T_algorithm import minimax

pygame.init()

display_width = 600
display_height = 600

MIN,MAX = 1000,-1000

black = (0, 0, 0)
white = (255, 255, 255)
green = (5,255,5)
d_green = (50,255,50)
red = (255,5,5)
ai = None

turn = "X"
pos = 0
p_board = [' 'for k in range(9)]

display = pygame.display.set_mode((display_width,display_height+100))
clock = pygame.time.Clock()
play = True


display.fill(white)

def board():
    pygame.draw.rect(display,black,(0,0,10,600))
    pygame.draw.rect(display, black, (590, 0, 10, 600))
    pygame.draw.rect(display, black, (0, 0, 600, 10))
    for i in range (1,4):
        pygame.draw.rect(display,black,(int((display_width/3)*i),0,10,600))
        pygame.draw.rect(display, black, (0,int((display_width / 3) * i), 600, 10))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text,a,b,font):
    pygame.draw.rect(display, white, (0, 610, 600, 100))
    pygame.display.update()
    largetext = pygame.font.SysFont("comicsansms", font)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (a,b)
    display.blit(TextSurf, TextRect)
    pygame.display.update()
# 300 650
def insert_letter(letter, pos):
    p_board[pos] = letter
def play_again():
    global play, p_board,turn,possible_moves,ch
    display.fill(white)
    pygame.draw.rect(display, green, (100, 400, 130, 70))
    message_display('Play again', 165, 435,25)
    pygame.draw.rect(display, red, (370, 400, 130, 70))
    message_display('Quit', 435, 435, 25)
    message_display('PLAY AGAIN?',300,250,80)
    again = True
    while again:


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                press = pygame.mouse.get_pos()
                xi=press[0]
                yi=press[1]

                if xi>100 and xi<230 and yi>400 and yi<460:
                    p_board = [' 'for k in range(9)]
                    display.fill(white)
                    message_display("X's turn", 300, 650, 50)
                    pygame.display.update()
                    play = True
                    ch = True
                    possible_moves = []
                    turn = 'X'
                    again = False
                if xi>370 and xi<500 and yi>400 and yi<460:
                    pygame.quit()
                    quit()

def intro():
    into = True

    display.fill(white)
    message_display('Tic Tac Toe',300,200,90)
    pygame.display.update()
    pygame.draw.rect(display,green,(200,350,200,100))
    message_display('Start',300,395,50)
    pygame.display.update()
    while into:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x_ = pos[0]
                y_ = pos[1]
                if x_>200 and x_<400 and y_>350 and y_< 450:
                    display.fill(white)
                    pygame.display.update()
                    into = False

def choose_ai():
    global ai
    ch = True
    display.fill(white)
    pygame.draw.rect(display, green, (80, 400, 170, 70))
    message_display('AI(Computer)', 165, 435, 25)
    pygame.draw.rect(display, red, (370, 400, 130, 70))
    message_display('P vs P', 435, 435, 25)
    message_display('Who do you want to play against?', 300, 250, 35)
    while ch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                press = pygame.mouse.get_pos()
                xi = press[0]
                yi = press[1]

                if xi > 100 and xi < 230 and yi > 400 and yi < 460:
                    ai = True
                    display.fill(white)
                    ch = False
                if xi>370 and xi<500 and yi>400 and yi<460:
                    ai = False
                    display.fill(white)
                    ch = False

def dis_X(x,y):
    pygame.draw.line(display, black, (x,y), (x+160,y+160), 20)
    pygame.draw.line(display, black, (x, y+160), (x + 160, y), 20)

    pygame.display.update()

def dis_O(x,y):
    pygame.draw.circle(display,black,(x,y),80,20)
    pygame.display.update()

def check_if_free(pos):
    return p_board[pos] == ' '


def change_turn():
    global turn
    if turn == 'X':
        turn = "O"
        message_display("O's turn",300,650,50)

    elif turn == 'O':
        turn = 'X'
        message_display("X's turn",300,650,50)

def get_x_y(x,y):
    if turn == 'X':
        if x>0 and x<200:
            if y>0 and y<200:
                p_x =20
                p_y =20
                pos =0
            if y>200 and y<400:
                p_x =20
                p_y =220
                pos = 3
            if y>400 and y<600:
                p_x =20
                p_y =420
                pos = 6
        if x>200 and x<400:
            if y>0 and y<200:
                p_x =220
                p_y =20
                pos = 1
            if y>200 and y<400:
                p_x =220
                p_y =220
                pos = 4
            if y>400 and y<600:
                p_x =220
                p_y =420
                pos = 7
        if x>400 and x<600:
            if y>0 and y<200:
                p_x =420
                p_y =20
                pos = 2
            if y>200 and y<400:
                p_x =420
                p_y =220
                pos = 5
            if y>400 and y<600:
                p_x =420
                p_y =420
                pos = 8
        if check_if_free(pos):
            dis_X(p_x,p_y)
            p_board[pos]= 'X'
            change_turn()
        else:
            message_display('choose a valid slot',300,650,50)
    elif turn == 'O':
        if x > 0 and x < 200:
            if y > 0 and y < 200:
                p_x=100
                p_y=100
                pos = 0
            if y > 200 and y < 400:
                p_x=100
                p_y=300
                pos = 3
            if y > 400 and y < 600:
                p_x=100
                p_y=500
                pos = 6
        if x > 200 and x < 400:
            if y > 0 and y < 200:
                p_x=300
                p_y=100
                pos = 1
            if y > 200 and y < 400:
                p_x=300
                p_y=300
                pos = 4
            if y > 400 and y < 600:
                p_x=300
                p_y=500
                pos = 7
        if x > 400 and x < 600:
            if y > 0 and y < 200:
                p_x=500
                p_y=100
                pos = 2
            if y > 200 and y < 400:
                p_x=500
                p_y=300
                pos = 5
            if y > 400 and y < 600:
                p_x=500
                p_y=500
                pos = 8
        if check_if_free(pos):
            p_board[pos]='O'
            dis_O(p_x,p_y)
            change_turn()
    # change_turn(turn)
        else:
            message_display('choose a valid slot',300,650,50)

def is_winner(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or (bo[0] == le and bo[1] == le and bo[2] == le) or (bo[0] == le and bo[3] == le and bo[6] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[0] == le and bo[4] == le and bo[8] == le) or(bo[2] == le and bo[4] == le and bo[6] == le)

def is_winner2(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or (bo[0] == le and bo[1] == le and bo[2] == le) or (bo[0] == le and bo[3] == le and bo[6] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[0] == le and bo[4] == le and bo[8] == le) or(bo[2] == le and bo[4] == le and bo[6] == le)


def is_tie(p_board):
    if p_board.count (' ') >0:
        return False
    else:
        return True

def possible_moves():
    for l in range(0,9):
        if p_board[l] == ' ':
            return l

def ai_move(turn):
    if turn == 'O':
        if not (is_winner(p_board, 'X')):
            if not (is_tie(p_board)):
                move = comp_move()
                insert_letter('O', move)
                change_turn()
                print("Computer placed an 'O' in", move)
                if p_board[0] == 'O':
                    dis_O(100, 100)
                if p_board[1] == 'O':
                    dis_O(300, 100)
                if p_board[2] == 'O':
                    dis_O(500, 100)
                if p_board[3] == 'O':
                    dis_O(100, 300)
                if p_board[4] == 'O':
                    dis_O(300, 300)
                    pygame.display.update()
                if p_board[5] == 'O':
                    dis_O(500, 300)
                if p_board[6] == 'O':
                    dis_O(100, 500)
                if p_board[7] == 'O':
                    dis_O(300, 500)
                if p_board[8] == 'O':
                    dis_O(500, 500)
                pygame.display.update()

def comp_move():
    c_move = True
    if c_move:
        possible_moves = [l for l in range(0,9) if p_board[l] == ' ']
        for let in ['O', 'X']:
            for i in possible_moves:
                boardCopy = p_board[:]
                boardCopy[i] = let
                if is_winner(boardCopy, let):
                    move = i
                    return move

        corner_open = []
        if 4 in possible_moves:
            move = 4
            return move
        for i in possible_moves:
            if i in [0, 2, 6, 8]:
                corner_open.append(i)
        if len(corner_open) > 0:
            move = select_random(corner_open)
            return move

        if is_tie(p_board):
            c_move = False
        edge_open = []
        for i in possible_moves:
            if i in [1, 3, 5, 7]:
                edge_open.append(i)
        if len(edge_open) > 0:
            move = select_random(edge_open)
            # return move
        return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def game_loop():
    global play
    message_display("X's turn", 300, 650, 50)
    pygame.display.update()
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                get_x_y(x,y)
        if ai == True:
            ai_move(turn)

        if is_winner(p_board,'X'):
            print('X won!!!')
            message_display('X won!!',300,650,50)
            time.sleep(2)
            play_again()
            choose_ai()
        if is_winner(p_board,'O'):
            print('O won!!')
            message_display('O won!!',300,650,50)
            time.sleep(2)
            play_again()
            choose_ai()
        if is_tie(p_board):
            print('tie')
            message_display('Tie',300,650,50)
            time.sleep(2)
            play_again()
            choose_ai()

        board()
        pygame.display.update()
        clock.tick(60)


intro()
choose_ai()
game_loop()
pygame.quit()
quit()
