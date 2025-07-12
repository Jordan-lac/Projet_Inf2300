import pygame
import sys

def character_select(screen, draw_text):
    # Charger les images
    garcon_img = pygame.image.load("assets/images/garçon.jpg").convert_alpha()
    fille_img = pygame.image.load("assets/images/fille.jpg").convert_alpha()
    garcon_img = pygame.transform.scale(garcon_img, (100, 150))
    fille_img = pygame.transform.scale(fille_img, (100, 150))

    selecting = True
    selected = None
    while selecting:
        screen.fill((0, 0, 0))
        draw_text("Choisissez votre personnage :", 100)
        draw_text("1. Garçon", 200)
        draw_text("2. Fille", 250)
        # Afficher les images à côté des choix
        screen.blit(garcon_img, (90, 100))  # À côté de '1. Garçon'
        screen.blit(fille_img, (170, 150))   # À côté de '2. Fille'
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = "garçon"
                    selecting = False
                elif event.key == pygame.K_2:
                    selected = "fille"
                    selecting = False
    return selected
