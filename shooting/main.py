import pygame
import random

pygame.init()

black = (0,0,0)
dis_x = 800
dis_y = 750
b_pos = [0]
b_pos_y = [0]

player_width = 64
x=(dis_x/2) - (player_width/2)
y=(dis_y*0.94)


yel = (255,255,255)

display = pygame.display.set_mode((dis_x,dis_y))
pygame.display.set_caption('shooter')

playerimg = pygame.image.load('player1.png')
enemyimg = pygame.image.load('enemy1.png')



clock = pygame.time.Clock()

def player(x,y):
    display.blit(playerimg,(x,y))

def enemy(ene_x, ene_y):
    display.blit(enemyimg,(ene_x,ene_y))

def bullet(bullet_x,bullet_y,bullet_w,bullet_h):
    pygame.draw.rect(display,yel,(bullet_x,bullet_y,bullet_w,bullet_h))

# def p_shoot(playerx,sy):
#     pygame.draw.rect(display,yel,(playerx,sy,10,30))


def play_game():
    x= int((dis_x/2) - (player_width/2))
    y= int((dis_y*0.94))
    x_change = 0


    e_x =random.randrange(0, dis_x)
    e_y = 10
    e_speed = 1

    
    b_speed = 2
    b2start = random.randrange(150, 400)
    by = b2start
    bw = 10
    bh = 30

    ps_speed = 2
    ps_y = -100
    no_bullet = 0


    game_exit = False
    while game_exit == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_UP:
                    no_bullet += 1
                    # for i in range (0,no_bullet):
                    ps_x = x+player_width/2
                    ps_y = 650
                    b_pos_y.append(ps_y)
                    b_pos.append(ps_x)
                        # pygame.draw.rect(display, yel, (x, ps_y, 10, 30))


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0


        x += x_change
        display.fill(black)
        player(x, y)
        enemy(e_x,e_y)
        e_y += e_speed

        if ps_y>=0:
            # for z in range(0,no_bullet):

                ps_y-=ps_speed
                # b_pos.append([ps_x, ps_y])
                # b_pos[no_bullet] = ps_y
                b_pos_y.pop(no_bullet)
                b_pos_y.insert(no_bullet,ps_y)
                pygame.draw.rect(display,yel,(b_pos[no_bullet],b_pos_y[no_bullet],10,30))
                # print(b_pos)
        if e_y > dis_y :
            e_y = 0 - 40
            e_x = random.randrange(0, dis_x)
            b2start = random.randrange(150, 400)
            by = b2start

        if e_y >= b2start :
            bx= e_x+20-5
            bullet(bx,by,bw,bh)
            by += b_speed

        if x>dis_x-player_width or x<0:
            quit()
        pygame.display.update()
        clock.tick(90)

play_game()
