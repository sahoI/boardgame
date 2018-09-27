import pygame
from pygame.locals import *
import sys


def rects(screen, x, y, color):  # 各色のこま
    for num in range(10):
        pygame.draw.rect(screen, color, (x[num] - 10, y[num] - 10, 20, 20))


def draw_line(screen):  # 盤の目
    x = 440
    y = 80
    for count in range(9):
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x, 520 - y), 1)  # 右から左
        pygame.draw.line(screen, (0, 0, 0), (x + 80, 320 - y), (x + 80, 200 + y), 1)  # 左から右
        pygame.draw.line(screen, (0, 0, 0), (x + 120, y + 180), (200, y * 2 - 80), 1)  # 右上から左下
        pygame.draw.line(screen, (0, 0, 0), (440, 560 - y * 2), (x - 40, 500 - y), 1)  # 右下から左上
        pygame.draw.line(screen, (0, 0, 0), (x - 40, y + 20), (440, y * 2 - 40), 1)  # 右上から左下
        pygame.draw.line(screen, (0, 0, 0), (x + 120, 340 - y), (200, 600 - y * 2), 1)  # 右下から左上
        x -= 40
        y += 20

def background(screen):
    x = 0
    for count in range(120):
        pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, 800), 2)  # 右上から左下
        pygame.draw.line(screen, (0, 255, 0), (0, x), (1200, x), 2)  # 右上から左下
        x += 10

def direction(screen): #方向キー
    pygame.draw.rect(screen, (255,0,0), (580, 140, 40, 20), 0) #右上
    pygame.draw.rect(screen, (255,0,0), (580, 180, 40, 20), 0) #右下
    pygame.draw.rect(screen, (255,0,0), (500, 140, 40, 20), 0) #左上
    pygame.draw.rect(screen, (255,0,0), (500, 180, 40, 20), 0) #左下
    pygame.draw.rect(screen, (255,0,0), (550, 100, 20, 40), 0) #上
    pygame.draw.rect(screen, (255,0,0), (550, 200, 20, 40), 0) #下

    sysfont = pygame.font.SysFont(None, 20)
    text = sysfont.render("R&U", True, (255, 255, 255))
    screen.blit(text, (580, 145))
    text = sysfont.render("R&D", True, (255, 255, 255))
    screen.blit(text, (580, 185))
    text = sysfont.render("L&U", True, (255, 255, 255))
    screen.blit(text, (500, 145))
    text = sysfont.render("L&D", True, (255, 255, 255))
    screen.blit(text, (500, 185))
    text = sysfont.render("UP", True, (255, 255, 255))
    screen.blit(text, (550, 105))
    text = sysfont.render("D", True, (255, 255, 255))
    screen.blit(text, (550, 205))

def mouseDownActionDirection(af_x, af_y,x, y,type): #遷移先のx,y座標を求める
    if (type == "typeX"):
        print("x")
        if (af_x > 580)and (af_x < 620):
            if(af_y > 140) and (af_y < 160):
                print("R&U")
            elif(af_y > 180) and (af_y < 220):
                print("R&D")
            x += 20
        elif (af_x > 550) and (af_x < 570):
            if (af_y > 100) and (af_y < 140):
                print("UP")
            elif (af_y > 200) and (af_y < 240):
                print("DOWN")
            x -= 20
        elif (af_x > 500) and (af_x < 540):
            if(af_y > 140) and (af_y < 160):
                print("L&U")
            elif(af_y > 180) and (af_y < 220):
                print("L&D")
            x -= 60
        return x
    else:
        print("y")
        if (af_x > 580)and (af_x < 620):
            if(af_y > 140) and (af_y < 160):
                print("R&U")
                y -= 20
            elif(af_y > 180) and (af_y < 220):
                print("R&D")
                y += 20
        elif (af_x > 550) and (af_x < 570):
            if (af_y > 100) and (af_y < 140):
                print("UP")
                y -= 40
            elif (af_y > 200) and (af_y < 240):
                print("DOWN")
                y += 40
        elif (af_x > 500) and (af_x < 540):
            if(af_y > 140) and (af_y < 160):
                print("L&U")
                y -= 20
            elif(af_y > 180) and (af_y < 220):
                print("L&D")
                y += 20
        return y
