def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((480,300))
    salir=False
    reloj1=pygame.time.Clock()
    
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
        
    
        reloj1.tick(20)
        pantalla.fill((200,200,200))
        pygame.display.update()
        
    pygame.quit()
    
main()