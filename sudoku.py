import pygame
import sys
import random
import concurrent.futures
import time

for i in range(1,82):
        level1 = [8,0,7,9,4,0,3,1,0,0,3,1,0,7,6,4,0,0,0,0,0,1,0,0,0,5,0,9,0,0,5,0,0,0,0,0,0,0,0,0,0,0,1,6,0,1,0,5,3,0,7,0,2,4,0,0,3,0,0,2,6,9,1,0,1,0,6,9,3,0,4,0,4,0,0,7,0,0,2,3,8]
        exec("var"+str(i)+" ="+str(level1[i-1]))

def Play():
        pygame.init()
        white = (255,255,255)
        light_sky_blue = (135,206,250)
        dodger_blue = (30,144,255)
        black = (0,0,0)
        red = (255,0,0)
        table = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65,var66,var67,var68,var69,var70,var71,var72,var73,var74,var75,var76,var77,var78,var79,var80,var81,]
        tab_hori = [[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80]]
        tab_ver = [[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80]]
        tab_block = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
        i_block = [0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8]
        wrongs = set()
        font = pygame.font.SysFont('verdana', 20)
        screen_width = 460
        screen_height = 370
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load("sudoku.png")
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()
        T = 0
        def T_Count(seconds):
                try:
                        minutes = seconds // 60
                        seconds %= minutes
                except ZeroDivisionError:
                        seconds = seconds
                return "%02d:%02d" % (minutes,seconds)
        
        while True:
                clock.tick(6)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                screen.fill(white)
                x = 1
                y = 1
                index = 0
                pygame.draw.rect(screen,white,(25,25,410,275))
                T_txt = font.render("T: "+T_Count(T//6),True, black)
                screen.blit(T_txt, (170,310))
                for var in table:
                        if var == 0:
                                temp = font.render(str(" "), True, black)
                        elif index in wrongs:
                                temp = font.render(str(var), True, red)
                        else:
                                temp = font.render(str(var), True, black)
                        if not x == 10:
                                if ((y*10+x)-y-10) % 2 == 0:
                                        pygame.draw.rect(screen,light_sky_blue,(x*45-15,y*30,40,25))
                                else:
                                        pygame.draw.rect(screen,dodger_blue,(x*45-15,y*30,40,25))
                                screen.blit(temp,(x*45,y*30))
                                if x % 3 == 0 and not x == 9:
                                        pygame.draw.rect(screen,black,(x*45+25,30,5,265))
                        else:
                                y += 1
                                x = 1
                                if y % 3 == 0 and not y == 9:
                                        pygame.draw.rect(screen,black,(30,y*30+25,400,5))
                                if ((y*10+x)-y-10) % 2 == 0:
                                        pygame.draw.rect(screen,light_sky_blue,(x*45-15,y*30,40,25))
                                else:
                                        pygame.draw.rect(screen,dodger_blue,(x*45-15,y*30,40,25))
                                screen.blit(temp,(x*45,y*30))
                        index += 1     
                        x += 1

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                y = 1
                def add_one(x):   
                    if x*45-15 < mouse[0] < x*45+25 and y*30 < mouse[1] < y*30+25:
                        if table[(y*10+x)-y-10] == 9:
                            table[(y*10+x)-y-10] = 1
                        else:
                            table[(y*10+x)-y-10] += 1

                            hor = [i for i in tab_hori[y-1] if i != (y*10+x)-y-10]
                            ver = [i for i in tab_ver[x-1] if i != (y*10+x)-y-10]
                            block = [i for i in tab_block[i_block[(y*10+x)-y-10]] if i!= (y*10+x)-y-10]
                            
                            f1 = lambda i: (table[i] == table[(y*10+x)-y-10])
                            
                            with concurrent.futures.ThreadPoolExecutor() as executor:

                                    hor_ftr = executor.map(f1, hor)
                                    ver_ftr = executor.map(f1, ver)
                                    block_ftr = executor.map(f1, block)

                                    if any(rsl for rsl in hor_ftr):
                                            wrongs.add((y*10+x)-y-10)
                                    elif any(rsl for rsl in ver_ftr):
                                            wrongs.add((y*10+x)-y-10)
                                    elif any(rsl for rsl in block_ftr):
                                            wrongs.add((y*10+x)-y-10)
                                    else:
                                            wrongs.discard((y*10+x)-y-10)
                        return True
                    else:
                        return False

                itr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]
                if click[0]:
                        with concurrent.futures.ThreadPoolExecutor() as executor:
                            
                            futures = executor.map(add_one, itr)
                            
                            while True:
                                if any(rsl for rsl in futures):
                                    break
                                else:
                                    y += 1
                                    futures = executor.map(add_one, itr)

                T += 1
                pygame.display.update()


def Menu():
        pygame.init()
        white = (255,255,255)
        black = (0,0,0)

        font = pygame.font.SysFont('verdana', 45)
        font_2 = pygame.font.SysFont('segoeui', 70,)
        screen_width = 460
        screen_height = 370
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load("sudoku.png")
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()

        btn_x = 140
        btn_y = 170
        btn_w = 200
        btn_h = 50

        title_txt = font_2.render("Sudoku",True,black)
        start_txt = font.render("PLAY",True,white)
        while True:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if btn_x < mouse[0] < btn_x + btn_w and btn_y < mouse[1] < btn_y + btn_h and click[0]:
                        Play()
                        sys.exit()
                
                screen.fill(white)
                pygame.draw.rect(screen, black, (btn_x,btn_y,btn_w,btn_h))
                screen.blit(title_txt,(btn_x-10,btn_y-120))
                screen.blit(start_txt,(btn_x+45,btn_y))
                pygame.display.update()
Menu()
