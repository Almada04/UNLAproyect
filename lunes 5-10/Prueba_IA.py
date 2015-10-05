import pygame
import random
from random import randrange
from pygame.event import Event

pygame.init()

pantalla=pygame.display.set_mode([640,245])

vy = 0
vx = 0
        
posx=randrange(50,200)
posy=randrange(50,550)

orient=False

xi=0
yi=100
fase=0
blanco=(255,255,255)

khleft,khright,khdown,khup=False,False,False,False

salir=False
reloj1=pygame.time.Clock()

     

class player(pygame.sprite.Sprite):
    def __init__(self):
        self.idleb=pygame.image.load("resources\zombieb.png")
        self.movib1=pygame.image.load("resources\zombieb1.png")
        self.movib2=pygame.image.load("resources\zombieb2.png")
        self.idlea=pygame.image.load("resources\zombiea.png")
        self.movia1=pygame.image.load("resources\zombiea1.png")
        self.movia2=pygame.image.load("resources\zombiea2.png")
        self.animacionesb=[self.idleb,self.movib1,self.movib2]
        self.animacionesa=[self.idlea,self.movia1,self.movia2]
        self.ani_estado=0
        self.img=self.movia1
        self.rect=self.img.get_rect()
        self.rect.top,self.rect.left=posx,posy
        self.status_anim=False
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy):
        self.mover(vx, vy)
        if pygame.KEYDOWN:
            self.anim()
        superficie.blit(self.img,self.rect)
    def anim(self):
        if vx>0:
            self.status_anim=True
            if fase==1:
                self.ani_estado+=1    
            if fase==2:
                self.ani_estado=2
            if self.ani_estado>(len(self.animacionesb)-1):
                self.ani_estado=0
            self.img=self.animacionesb[self.ani_estado]
        else:
            if khright==True:
                self.img=self.animacionesb[0]
        if vx<0:
            self.status_anim=True
            if fase==1:
                self.ani_estado+=1    
            if fase==2:
                self.ani_estado=2
            if self.ani_estado>(len(self.animacionesa)-1):
                self.ani_estado=0
            self.img=self.animacionesa[self.ani_estado]
        else:
            if khleft==True:
                self.img=self.animacionesa[0]
        

        
                
                

def main():
        #CONFIGURACION
        
        global xi,yi,salir,vx,khright,khleft,vy,khdown,khup,fase
        
        reloj1=pygame.time.Clock()
        pantalla.fill(blanco)
        player1=player()
        
        while salir!=True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        khright=True
                        khleft=False
                        vx+=10
                    if event.key == pygame.K_LEFT:
                        khleft=True
                        khright=False
                        vx-=10
                    if event.key == pygame.K_UP:
                        khup=True
                        vy-=10
                    if event.key == pygame.K_DOWN:
                        khdown=True
                        vy+=10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        if khleft:
                            vx-=10
                            khright=False
                        else:
                            vx=0
                    if event.key == pygame.K_LEFT:
                        if khright:
                            vx+=10
                            khleft=False
                        else:
                            vx=0
                    if event.key == pygame.K_UP:
                        if khdown:
                            vy+=10
                            khup=False
                        else:
                            vy=0
                    if event.key == pygame.K_DOWN:
                        if khup:
                            vy-=10
                            khdown=False
                        else:
                            vy=0
            fase=fase+1
            if fase>2:
                fase=0            
            xi+=vx
            yi+=vy
            reloj1.tick(15)                    
            pantalla.fill(blanco)  
            player1.update(pantalla,vx,vy)         
            pygame.display.update()
            
        pygame.quit()
main()