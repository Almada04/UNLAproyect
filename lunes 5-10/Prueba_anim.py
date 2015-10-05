import pygame



pantalla=pygame.display.set_mode([640,245])

class player(pygame.sprite.Sprite):
    def __init__(self):
        self.idle1=pygame.image.load("resources\zombieb.png")
        self.movi1=pygame.image.load("resources\zombieb1.png")
        self.movi2=pygame.image.load("resources\zombieb2.png")
        self.animaciones=[self.idle1,self.movi1,self.movi2]
        self.ani_estado=0
        self.img=self.animaciones[self.ani_estado]
        self.rect=self.img.get_rect()
        self.rect.top,self.rect.left=vx,vy
        self.status_anim=False
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy,fase):
        if (vx,vy) == (0,0):
            self.status_anim=False
        else:
            self.status_anim=True
        if fase==1:
            self.ani_estado+=1
        if fase==2:
            self.ani_estado=2
        if self.ani_estado>(len(self.animaciones)-1):
            self.ani_estado=0
        self.mover(vx, vy)
        self.img=self.animaciones[self.ani_estado]
        if self.status_anim==False:
            self.img=self.animaciones[0]
        superficie.blit(self.img,self.rect)

vy = 0
vx = 0
xi=0
yi=100
fase=0
blanco=(255,255,255)


khleft,khright,khdown,khup=False,False,False,False

salir=False
reloj1=pygame.time.Clock()

     
def main():
        #CONFIGURACION
        pygame.init()
        
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
                        vx+=10
                    if event.key == pygame.K_LEFT:
                        khleft=True
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
                        else:
                            vx=0
                    if event.key == pygame.K_LEFT:
                        if khright:
                            vx+=10
                        else:
                            vx=0
                    if event.key == pygame.K_UP:
                        if khdown:
                            vy+=10
                        else:
                            vy=0
                    if event.key == pygame.K_DOWN:
                        if khup:
                            vy-=10
                        else:
                            vy=0
            fase=fase+1
            if fase>2:
                fase=0            
            xi+=vx
            yi+=vy
            reloj1.tick(10)                    
            pantalla.fill(blanco)  
            player1.update(pantalla,vx,vy,fase)         
            pygame.display.update()
            
        pygame.quit()
main()