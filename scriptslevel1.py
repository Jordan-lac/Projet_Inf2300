import pygame
import sys
import os
def level1(screen, draw_text, selected):
    bg_path = "assets/images/background.jpeg"
    if not os.path.exists(bg_path):
        print("Image de fond non trouvée :", os.path.abspath(bg_path))
        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 0))
    else:
        background = pygame.image.load(bg_path).convert()
        background = pygame.transform.scale(background, screen.get_size())

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
                    screen.blit(background, (0, 0))
                    draw_text("Tu nettoies seul(e)... Les gens te regardent, émus.", 300)
                    draw_text("5 jeunes sont inspirés. L'espoir naît.", 350)
                elif event.key == pygame.K_2:
                    choice_made = True
                    screen.blit(background, (0, 0))
        if choice_made:
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True

