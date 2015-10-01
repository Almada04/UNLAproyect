import pygame

#contadores
moveright = 0
moveleft = 0
moveup=0
movedown=0
xi=0
yi=100

blanco=(0,0,0)

#carga de imagenes
idle1=pygame.image.load("resources\killer1.png")
mover1=pygame.image.load("resources\mover1.png")
mover2=pygame.image.load("resources\mover2.png")
#mover3
#mover4
pantalla=pygame.display.set_mode([640,245])

salir=False
reloj1=pygame.time.Clock()


def moverightk1():
    global moveright,xi,moveleft
    moveright=moveright+1
    moveleft=0
    if moveright==1:
        xi+=2
        pantalla.fill(blanco)
        pantalla.blit(mover1,(xi,yi))
    #if moveright==2:
        xi+=2
        pantalla.fill(blanco)
        pantalla.blit(mover2,(xi,yi))
     
def main():
        #CONFIGURACION
        pygame.init()
        
        global xi,yi,salir
        
        reloj1.tick(0)
        pantalla.fill(blanco)
        pantalla.blit(idle1,(xi,yi))
        
        while salir!=True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xi-=10
                    if event.key == pygame.K_RIGHT:
                        moverightk1()
                    if event.key == pygame.K_UP:
                        yi-=10
                    if event.key == pygame.K_DOWN:
                        yi+=10
                        
            pygame.display.update()
            
        pygame.quit()
main()