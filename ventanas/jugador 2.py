import pygame , sys
blanco = [255,255,255]
pygame.init()
tamaño = (634,496)
screen = pygame.display.set_mode(tamaño)
fondo = pygame.image.load("jugador2.jpg").convert()
clock = pygame.time.Clock()
sonido = pygame.mixer.Sound("victoria.ogg")
sonido.play()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(fondo,[0,0])
    pygame.display.flip()
    clock.tick(60)
