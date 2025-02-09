import pygame
import random
from pygame import mixer 
mixer.init()
Color=(255,100,98)
#s_color=(167,255,100)
weight=500
height=600
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,weight):
        super().__init__()

        self.image=pygame.Surface([height,weight])

        

        pygame.draw.rect(self.image,color,pygame.Rect(0,0,weight,height))
        self.rect= self.image.get_rect()

    def moveright(self,pix):
        self.rect.x +=pix
    def moveleft(self,pix):
        self.rect.x -=pix
    def moveforward(self,speed):
        self.rect.y +=speed*speed/2
    def movebackward(self,speed):
        self.rect.y -=speed*speed/2


bg=pygame.image.load("images.jpeg")
bg=pygame.transform.scale(bg,(500,400))


screen=pygame.display.set_mode((400,500))
pygame.display.set_caption("baundary sprite")
bgcolor="blue"
screen.fill( bgcolor)

all=pygame.sprite.Group()

sp2=sprite("black",20,30)
sp2.rect.x=random.randint(0,480)
sp2.rect.y=random.randint(0,370)
all.add(sp2)
sp3=sprite("cyan",20,30)
sp3.rect.x=random.randint(0,480)
sp3.rect.y=random.randint(0,370)
all.add(sp3)
exit=True
clock=pygame.time.Clock()
rad=20
while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sp2.moveleft(5)
    if key[pygame.K_RIGHT]:
        sp2.moveright(5)
    if key[pygame.K_DOWN]:
        sp2.moveforward(5)
    if key[pygame.K_UP]:
        sp2.movebackward(5)



            
    all.update()
    
    all.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    screen.blit(bg, (0,0))

    if sp2.rect.colliderect(sp3.rect):
        all.remove(sp3)
        text="you win"
        font=pygame.font.SysFont("TIMES NEW ROMAN",50)
        text=font.render(text,True(158,16,16))
        screen.blit(text,(200-text.get_width()//2,150-text.get_height()//2))
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()