import pygame
from pygame.locals import *
import sys

def circle_position(screen, num, str): #選択する円の作成→交点
    # num1 = [2,3,10,9,8,7,8,9,10,3,2,1]
    if str == "x":
        x = 510
        black_x=[550]
        for i in range(12):
            for j in range(num[i]):
                black_x.append(x)
            x-=40
        return black_x

    else:
        black_y=[250]
        y = [230,210,70,90,110,130,110,90,70,210,230,250]
        for i in range(12):
            for j in range(num[i]):
                black_y.append(y[i])
                y[i]+=40
        return black_y

#文字の色を引数にしてコマの出力を一つのメソッドで書けそう
#x,y座標の順番を一定にすればfor文で配列を作れそうor引数にx,y座標の配列を挿入する

def circles(screen, x, y, color): #各色のこま
    for num in range(10):
        pygame.draw.rect(screen,color,(x[num]-10,y[num]-10,20,20))
    font(screen,x,y)

def draw_line(screen): #盤の目
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

def font(screen,x,y):
    num = [1]
    for i in range(9):
        num.append(i+2)
    # print(num)
    sysfont = pygame.font.SysFont(None, 20)
    for i in range(10):
        text = sysfont.render(str(num[i]), True, (255,255,255))
        screen.blit(text, (x[i]-5,y[i]-5))

def background(screen):
    x = 0
    for count in range(120):
        pygame.draw.line(screen, (0,255,0), (x,0), (x, 800), 2) #右上から左下
        pygame.draw.line(screen, (0,255,0), (0,x), (1200, x), 2) #右上から左下
        x+=40

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))
    pygame.display.set_caption("ダイヤモンドゲーム")
    screen.fill((255,255,255))
    background(screen) #背景
    draw_line(screen) #盤の目
    num = [2,3,10,9,8,7,8,9,10,3,2,1]
    for count in range(73): #交点の円
        pygame.draw.rect(screen,(255,255,255),(circle_position(screen, num, "x")[count],circle_position(screen, num, "y")[count],20,20))
        pygame.draw.rect(screen,(0,0,0),(circle_position(screen, num, "x")[count],circle_position(screen, num, "y")[count],20,20),1)
    # circles(screen)
    red_x = [440,440,440,440,400,400,400,360,360,320]
    red_y = [80,120,160,200,100,140,180,120,160,140]
    green_x = [200,200,200,200,160,160,160,120,120,80]
    green_y = [200,240,280,320,220,260,300,240,280,260]
    blue_x = [440,440,440,440,400,400,400,360,360,320]
    blue_y = [320,360,400,440,340,380,420,360,400,380]

    circles(screen,red_x, red_y, (249,37,0))
    circles(screen,green_x, green_y, (64,175,78))
    circles(screen,blue_x, blue_y, (0,0,255))
    count = 0
    while(1):
        pygame.display.update()
        #イベント処理
        for event in pygame.event.get():
            # circles(screen,red_x, red_y, (249,37,0))
            # circles(screen,green_x, green_y, (64,175,78))
            # circles(screen,blue_x, blue_y, (0,0,255))
            print(count)
            if count == 0:
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # for num in range(10):
                    if (x > red_x[3]-20) or (x < red_x[3]+20) and (y > red_y[3]-20) or (y < red_y[3]+20):
                        print(x, red_x[3]-20, y, red_y[3]-20)
                        pygame.draw.rect(screen,(255,255,0),(red_x[3]-10,red_y[3]-10,20,20))
                        count += 1
                    # font(screen,red_x[num],red_y[num])
                    # print(x, y)
                    # pygame.draw.rect(screen,(255,255,255),(red_x[3]-10,red_y[3]-10,20,20))
                    # pygame.draw.rect(screen,(0,0,0),(red_x[3]-10,red_y[3]-10,20,20),1)

                    # red_x[3] = x
                    # red_y[3] = y
                    # x -= player.get_width() / 2
                    # y -= player.get_height() / 2
            else:
                # print(count)
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for num in range(10):
                        a = 0

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #コマの表示
            # circles(screen,red_x, red_y, (249,37,0))
            # circles(screen,green_x, green_y, (64,175,78))
            # circles(screen,blue_x, blue_y, (0,0,255))

if __name__ == "__main__":
    main()
