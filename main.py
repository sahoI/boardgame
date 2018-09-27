import pygame
import initialize
from pygame.locals import *
import sys


def rect_position(screen, num, str):  # 選択する四角の作成→交点
    # num1 = [2,3,10,9,8,7,8,9,10,3,2,1]
    if str == "x":
        x = 510
        black_x = [550]
        for i in range(12):
            for j in range(num[i]):
                black_x.append(x)
            x -= 40
        return black_x

    else:
        black_y = [250]
        y = [230, 210, 70, 90, 110, 130, 110, 90, 70, 210, 230, 250]
        for i in range(12):
            for j in range(num[i]):
                black_y.append(y[i])
                y[i] += 40
        return black_y


# 文字の色を引数にしてコマの出力を一つのメソッドで書けそう
# x,y座標の順番を一定にすればfor文で配列を作れそうor引数にx,y座標の配列を挿入する

def click_process(x, y, red_x, red_y):
    if x > 420 or x < 460 and y > 60 or y < 100:
        # pygame.draw.rect(screen,(255,255,0),(red_x[3]-10,red_y[3]-10,20,20))
        x = 430
        y = 120
    return x


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("ダイヤモンドゲーム")
    screen.fill((255, 255, 255))
    initialize.background(screen)  # 背景
    initialize.draw_line(screen)  # 盤の目
    initialize.direction(screen)

    num = [2, 3, 10, 9, 8, 7, 8, 9, 10, 3, 2, 1]
    for count in range(73):  # 交点の円
        pygame.draw.rect(screen, (255, 255, 255),
                         (rect_position(screen, num, "x")[count], rect_position(screen, num, "y")[count], 20, 20))
        pygame.draw.rect(screen, (0, 0, 0),
                         (rect_position(screen, num, "x")[count], rect_position(screen, num, "y")[count], 20, 20), 1)
    # rects(screen)
    red_x = [440, 440, 440, 440, 400, 400, 400, 360, 360, 320]
    red_y = [80, 120, 160, 200, 100, 140, 180, 120, 160, 140]
    green_x = [200, 200, 200, 200, 160, 160, 160, 120, 120, 80]
    green_y = [200, 240, 280, 320, 220, 260, 300, 240, 280, 260]
    blue_x = [440, 440, 440, 440, 400, 400, 400, 360, 360, 320]
    blue_y = [320, 360, 400, 440, 340, 380, 420, 360, 400, 380]

    initialize.rects(screen, red_x, red_y, (249, 37, 0))
    initialize.rects(screen, green_x, green_y, (64, 175, 78))
    initialize.rects(screen, blue_x, blue_y, (0, 0, 255))
    count = 0
    tmp = 0
    while (1):
        pygame.display.update()
        # イベント処理
        af_x = [0]*10
        af_y = [0]*10
        for event in pygame.event.get():
            if count == 0:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    click_process(x, y, red_x, red_y)
                    for num in range(10):
                        if (x > red_x[num] - 20) and (x < red_x[num] + 20) and (y > red_y[num] - 20) and (
                                y < red_y[num] + 20):
                            pygame.draw.rect(screen, (255, 0, 255), (red_x[num]-10,red_y[num]-10, 20, 20), 0)
                            pygame.draw.rect(screen, (0, 0, 0), (red_x[num]-10,red_y[num]-10, 20, 20), 1)
                            tmp = num
                            print(num)
                            count = 1
                            print("a")
            elif count == 1:
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    af_x[tmp] = initialize.mouseDownActionDirection(x, y,red_x[tmp],red_y[tmp],"typeX")
                    af_y[tmp] = initialize.mouseDownActionDirection(x, y,red_x[tmp],red_y[tmp],"typeY")
                    print(num,tmp,af_x[tmp], af_y[tmp],red_x[tmp], red_y[tmp])
                    pygame.draw.rect(screen, (255, 0, 0), (af_x[tmp]+10,af_y[tmp]-10, 20, 20), 0)
                    count = 0

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # コマの表示
    # initialize.rects(screen,red_x, red_y, (249,37,0))
    # initialize.rects(screen,green_x, green_y, (64,175,78))
    # initialize.rects(screen,blue_x, blue_y, (0,0,255))


if __name__ == "__main__":
    main()
