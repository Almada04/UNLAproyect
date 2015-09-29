import pygame
def main():
        #CONFIGURACION
        pygame.init()
        pantalla=pygame.display.set_mode([400,400])
        salir=False
        reloj1=pygame.time.Clock()
        
        #COLORES
        blanco=(255,255,255)
        rojo=(200,20,50)
        azul=(70,70,190)
        violeta=(100,20,30)
        amarillo=(222,20,45)
        
        
        #CREACION DE RECTANGULOS
        r1=pygame.Rect(50,50,50,50)
        r2=pygame.Rect(300,400,30,30)
        r3=pygame.Rect(10,200,60,60)
        r4=pygame.Rect(200,56,100,100) 
        
        
        #EVENTOS 
        while salir!=True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir=True
                    #EVENTO RECTANGULO 1 CON TECLAS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        r1.move_ip(-30,0)
                    if event.key == pygame.K_RIGHT:
                        r1.move_ip(30,0)
                    if event.key == pygame.K_UP:
                        r1.move_ip(0,-30)
                    if event.key == pygame.K_DOWN:
                        r1.move_ip(0,30)
                
            
            reloj1.tick(20)#20 fps
            pantalla.fill(blanco)#la consola sea blanca
            
            (r2.left,r2.top)=pygame.mouse.get_pos() #rectangulo 2 que tome eje x e y del mouse
            r2.left-=r2.width/2
            r2.top-=r2.height/2
            if r2.colliderect(r1):
                r1.inflate_ip(-1,-1)
                r2.inflate_ip(1,1)
                
            #DIBUJO LOS RECTANGULOS 
            pygame.draw.rect(pantalla,amarillo,r4)
            pygame.draw.rect(pantalla,violeta,r3)
            pygame.draw.rect(pantalla,rojo,r1)
            pygame.draw.rect(pantalla,azul,r2)
            
           
            
            pygame.display.update()
            
        pygame.quit()
main()