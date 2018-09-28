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
    point = initialize.rect_position()
    print(red_rect)
    koma = True #駒を選択するときか方向を選ぶときか
    turn = 1
    tmp = 0
    while (1):
        pygame.display.update()
        # イベント処理
        after = [0]*10
        # af_x = [0] * 10
        # af_y = [0] * 10
        for event in pygame.event.get():
            # if turn == 1: #赤の時
            #     turn_type = red_rect
            #     print("赤の番")
            #     af_color = (255,0,0)
            #     turn = 2
            # else: #turn == 2: #青の時
            #     turn_type = blue_rect
            #     print("青の番")
            #     af_color = (0,0,255)
            #     turn = 1
            if koma:
                # print(koma)
                if turn == 1: #赤の時
                    turn_type = red_rect
                    # print("赤の番")
                    af_color = (255,0,0)
                    turn = 2
                else: #turn == 2: #青の時
                    turn_type = blue_rect
                    # print("青の番")
                    af_color = (0,0,255)
                    turn = 1
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for num in range(10):
                        if (x > turn_type[num][0] - 20) and (x < turn_type[num][0] + 20) and (y > turn_type[num][1] - 20) and (
                                y < turn_type[num][1] + 20):
                            pygame.draw.rect(screen, (255, 255, 0), (turn_type[num][0], turn_type[num][1], 20, 20), 0)
                            pygame.draw.rect(screen, (0, 0, 0), (turn_type[num][0], turn_type[num][1], 20, 20), 1)
                            print("方向キーを押してね")
                            tmp = num
                            koma = False
            else:
                # print(koma)
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    after[tmp] = initialize.mouseDownActionDirection(x, y, turn_type[tmp][0], turn_type[tmp][1])
                    # print(num, tmp, af_x[tmp], af_y[tmp], turn_type[tmp][0], turn_type[tmp][1])
                    pygame.draw.rect(screen, af_color, (after[tmp][0], after[tmp][1], 20, 20), 0)
                    pygame.draw.rect(screen, (0, 0, 0), (turn_type[tmp][0], turn_type[tmp][1], 20, 20), 0)
                    print(turn_type[tmp][1], after[tmp][1])
                    turn_type[tmp][0] = after[tmp][0]
                    turn_type[tmp][1] = after[tmp][1]

                    koma = True
                    print(color)
            initialize.draw_rects(screen, color)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
