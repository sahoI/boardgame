import pygame
import initialize
from pygame.locals import *
import sys
from time import sleep  # https://www.sejuku.net/blog/21474

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("ダイヤモンドゲーム")
    screen.fill((255, 255, 255))
    initialize.background(screen)  # 背景
    initialize.draw_line(screen)  # 盤の目
    initialize.direction(screen) #方向キー
    color = [0,
             0, 0,
             0, 0, 0,
             1, 1, 1, 1, 0, 0, 2, 2, 2, 2,
             1, 1, 1, 0, 0, 0, 2, 2, 2,
             1, 1, 0, 0, 0, 0, 2, 2,
             1, 0, 0, 0, 0, 0, 2,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0,
             0, 0,
             0]
    initialize.draw_rects(screen, color)
    red_rect = initialize.decide_position(color, 1)
    blue_rect = initialize.decide_position(color, 2)
    green_rect = initialize.decide_position(color, 3)
    koma = True  # 駒を選択するときか方向を選ぶときか
    turn = 1
    tmp = 0
    while (1):
        pygame.display.update()
        # イベント処理
        after = [0] * 10
        for event in pygame.event.get():
            if koma:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if turn == 1:  # 赤の時
                        turn_type = red_rect
                        print("赤の番")
                    elif turn == 2:  #青の時
                        turn_type = blue_rect
                        print("青の番")
                    for num in range(10):
                        if (x > turn_type[num][0] - 20) and (x < turn_type[num][0] + 20) and (
                                y > turn_type[num][1] - 20) and (
                                y < turn_type[num][1] + 20):
                            pygame.draw.rect(screen, (255, 255, 0), (turn_type[num][0], turn_type[num][1], 20, 20), 0)
                            pygame.draw.rect(screen, (0, 0, 0), (turn_type[num][0], turn_type[num][1], 20, 20), 1)
                            tmp = num
                            koma = False
            else:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    after[tmp] = initialize.mouseDownActionDirection(x, y, turn_type[tmp][0], turn_type[tmp][1])
                    before_color_num = initialize.decide_color(turn_type[tmp][0], turn_type[tmp][1])
                    after_color_num = initialize.decide_color(after[tmp][0], after[tmp][1])
                    if color[after_color_num] != 0:
                        print("もう一回")
                        break
                    else:
                        color[after_color_num] = turn
                        if turn == 1:
                            turn = 2
                        elif turn == 2:
                            turn = 1
                        color[before_color_num] = 0
                        print(turn_type[tmp][1], after[tmp][1])
                        turn_type[tmp][0] = after[tmp][0]
                        turn_type[tmp][1] = after[tmp][1]

                        koma = True
                        initialize.draw_rects(screen, color) #駒を書き直す
                        initialize.win_check(color) #勝利条件

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
