import pygame
import sys
import random

for i in range(1,82):
        choice = random.choice([0,0,random.randint(1,9)])
        exec("var"+str(i)+" ="+str(choice))

def Play():
        pygame.init()
        white = (255,255,255)
        light_sky_blue = (135,206,250)
        dodger_blue = (30,144,255)
        black = (0,0,0)
        table = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65,var66,var67,var68,var69,var70,var71,var72,var73,var74,var75,var76,var77,var78,var79,var80,var81,]
        font = pygame.font.SysFont('verdana', 20)
        screen_width = 460
        screen_height = 370
        screen = pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("Sudoku")
        icon = pygame.image.load("sudoku.png")
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()
        time = 0
        def Time_Count(seconds):
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
                time_txt = font.render("Time: "+Time_Count(time//6),True, black)
                screen.blit(time_txt, (170,310))
                for var in table:
                        if var == 0:
                                temp = font.render(str(" "), True, black)
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
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if x*45-15 < mouse[0] < x*45+25 and y*30 < mouse[1] < y*30+25 and click[0]:
                                if table[(y*10+x)-y-10] == 9:
                                        table[(y*10+x)-y-10] = 1
                                else:
                                        table[(y*10+x)-y-10] += 1
                        index += 1     
                        x += 1
                time += 1
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
#Check horizontally
'''
x = 2
i = 12
j = 0
while 12 <= i <= 12+2:
	while j < 3:
		if i != 14 and j != 2:
			if arr[i][j] == x:
				print((i, j))
		j += 1
	j = 0
	i += 1
'''
'''Check vertically'''
#i = 0
#while i <= 24:
#	print(arr[i][1])
#	i += 3
