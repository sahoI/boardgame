import pygame
from pygame.locals import *
import sys

def draw_line(screen):
    x = 240
    y = 0
    count = 0
    pygame.draw.line(screen, (0,0,0), (x-160,y), (x-160, x), 1) #右から左
    for count in range(12):
        pygame.draw.line(screen, (0,0,0), (x,y), (x, (y+240)-y*2), 1) #右から左
        pygame.draw.line(screen, (0,0,0), (x+80,y+120), (x+80, (y+120)-y*2), 1) #左から右
        pygame.draw.line(screen, (0,0,0), (240,x-20), (x-20, 230-y), 1) #左上から右下
        pygame.draw.line(screen, (0,0,0), (x,y), (x, 240-y), 1) #右上から左下
        pygame.draw.line(screen, (0,0,0), (x+80,120-y), (80, 240-y*2), 1) #左上から右下
        pygame.draw.line(screen, (0,0,0), (x+80,120+y), (80, 240-x), 1) #右下から左上
        pygame.draw.line(screen, (0,0,0), (240,x), (240-x, 120-y), 1) #左下から右上
        x-=20
        y+=10

def background(screen):
    x = 0
    for count in range(60):
        pygame.draw.line(screen, (0,255,0), (x,0), (x, 400), 2) #右上から左下
        pygame.draw.line(screen, (0,255,0), (0,x), (600, x), 2) #右上から左下
        x+=20

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("line")
    screen.fill((255,255,255))
    background(screen)
    draw_line(screen)
    while(1):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
