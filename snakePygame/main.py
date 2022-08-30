import pygame , sys , random , time

blanco = [255,255,255]
rojo = [255,0,0]
verde = [0,128,0]
negro = [0,0,0]

pygame.init()

def textoPantalla(surface, text , size , x , y ):
    font = pygame.font.SysFont("Latin",size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x , y)
    surface.blit(text_surface,text_rect)

tamaño = (400,500)
screen = pygame.display.set_mode(tamaño)
reloj = pygame.time.Clock()
Eat = pygame.mixer.Sound("paleta.ogg")
Muerte = pygame.mixer.Sound("daño.ogg")
#movimiento jugador
cordx = 150
cordy = 150
speedx = 0
speedy = 0
cordXM = random.randint(10, 380)
cordYM = random.randint(110, 480)
n = 0
f = 2
#coordenadas de las manzanas
cordx2 = 0
cordy2 = 0
puntos = ""
#/////////////////////////////////////////////////
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speedy = -1
                speedx = 0
            if event.key == pygame.K_DOWN:
                speedy = 1
                speedx = 0
            if event.key == pygame.K_LEFT:
                speedx = -1
                speedy = 0
            if event.key == pygame.K_RIGHT:
                speedx = 1
                speedx = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speedy = -1
                speedx = 0
            if event.key == pygame.K_DOWN:
                speedy = 1
                speedx = 0
            if event.key == pygame.K_LEFT:
                speedx = -1
                speedy = 0
            if event.key == pygame.K_RIGHT:
                speedx = 1
                speedy = 0
    cordx += speedx
    cordy += speedy
    screen.fill(negro)
    textoPantalla(screen, puntos,40,75,40)
    textoPantalla(screen,"Snake <|-|><|-|>", 40, 270, 40)
    #limites
    pared1 = pygame.draw.rect(screen,blanco,(0,100,400,5))
    pared2 = pygame.draw.rect(screen,blanco,(0,495,400,5))
    pared3 = pygame.draw.rect(screen,blanco,(0,100,5,400))
    pared4 = pygame.draw.rect(screen,blanco,(395,100,5,400))
    pygame.draw.rect(screen,blanco,(0,0,5,100))
    pygame.draw.rect(screen,blanco,(395,0,5,100))
    #jugador
    jugador = pygame.draw.rect(screen,verde, (cordx, cordy, 15, 15))
    if n >= 1:
        f = 1
        if speedx == 1: # a la derecha es la misma coordenada Y
            cordx2 = cordx-15*f
            cordy2  = cordy
        elif speedx == -1:# a la izquierda lo mismo
            cordx2 = cordx + 15*f
            cordy2 = cordy
        elif speedy == 1:# para abajo es la mim
            cordy2 = cordy - 15*f
            cordx2 = cordx
        elif speedy == -1:
            cordy2 = cordy + 15*f
            cordx2 = cordx
        pygame.draw.rect(screen, verde, (cordx2, cordy2, 15, 15))
    #manzanas
    manzana1 = pygame.draw.rect(screen,rojo,(cordXM,cordYM,20,20))
    if jugador.colliderect(manzana1):#cuando toca la manzana la teletrasnporta aleatoriamente
        cordXM = random.randint(10, 380)
        cordYM = random.randint(110, 480)
        n += 1
        Eat.play()
    if jugador.colliderect(pared1) or jugador.colliderect(pared2) or jugador.colliderect(pared3) or jugador.colliderect(pared4):
        Muerte.play()
        time.sleep(2)
        break
        pygame.draw.rect(screen, verde, (cordx2,cordy2, 15, 15))
    puntos = "Puntos: " + str(n)
    pygame.display.flip()
    reloj.tick(60)

print("Game Over")
