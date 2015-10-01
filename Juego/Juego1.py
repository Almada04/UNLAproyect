import pygame

class player(pygame.sprite.Sprite):
    
    #DECLARACION DE IMAGENES 
    def __init__(self):
        self.imagen1=pygame.image.load("Killer1.png").convert_alpha()
        self.imagen2=pygame.image.load("Mover1.png").convert_alpha()
        self.imagenes=[self.imagen1,self.imagen2]
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
        self.seestamoviendo=False
        
    # MOVIMIENTOS , COLISIONES , MOVIMIENTOS ENEMIGOS
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    
    # ANIMACION DEL PERSONAJE CON IMAGENES
    def update(self,superficie,vx,vy,t):
        if  (vx,vy)== (0,0):
            self.seestamoviendo=False
        else: 
            self.seestamoviendo=True
        if t==1:
            self.imagen_actual+=1
        if self.imagen_actual>(len(self.imagenes)-1):
            self.imagen_actual=0
        self.mover(vx, vy)
        self.imagen=self.imagenes[self.imagen_actual]
        
        if self.seestamoviendo == False:
            self.imagen=self.imagenes[0]
        superficie.blit(self.imagen,self.rect)
        

def main():
    
    pygame.init()
    pantalla=pygame.display.set_mode((480,300))
    salir=False
    reloj1=pygame.time.Clock()
    
    player1=player()
    vx,vy=0,0
    velocidad=10
    lapretada,rapretada,dapretada,uapretada=False,False,False,False
    t=0
    
    #EVENTOS
    while salir!=True:
        for event in pygame.event.get():
            
            
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lapretada=True
                    vx=-velocidad
                if event.key == pygame.K_RIGHT:
                    rapretada=True
                    vx=velocidad
                if event.key == pygame.K_UP:
                    uapretada=True
                    vy=-velocidad
                if event.key == pygame.K_DOWN:
                    dapretada=True
                    vy=velocidad
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lapretada=False
                    if rapretada:
                        vx=velocidad
                    else:vx=0
                if event.key == pygame.K_RIGHT:
                    rapretada=False
                    if lapretada:
                        vx=-velocidad
                    else:vx=0
                if event.key == pygame.K_UP:
                    uapretada=False
                    if uapretada:
                        vy=-velocidad
                    else:vy=0
                    
                if event.key == pygame.K_DOWN:
                    dapretada=False
                    if dapretada:
                        vy=velocidad
                    else:vy=0
                
        
    
        reloj1.tick(30)
        
        t+=1
        if t>1:
            t=0
        
        pantalla.fill((200,200,200))
        player1.update(pantalla,vx,vy,t)
        pygame.display.update()
       
        
    pygame.quit()
    
main()