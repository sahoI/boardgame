import pygame
import initialize
from pygame.locals import *
import sys

# 文字の色を引数にしてコマの出力を一つのメソッドで書けそう
# x,y座標の順番を一定にすればfor文で配列を作れそうor引数にx,y座標の配列を挿入する

# def click_process(x, y, red_x, red_y):
#     if x > 420 or x < 460 and y > 60 or y < 100:
#         # pygame.draw.rect(screen,(255,255,0),(red_x[3]-10,red_y[3]-10,20,20))
#         x = 430
#         y = 120
#     return x

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("ダイヤモンドゲーム")
    screen.fill((255,255,255))
    # initialize.background(screen)  # 背景
    initialize.background(screen)  # 背景
    initialize.draw_line(screen)  # 盤の目
    initialize.direction(screen)
    color = [0,
             0,0,
             0,0,0,
             1,1,1,1,0,0,2,2,2,2,
             1,1,1,0,0,0,2,2,2,
             1,1,0,0,0,0,2,2,
             1,0,0,0,0,0,2,
             0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,
             0,0,0,3,3,3,3,0,0,0,
             3,3,3,
             3,3,
             3]
    initialize.draw_rects(screen, color)
    red_rect = initialize.decide_position(color,1)
    blue_rect = initialize.decide_position(color,2)
    green_rect = initialize.decide_position(color,3)

    count = 0
    tmp = 0
    while (1):
        pygame.display.update()
        # イベント処理
        after = [0]*10
        # af_x = [0] * 10
        # af_y = [0] * 10
        for event in pygame.event.get():
            if count == 0:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for num in range(10):
                        if (x > red_rect[num][0] - 20) and (x < red_rect[num][0] + 20) and (y > red_rect[num][1] - 20) and (
                                y < red_rect[num][1] + 20):
                            pygame.draw.rect(screen, (255, 255, 0), (red_rect[num][0], red_rect[num][1], 20, 20), 0)
                            pygame.draw.rect(screen, (0, 0, 0), (red_rect[num][0], red_rect[num][1], 20, 20), 1)
                            tmp = num
                            count = 1
            elif count == 1:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    after[tmp] = initialize.mouseDownActionDirection(x, y, red_rect[tmp][0], red_rect[tmp][1])
                    # print(num, tmp, af_x[tmp], af_y[tmp], red_rect[tmp][0], red_rect[tmp][1])
                    pygame.draw.rect(screen, (255, 0, 0), (after[tmp][0] + 20, after[tmp][1], 20, 20), 0)
                    count = 0

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
