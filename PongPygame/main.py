import pygame , sys , time , random

blanco = [255,255,255]
negro = [0,0,0]
rojo = [255,0,0]
azul = [0,0,255]
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
reloj = pygame.time.Clock()
pygame.mouse.set_visible(0)
#texto en la pantalla

def textoPantalla(surface, text ,color, size , x , y ):
    font = pygame.font.SysFont("Latin",size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x , y)
    surface.blit(text_surface,text_rect)

pong = pygame.mixer.Sound("paleta.ogg")
punto = pygame.mixer.Sound("punto.ogg")
pared = pygame.mixer.Sound("pared.ogg")
#velocidad y movimiento jugador
cordY = 200
speedY = 0
#IA enemiga
cordY2 = 200
speedY2 = 0
#pelota
cordPeloX = 350
cordPeloY = 250
speedPX = 3
speedPY = 3
#contadores
conPlayer = 0
conEnemi = 0

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speedY2 = 4
            if event.key == pygame.K_UP:
                speedY2 = -4
            if event.key == pygame.K_s:
                speedY = 4
            if event.key == pygame.K_w:
                speedY = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speedY2 = 0
            if event.key == pygame.K_DOWN:
                speedY2 = 0
            if event.key == pygame.K_s:
                speedY = 0
            if event.key == pygame.K_w:
                speedY = 0

    cordPeloX += speedPX
    cordPeloY += speedPY
    if cordPeloY > 465 or cordPeloY < 10:#rebote pelota horizontalmente
        speedPY *= -1
        pared.play()
    if cordPeloX > 730 :#sale por la derecha
        cordPeloX = 350
        cordPeloY = 250
        speedPX *=-1
        speedPY *=-1
        conPlayer += 1
        punto.play()
    if cordPeloX < -30:#si sale por la izquierda
        cordPeloX = 350
        cordPeloY = 250
        speedPX *= -1
        speedPY *= -1
        punto.play()
        conEnemi += 1
    if conEnemi == 3 or conPlayer == 3 :
        punto.play()
        time.sleep(1)
        break
    cordY += speedY
    cordY2 += speedY2
    screen.fill(negro)
    textoPantalla(screen,str(conPlayer),azul,100,180,50)
    textoPantalla(screen,str(conEnemi),rojo,100,500,50)
    pelota =pygame.draw.rect(screen,blanco,(cordPeloX,cordPeloY,30,30))# pelota
    pygame.draw.rect(screen,blanco,(0,0,700,10))
    pygame.draw.rect(screen,blanco,(0,495,700,10))
    jugador = pygame.draw.rect(screen,azul,(5,cordY,20,100))#jugador
    if cordY == 0:
        speedY = 0
    if cordY == 400:
        speedY = 0
    enemigo = pygame.draw.rect(screen,rojo,(675,cordY2,20,100))# movimiento enemigo
    if cordY2 == 0:
        speedY2 = 0
    if cordY2 == 400:
        speedY2 = 0
    for i in range(0,500,20):
        pygame.draw.rect(screen,blanco,(345,i,5,10))#for loop mitad
    if pelota.colliderect(jugador) or pelota.colliderect(enemigo):#coliciones enemigo
        pong.play()
        speedPX *=-1
    pygame.display.flip()
    reloj.tick(60)

