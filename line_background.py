import pygame
from pygame.locals import *
import sys

def draw_circle(screen):
     pygame.draw.ellipse(screen,(249,37,0),(510,70,20,20))
     pygame.draw.ellipse(screen,(40,175,12),(190,70,20,20))
     pygame.draw.ellipse(screen,(25,22,135),(31,310,20,20))

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
    # draw_circle(screen)
    while(1):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
