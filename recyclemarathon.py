import pygame

import random

pygame.init()

WIDTH=1000
HEIGHT=800
TITLE="RECYCLE_MARATHON"

score=0
font=pygame.font.SysFont("Arial",40)

background=pygame.image.load("background1.png")
paperbag=pygame.image.load("paperbag.png")
paperbag=pygame.transform.scale(paperbag,(70,100))
plasticbag=pygame.image.load("plasticbag.png")
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
        super().__init__()
        self.image=i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


class Nonrecycle(pygame.sprite.Sprite):
    def __init__(self,x,y,i):
        super().__init__()
        self.image=i
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

rsprites=pygame.sprite.Group()

nonsprites=pygame.sprite.Group()

binsprites=pygame.sprite.Group()





bin=Bin(0,0,binimg)
sprites=pygame.sprite.Group()
sprites.add(bin)
binsprites.add(bin)


for i in range(10):
    box1=Recycle(random.randint(50,950),random.randint(50,750),box)
    sprites.add(box1)
    rsprites.add(box1)

for i in range(10):
    paperbag1=Recycle(random.randint(50,950),random.randint(50,750),paperbag)
    sprites.add(paperbag1)
    rsprites.add(paperbag1)

for i in range(30):
    plasticbag1=Nonrecycle(random.randint(50,950),random.randint(50,750),plasticbag)
    sprites.add(plasticbag1)
    nonsprites.add(plasticbag1)

for i in range(10):
    pen1=Recycle(random.randint(50,950),random.randint(50,750),pen)
    sprites.add(pen1)
    rsprites.add(pen1)
 
    

run = True
while run:
    screen.blit(background,(0,0))
    sprites.draw(screen)
    if pygame.sprite.groupcollide(binsprites,rsprites,False,True):
        score=score+1
    if pygame.sprite.groupcollide(binsprites,nonsprites,False,True):
        score=score-1
    keys=pygame.key.get_pressed()
    if keys [pygame.K_w]:
        bin.rect.y +=5
    if keys [pygame.K_s]:
        bin.rect.y -=5
    if keys [pygame.K_a]:
         bin.rect.x +=5
    if keys [pygame.K_d]:
        bin.rect.x -=5
    if bin.rect.left<0:
        bin.rect.left=0
    if bin.rect.right>1000:
        bin.rect.right=1000
    if bin.rect.top<0:
        bin.rect.top=0
    if bin.rect.bottom>800:
        bin.rect.bottom=800
    
    
    if pygame.sprite.groupcollide(binsprites,rsprites, False, True):
        score=score+1
    if pygame.sprite.groupcollide(binsprites,nonsprites, False, True):
        score=score-1

  
    score_text=font.render("Score"+str(score), True,"black")
    screen.blit(score_text,(20,20))
   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
         

 
    pygame.display.update()



