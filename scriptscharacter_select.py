import pygame
import sys

def character_select(screen, draw_text):
    bg_path = "assets/images/background.jpeg"
    background = pygame.image.load(bg_path).convert()
    background = pygame.transform.scale(background, screen.get_size())
    selecting = True
    selected = None

    while selecting:
        screen.blit(background, (0, 0))
        draw_text("Choisissez votre personnage :", 100)
        draw_text("1. Garçon", 200)
        draw_text("2. Fille", 250)
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
