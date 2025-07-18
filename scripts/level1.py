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
    bg_path = "assets/images/select.jpeg"
    background = safe_load(bg_path, screen.get_size())
    done = False
    choice_made = False

    while not done:
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
                if event.key == pygame.K_1:
                    choice_made = True
                    screen.fill((0, 0, 0))
                    draw_text("Tu nettoies seul(e)... Les gens te regardent, émus.", 300)
                    draw_text("5 jeunes sont inspirés. L'espoir naît.", 350)
                elif event.key == pygame.K_2:
                    choice_made = True
                    draw_text("Tu ignores... L'odeur empire. Le quartier s'effondre.", 300)
                    draw_text("GAME OVER - L'indifférence détruit tout.", 350)
                    screen.background = (0, 0, 0)
        if choice_made:
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True
