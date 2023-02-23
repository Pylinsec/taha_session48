import pygame , sys


pygame.init()

size = (500,600)
red = (255,1,1)
white = (255,255,255)
black = (0,0,0)

# define display 
win = pygame.display.set_mode(size)
pygame.display.set_caption('lines')

# list of line 
line_list = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # select mouse 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # select left click in mouse 
            if event.button == 1:
                line_list.append(event.pos)  
                # check for tow point 
                if len(line_list)>= 2:
                    # draw line
                    pygame.draw.lines(win,red,False, line_list,4)

            if event.button == 3:
                if len(line_list) > 2:
                    line_list.pop()
                    win.fill(black)
                    pygame.draw.lines(win,red,False, line_list,4)
                else:
                    win.fill(black)  
                    line_list.clear() 
        if event.type == pygame.MOUSEMOTION:
            if len(line_list)>= 2:
                win.fill(black)
                line_list[-1] = event.pos  
                pygame.draw.lines(win,red,False, line_list,4) 
                print(line_list) 
                

    pygame.display.update()        