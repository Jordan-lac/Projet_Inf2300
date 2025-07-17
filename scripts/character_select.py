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

def intro_scene(screen, draw_text):
    # Charger les backgrounds pour la narration (scene1 à scene10)
    size = screen.get_size()
    backgrounds = []
    for i in range(1, 11):
        if i not in [3,4,8,9,10]:
            path = f"assets/images/scene{i}.png"
        else:
            path = f"assets/images/scene {i}.jpeg"
        backgrounds.append(safe_load(path, size))

    narration = [
        "Ayiti... Peyi libète, doulè ak lespwa...",
        "Istwa a chaje ak viktwa... men tou ak trayizon.",
        "Politik la pa gade sou pèp la ankò.",
        "Jèn yo santi yo poukont yo, bliye...",
        "Men ou menm... ou diferan.",
        "Ou toujou kwè.",
        "Ou se limyè nan fènwa a.",
        "Ou se DESTINE.",
        "Vwayaj ou kòmanse jodi a... pou kont ou, men ak yon rèv.",
        "Men gason an."
    ]
    # Correction : chaque phrase a son background correspondant, pas de fond noir
    for i, line in enumerate(narration):
        screen.blit(backgrounds[i], (0, 0))
        draw_text(line, screen.get_height()//2)
        pygame.display.flip()
        pygame.time.wait(3000)

# Correction : background noir pour la sélection du personnage

def character_select(screen, draw_text):
    # Charger les images garçon/fille
    
    
   

    selecting = True
    selected = None
    while selecting:
        screen.fill((0, 0, 0))  # Fond noir
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
