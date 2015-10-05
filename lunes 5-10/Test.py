import pygame



pantalla=pygame.display.set_mode([640,245])

class player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=vx,vy
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie):
        self.mover(vx, vy) 
        superficie.blit(self.imagen,self.rect)
    

vy = 0
vx = 0
xi=0
yi=100

blanco=(255,255,255)

#carga de imagenes
idle1=pygame.image.load("resources\killer1.png")
mover1=pygame.image.load("resources\mover1.png")
mover2=pygame.image.load("resources\mover2.png")
#mover3
#mover4

khleft,khright,khdown,khup=False,False,False,False

salir=False
reloj1=pygame.time.Clock()

     
def main():
        #CONFIGURACION
        pygame.init()
        
        global xi,yi,salir,vx,khright,khleft,vy,khdown,khup
        
        reloj1=pygame.time.Clock()
        pantalla.fill(blanco)
        player1=player(mover1)
        
        
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
            xi+=vx
            yi+=vy
            reloj1.tick(20)                    
            pantalla.fill(blanco)  
            player1.update(pantalla)         
            pygame.display.update()
            
        pygame.quit()
main()