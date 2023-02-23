import pygame , sys


pygame.init()

size = (500,600)
red = (255,1,1)
white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode(size)
pygame.display.set_caption('key review')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            ch = pygame.key.get_pressed()
            print(pygame.K_a)
            if ch[pygame.K_a]:
                print('a was pressed')

    pygame.display.update()        