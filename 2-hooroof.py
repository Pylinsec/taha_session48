import pygame , sys
from tkinter import colorchooser


pygame.init()

size = (800,600)

color = (255,1,1)
white = (255,255,255)
black = (0,0,0)
line1_x1 = 0
line1_x2 = 0
line1_y1 = 0
line1_y2 = 0
win = pygame.display.set_mode(size)
pygame.display.set_caption('key review')
def select_color():
    global color
    color = colorchooser.askcolor(title='select color')[0]
    return color

while True:
    win.fill(black)
    pygame.draw.line(win,color,(line1_x1,0),(line1_x2,600),5)
    pygame.draw.line(win,color,(0,line1_y1),(800,line1_y2),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)    
            line1_x1 = line1_x2  = event.pos[0]
            line1_y1 = line1_y2  = event.pos[1]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                select_color()    





            

    pygame.display.update()        