import pygame
import main_mini
from pygame.locals import *
import sys
import pygame.gfxdraw


def background(screen):
    x = 0
    for count in range(120):
        pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, 800), 2)  # 右上から左下
        pygame.draw.line(screen, (0, 255, 0), (0, x), (1200, x), 2)  # 右上から左下
        x += 40


def draw_line(screen):  # 盤の目
    pygame.gfxdraw.filled_trigon(screen, 260, 100, 260, 260, 420, 180, (156, 167, 226))  # 青
    pygame.gfxdraw.filled_trigon(screen, 260, 420, 260, 580, 420, 500, (235, 121, 136))  # 赤
    pygame.gfxdraw.filled_trigon(screen, 580, 260, 580, 420, 740, 340, (0, 255, 0))  # 緑
    x = 580
    y = 80
    for count in range(7):
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x, 680 - y), 3)  # 右から左
        pygame.draw.line(screen, (0, 0, 0), (x + 160, 400 - y), (x + 160, 280 + y), 3)  # 左から右
        pygame.draw.line(screen, (0, 0, 0), (x + 160, y + 260), (260, y * 2 - 60), 3)  # 右上から左下
        pygame.draw.line(screen, (0, 0, 0), (580, 740 - y * 2), (x, 660 - y), 3)  # 右下から左上
        pygame.draw.line(screen, (0, 0, 0), (x, y + 20), (580, y * 2 - 60), 3)  # 右上から左下
        pygame.draw.line(screen, (0, 0, 0), (x + 160, 420 - y), (260, 740 - y * 2), 3)  # 右下から左上
        x -= 80
        y += 40


def direction(screen):  # 方向キー
    pygame.draw.rect(screen, (255, 0, 0), (800, 100, 60, 40), 0)  # 右上
    pygame.draw.rect(screen, (255, 0, 0), (800, 180, 60, 40), 0)  # 右下
    pygame.draw.rect(screen, (255, 0, 0), (680, 100, 60, 40), 0)  # 左上
    pygame.draw.rect(screen, (255, 0, 0), (680, 180, 60, 40), 0)  # 左下
    pygame.draw.rect(screen, (255, 0, 0), (750, 60, 40, 60), 0)  # 上
    pygame.draw.rect(screen, (255, 0, 0), (750, 200, 40, 60), 0)  # 下

    sysfont = pygame.font.SysFont(None, 40)
    text = sysfont.render("R&U", True, (255, 255, 255))
    screen.blit(text, (800, 100))
    text = sysfont.render("R&D", True, (255, 255, 255))
    screen.blit(text, (800, 180))
    text = sysfont.render("L&U", True, (255, 255, 255))
    screen.blit(text, (680, 100))
    text = sysfont.render("L&D", True, (255, 255, 255))
    screen.blit(text, (680, 180))
    text = sysfont.render("UP", True, (255, 255, 255))
    screen.blit(text, (750, 60))
    text = sysfont.render("DO", True, (255, 255, 255))
    screen.blit(text, (750, 200))


def color_change(color):
    colors = [0] * 37
    for i in range(37):
        c = color[i]
        if c == 0:
            colors[i] = (0, 0, 0)
        elif c == 1:
            colors[i] = (255, 0, 0)
        elif c == 2:
            colors[i] = (0, 0, 255)
        elif c == 3:
            colors[i] = (50, 204, 18)
    return colors


def draw_rects(screen, color):
    colors = color_change(color)
    num = [1, 2, 7, 6, 5, 6, 7, 2, 1]
    for count in range(37):  # 交点の四角
        pygame.draw.rect(screen, colors[count],
                         (rect_position()[count][0], rect_position()[count][1], 40, 40))


def decide_position(color, player):
    players_red = []
    players_blue = []
    players_green = []
    point = rect_position()
    num = [1, 2, 7, 6, 5, 6, 7, 2, 1]
    for i in range(37):
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


def mouseDownActionDirection(af_x, af_y, x, y):  # 遷移先のx,y座標を求める
    if (af_x > 800) and (af_x < 860):
        if (af_y > 100) and (af_y < 140):
            y -= 40
        elif (af_y > 180) and (af_y < 240):
            y += 40
        x += 80
    elif (af_x > 750) and (af_x < 790):
        if (af_y > 60) and (af_y < 120):
            y -= 80
        elif (af_y > 200) and (af_y < 260):
            y += 80
    elif (af_x > 680) and (af_x < 740):
        if (af_y > 100) and (af_y < 140):
            y -= 40
        elif (af_y > 180) and (af_y < 220):
            y += 40
        x -= 80
    return (x, y)


def rect_position():  # 選択する四角の作成→交点
    num = [1, 2, 7, 6, 5, 6, 7, 2, 1]
    point = [[0 for i in range(2)] for j in range(37)]
    count = 0
    x = 720
    y = [320, 280, 80, 120, 160, 120, 80, 280, 320]
    for i in range(9):
        for j in range(num[i]):
            point[count][0] = x
            point[count][1] = y[i]
            y[i] += 80
            count += 1
        x -= 80
    return point


def decide_color(x, y):  # 色がついている箇所が何番目の番号かを返す
    point = rect_position()
    for i in range(37):
        if point[i][0] == x and point[i][1] == y:
            return i


def win_check(screen,color):
    red_count = 0
    blue_count = 0
    green_count = 0
    red_win_color = [20, 25, 26, 31, 32, 33]
    blue_win_color = [16, 21, 22, 27, 28, 29]
    green_win_color = [0, 1, 2, 3, 4, 5]
    for i in range(6):
        if color[red_win_color[i]] == 1:
            red_count += 1
        if color[blue_win_color[i]] == 2:
            blue_count += 1
        if color[green_win_color[i]] == 2:
            green_count += 1
    if red_count == 6:
        print("赤の勝利")
        result(screen,"RED")
    elif blue_count == 6:
        print("青の勝利")
        result(screen,"BLUE")
    elif green_count == 6:
        print("緑の勝利")
        result(screen,"GREEN")

def result(screen,color):
    screen.fill((255, 255, 255))
    sysfont = pygame.font.SysFont(None, 120)
    text = sysfont.render("Winner"+color, True, (0,0,0))
    screen.blit(text, (200, 200))
    pygame.draw.rect(screen, (0,0,0),(250,600, 160, 60),5)
    sysfont2 = pygame.font.SysFont(None, 60)
    end = sysfont2.render("END", True, (255,0,255))
    screen.blit(end, (290,610))
    pygame.draw.rect(screen, (0,0,0),(450,600, 160, 60),5)
    again = sysfont2.render("AGAIN", True, (0,0,255))
    screen.blit(again, (460,610))

    while (1):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                if (y > 600) and (y < 660):
                    if (x > 250) and (x < 410):
                        sys.exit()
                    elif (x > 450) and (x < 610):
                        main_mini.main()
