import pygame
from pygame.locals import *
import sys

def circle_position(screen, num, str): #選択する円の作成→交点
    # num1 = [2,3,10,9,8,7]
    if str == "x":
        x = 510
        black_x=[550]
        for i in range(12):
            for j in range(num[i]):
                black_x.append(x)
            x-=40
        return black_x

    else:
        black_y=[250]
        y = [230,210,70,90,110,130,110,90,70,210,230,250]
        for i in range(12):
            for j in range(num[i]):
                black_y.append(y[i])
                y[i]+=40
        return black_y

    # black_y = []
def draw_circle(screen):
     pygame.draw.ellipse(screen,(249,37,0),(430,70,20,20))
     pygame.draw.ellipse(screen,(40,175,12),(190,70,20,20))
     pygame.draw.ellipse(screen,(25,22,135),(71,250,20,20))

def circles(screen): #redのこま
    red_x = [430, 390, 430, 350, 390, 430, 310, 350, 390, 430]
    red_y = [71, 91, 111, 111, 131, 151, 131, 151, 171, 191]
    for num in range(10):
        pygame.draw.ellipse(screen,(249,37,0),(red_x[num],red_y[num],20,20))

def draw_line(screen):
    x = 440
    y = 80
    for count in range(9):
        pygame.draw.line(screen, (0,0,0), (x,y), (x, 520-y), 1) #右から左
        pygame.draw.line(screen, (0,0,0), (x+80,320-y), (x+80, 200+y), 1) #左から右
        pygame.draw.line(screen, (0,0,0), (x+120,y+180), (200, y*2-80), 1) #右上から左下
        pygame.draw.line(screen, (0,0,0), (440,560-y*2), (x-40, 500-y), 1) #右下から左上
        pygame.draw.line(screen, (0,0,0), (x-40,y+20), (440, y*2-40), 1) #右上から左下
        pygame.draw.line(screen, (0,0,0), (x+120,340-y), (200, 600-y*2), 1) #右下から左上
        x-=40
        y+=20

def background(screen):
    x = 0
    for count in range(120):
        pygame.draw.line(screen, (0,255,0), (x,0), (x, 800), 2) #右上から左下
        pygame.draw.line(screen, (0,255,0), (0,x), (1200, x), 2) #右上から左下
        x+=40

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("line")
    screen.fill((255,255,255))
    background(screen)
    draw_line(screen)
    num = [2,3,10,9,8,7,8,9,10,3,2,1]
    for count in range(73):
        pygame.draw.ellipse(screen,(255,255,255),(circle_position(screen, num, "x")[count],circle_position(screen, num, "y")[count],20,20))
        pygame.draw.ellipse(screen,(0,0,0),(circle_position(screen, num, "x")[count],circle_position(screen, num, "y")[count],20,20),1)
    # circles(screen)
    while(1):
        circles(screen)
        # red_x = [430, 390, 430, 350, 390, 430, 310, 350, 390, 430]
        # red_y = [71, 91, 111, 111, 131, 151, 131, 151, 171, 191]
        # red_y[9] = 231
        # for num in range(10):
        #     pygame.draw.ellipse(screen,(249,37,0),(red_x[num],red_y[num],20,20))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
