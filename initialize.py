import pygame
from pygame.locals import *
import sys
import pygame.gfxdraw


def rects(screen, x, y, color):  # 各色のこま
    for num in range(10):
        pygame.draw.rect(screen, color, (x[num] - 10, y[num] - 10, 20, 20))


def rect_position():  # 選択する四角の作成→交点
    num = [1, 2, 3, 10, 9, 8, 7, 8, 9, 10, 3, 2, 1]
    point = [[0 for i in range(2)] for j in range(73)]
    count = 0
    x = 550
    y = [250, 230, 210, 70, 90, 110, 130, 110, 90, 70, 210, 230, 250]
    for i in range(13):
        for j in range(num[i]):
            point[count][0] = x
            point[count][1] = y[i]
            y[i] += 40
            count += 1
        x -= 40
    return point


def color_change(color):
    colors = [0] * 73
    for i in range(73):
        c = color[i]
        if c == 0:
            colors[i] = (0, 0, 0)
        elif c == 1:
            colors[i] = (255, 0, 0)
        elif c == 2:
            colors[i] = (0, 0, 255)
        elif c == 3:
            colors[i] = (0, 255, 0)
    return colors


def draw_rects(screen, color):
    colors = color_change(color)
    num = [1, 2, 3, 10, 9, 8, 7, 8, 9, 10, 3, 2, 1]
    for count in range(73):  # 交点の四角
        pygame.draw.rect(screen, colors[count],
                         (rect_position()[count][0], rect_position()[count][1], 20, 20))


def decide_position(color, player):
    players_red = []
    players_blue = []
    players_green = []
    point = rect_position()
    num = [1, 2, 3, 10, 9, 8, 7, 8, 9, 10, 3, 2, 1]
    for i in range(73):
        if color[i] == 1:
            players_red.append(point[i])
        elif color[i] == 2:
            players_blue.append(point[i])
        elif color[i] == 3:
            players_green.append(point[i])
    if player == 1:
        return players_red
    elif player == 2:
        return players_blue
    elif player == 3:
        return players_green


def draw_line(screen):  # 盤の目
    pygame.gfxdraw.filled_trigon(screen, 200, 80, 320, 140, 200, 200, (156, 167, 226)) #青
    pygame.gfxdraw.filled_trigon(screen, 200, 320, 200, 440, 320, 380, (235, 121, 136)) #赤
    # pygame.gfxdraw.filled_trigon(screen, 200, 320, 200, 440, 320, 380, (235, 121, 136)) #緑
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
        x += 40

def direction(screen):  # 方向キー
    pygame.draw.rect(screen, (255, 0, 0), (580, 140, 40, 20), 0)  # 右上
    pygame.draw.rect(screen, (255, 0, 0), (580, 180, 40, 20), 0)  # 右下
    pygame.draw.rect(screen, (255, 0, 0), (500, 140, 40, 20), 0)  # 左上
    pygame.draw.rect(screen, (255, 0, 0), (500, 180, 40, 20), 0)  # 左下
    pygame.draw.rect(screen, (255, 0, 0), (550, 100, 20, 40), 0)  # 上
    pygame.draw.rect(screen, (255, 0, 0), (550, 200, 20, 40), 0)  # 下

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


def mouseDownActionDirection(af_x, af_y, x, y):  # 遷移先のx,y座標を求める
    if (af_x > 580) and (af_x < 620):
        if (af_y > 140) and (af_y < 160):
            # print("R&U")
            y -= 20
        elif (af_y > 180) and (af_y < 220):
            # print("R&D")
            y += 20
        x += 40
    elif (af_x > 550) and (af_x < 570):
        if (af_y > 100) and (af_y < 140):
            # print("UP")
            y -= 40
        elif (af_y > 200) and (af_y < 240):
            # print("DOWN")
            y += 40
        # x -= 20
    elif (af_x > 500) and (af_x < 540):
        if (af_y > 140) and (af_y < 160):
            # print("L&U")
            y -= 20
        elif (af_y > 180) and (af_y < 220):
            # print("L&D")
            y += 20
        x -= 40
    return (x, y)


def decide_color(x, y): #色がついている箇所が何番目の番号かを返す
    point = rect_position()
    for i in range(73):
        if point[i][0] == x and point[i][1] == y:
            return i

def win_check(color):
    red_count = 0
    blue_count = 0
    red_win_color = [40, 47, 48, 55, 56, 57, 64, 65, 66, 67]
    blue_win_color = [34, 41, 42, 49, 50, 51, 58, 59, 60, 61]
    for i in range(10):
        if color[red_win_color[i]] == 1:
            red_count += 1
        if color[blue_win_color[i]] == 2:
            blue_count += 1
        #新しいウィンドウを出して表示する
    if red_count == 10:
        print("赤の勝利")
    elif blue_count == 10:
        print("青の勝利")
