import pygame
import sys
import os

def safe_load(path, size):
    if os.path.exists(path):
        img = pygame.image.load(path).convert()
        return pygame.transform.scale(img, size)
    else:
        print(f"Image non trouvée : {path}")
        return pygame.Surface(size)  # Surface vide

def level1(screen, draw_text, selected):
    # Chargement des images de fond
    bg_path = "assets/images/select.jpeg"
    success_path = "assets/images/success_bg.jpeg"
    failure_path = "assets/images/failure_bg.jpeg"

    background = safe_load(bg_path, screen.get_size())
    success_bg = safe_load(success_path, screen.get_size())
    failure_bg = safe_load(failure_path, screen.get_size())

    done = False
    choice_made = False

    while not done:
        # Affiche le fond initial tant que le choix n’est pas fait
        if not choice_made:
            screen.blit(background, (0, 0))
            draw_text("Niveau 1 - Quartier sale et abandonné", 50)
            draw_text("Tu proposes de nettoyer... personne ne vient.", 100)
            draw_text("1. Tu le fais seul(e)", 200)
            draw_text("2. Tu ignores", 250)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not choice_made:
                choice_made = True

                if event.key == pygame.K_1:
                    screen.blit(success_bg, (0, 0))  # Quartier propre
                    draw_text("Tu nettoies seul(e)... Les gens te regardent, émus.", 300)
                    draw_text("5 jeunes sont inspirés. L'espoir naît.", 350)

                elif event.key == pygame.K_2:
                    screen.blit(failure_bg, (0, 0))  # Quartier détruit
                    draw_text("Tu ignores... L'odeur empire. Le quartier s'effondre.", 300)
                    draw_text("GAME OVER - L'indifférence détruit tout.", 350)
                    pygame.display.flip()
                    pygame.time.wait(5000)
                    pygame.quit()
                    sys.exit()

                pygame.display.flip()
                pygame.time.wait(5000)
                done = True
