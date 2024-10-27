import pygame

WIDTH=1000
HEIGHT=800
TITLE="RECYCLE_MARATHON"

background=pygame.image.load("background1.png")
paperbag=pygame.image.load("item1.png")
plasticbag=pygame.image.load("paperbag.png")
box=pygame.image.load("box.png")
pen=pygame.image.load("pen.png")
binimg=pygame.image.load("bin.png")
binimg=pygame.transform.scale(binimg,(70,100))

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.image=i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y



class Recycle(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super()._init_()
        self.image=i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super()._init_()
        self.image=i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y



bin=Bin(0,0,binimg)
sprites=pygame.sprite.Group()
sprites.add(bin)



run = True
while run:
    screen.blit(background,(0,0))
    sprites.draw(screen)
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()



