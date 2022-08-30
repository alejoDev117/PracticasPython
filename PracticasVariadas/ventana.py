import random
import pygame , sys
def ventana(vida):
    # Ventana principal
    blanco = [255, 255, 255]
    negro = [0, 0, 0]
    pygame.init()
    tamaño = (400, 500)
    screen = pygame.display.set_mode(tamaño)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(blanco)
        if vida == 1:
            # primer error
            pygame.draw.line(screen, negro, (350, 500), (350, 50), 5)
            pygame.draw.line(screen, negro, (200, 50), (350, 50), 5)
            pygame.draw.line(screen, negro, (201, 50), (201, 100), 5)
        elif vida == 2:
          # primer error
          pygame.draw.line(screen, negro, (350, 500), (350, 50), 5)
          pygame.draw.line(screen, negro, (200, 50), (350, 50), 5)
          pygame.draw.line(screen, negro, (201, 50), (201, 100), 5)
          # segundo error
          pygame.draw.circle(screen, negro, (201, 150), 50)

        pygame.display.flip()
