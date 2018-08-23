import pygame
from pygame.locals import *
import sys

def draw_line(screen):
    x = 520
    y = 80
    # pygame.draw.line(screen, (0,0,0), (x-160,y), (x-160, x), 1) #右から左
    for count in range(12):
        pygame.draw.line(screen, (0,0,0), (x,y), (x, 640-y), 1) #右から左
        pygame.draw.line(screen, (0,0,0), (x+120,380-y), (x+120, 260+y), 1) #左から右
        pygame.draw.line(screen, (0,0,0), (x+160,y+240), (200, y*2-80), 1) #右上から左下
        pygame.draw.line(screen, (0,0,0), (520,680-y*2), (x-40, 620-y), 1) #右下から左上
        pygame.draw.line(screen, (0,0,0), (x-40,y+20), (520, y*2-40), 1) #右上から左下
        pygame.draw.line(screen, (0,0,0), (x+160,400-y), (200, 720-y*2), 1) #右下から左上
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
    screen = pygame.display.set_mode((720, 640))
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
