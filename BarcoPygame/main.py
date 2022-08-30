import pygame , sys , random,time  # importacion de las librerias
#colores
blanco = [255,255,255]
negro = [0,0,0]
carmeci = [139,0,0]
amarillo = [255,140,0]
#clases
class Mina(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mina.png").convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y>500:
            self.rect.y = -10
            self.rect.x =random.randrange(380)

class Barco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("barco.png").convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()

class Torpedo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("torpedo.png").convert()
        self.image.set_colorkey(blanco)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -=3

def drawText(surface,text,size,x,y):
    font = pygame.font.SysFont("serif",size)
    text_surface = font.render(text,True,blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop =(x,y)
    surface.blit(text_surface,text_rect)
pygame.init()
#Pantalla////////////////////////////
tamaño = (400,500)
screen = pygame.display.set_mode(tamaño)
fondo = pygame.image.load("fondo.jpg").convert()
clock = pygame.time.Clock()

#Esconder el mouse//////////////////////////////////
pygame.mouse.set_visible(0)

mina_list = pygame.sprite.Group()# aleatoriedad de los obstaculos
all_sprite_list = pygame.sprite.Group()
torpedo_list =pygame.sprite.Group()
cantidad = 0
for i in range(10):
 for i in range(6):
    mina = Mina()
    mina.rect.x = random.randint(2,390)
    mina.rect.y = random.randrange(300)
    mina_list.add(mina)
    all_sprite_list.add(mina)
    cantidad += 1
#movimiento del barco///////////////
cordX = 200
cordY = 440
speedX = 0
speedY = 0

barco = Barco()
all_sprite_list.add(barco)
#inicializacion de marcadores
vidas = 3
puntos = 0
punt = 0
point = 0
#sonidos del juego
explosion = pygame.mixer.Sound("explosion.ogg")
vidaExtra = pygame.mixer.Sound("vida.ogg")
daño = pygame.mixer.Sound("daño.ogg")
fin = pygame.mixer.Sound("Kirby-victory.ogg")
fail = pygame.mixer.Sound("fail.ogg")
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:#eventos al presionar teclas
            if event.key == pygame.K_LEFT:
                speedX = -3
            if event.key == pygame.K_RIGHT:
                speedX = 3
            if event.key == pygame.K_UP:
                speedY = -3
            if event.key == pygame.K_DOWN:
                speedY = 3
            if event.key == pygame.K_SPACE:
                torpedo = Torpedo()
                torpedo.rect.x = barco.rect.x
                torpedo.rect.y = barco.rect.y -22
                all_sprite_list.add(torpedo)
                torpedo_list.add(torpedo)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speedX = 0
            if event.key == pygame.K_RIGHT:
                speedX = 0
            if event.key == pygame.K_UP:
                speedY = 0
            if event.key == pygame.K_DOWN:
                speedY = 0
    #coliciones //////////////////////////
    mina_col_list = pygame.sprite.spritecollide(barco,mina_list,True)
    for i in mina_col_list:
        vidas -= 1
        cantidad -=1
        daño.play()
    corazones = "Vidas:" + str(vidas)
    if vidas==0:
        fail.play()
        time.sleep(3)
        break
    for torpedo in torpedo_list:
        mina_col_list = pygame.sprite.spritecollide(torpedo,mina_list,True)
        for i  in mina_col_list:
          torpedo_list.remove(torpedo)
          all_sprite_list.remove(torpedo)
          puntos += 1
          punt +=1
          explosion.play()
        if torpedo.rect.y < - 10 :
            all_sprite_list.remove(torpedo)
            torpedo_list.remove(torpedo)
    point ="Puntos:"+str(punt)
    if puntos == 10:
        texto = "+1 Vida"#marcadores
        vidas += 1
        vidaExtra.play()
        puntos = 0
    if punt >=cantidad:
        fin.play()
        time.sleep(4)
        break
    cordX += speedX#velocidades del teclado
    cordY += speedY
    screen.blit(fondo,[0,0])# fondo de pantalla
    barco.rect.x = cordX#movimiento del personaje con el teclado
    barco.rect.y = cordY
    mina_list.update()
    torpedo_list.update()# movimiento de los sprite
    all_sprite_list.draw(screen)# impresion de todos los sprites
    drawText(screen,str(corazones),25,50 ,5)#imprime los marcadores
    drawText(screen,str(point),25,330,5)
    pygame.display.flip()  # actualizar la pantalla
    clock.tick(60)
if punt == cantidad:
 print("Fin del juego, ganaste ")
else:
    print("fin del juego, perdiste")
