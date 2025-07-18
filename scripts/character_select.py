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

def character_select(screen, draw_text):
    bg_path = "assets/images/select_bg.jpeg"
    background = safe_load(bg_path, screen.get_size())

    # Polices personnalisées
    title_font = pygame.font.SysFont("arial", 48, bold=True)
    option_font = pygame.font.SysFont("arial", 36)

    selecting = True
    selected = None

    while selecting:
        screen.blit(background, (0, 0))  # Afficher l’image de fond

        # 🎨 Titre en violet foncé
        title_text = title_font.render("Choisissez votre personnage :", True, (0, 0, 0))
        screen.blit(title_text, (screen.get_width()//2 - title_text.get_width()//2, 80))

        #  Garçon en bleu ciel
        garcon_text = option_font.render("1.  Garçon", True, (0, 191, 255))
        screen.blit(garcon_text, (screen.get_width()//2 - garcon_text.get_width()//2, 160))

        #  Fille en rose clair
        fille_text = option_font.render("2.  Fille", True, (255, 105, 180))
        screen.blit(fille_text, (screen.get_width()//2 - fille_text.get_width()//2, 220))

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
