import pygame
import random
import os

def safe_load(path, size):
    if os.path.exists(path):
        img = pygame.image.load(path).convert()
        return pygame.transform.scale(img, size)
    else:
        print(f"Image non trouvée : {path}")
        return pygame.Surface(size)  # Surface vide



def level4(screen, draw_text, selected):
    pygame.init()
    clock = pygame.time.Clock()

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    font = pygame.font.SysFont(None, 28)

    # Joueur
    player = pygame.Rect(100, 100, 40, 40)
    player_speed = 5

    # Groupes (zones à visiter)
    groups = [
        pygame.Rect(200, 150, 60, 60),
        pygame.Rect(400, 300, 60, 60),
        pygame.Rect(600, 120, 60, 60),
        pygame.Rect(250, 450, 60, 60),
    ]
    visited_groups = []

    # Dialogue actif
    active_dialogue = None
    show_choices = False
    current_choices = []
    group_index = -1
    finished = False

    def show_dialogue(group_num):
        nonlocal active_dialogue, show_choices, current_choices
        dialogues = [
            "Ce quartier veut plus d’écoles. Tu proposes quoi ?",
            "Ce groupe demande plus de sécurité.",
            "Ici, ils veulent de l’eau potable en continu.",
            "Ce secteur veut que leurs routes soient réparées."
        ]
        choices = [
            ["On va lancer un projet communautaire", "On attendra le gouvernement", "Ce n'est pas urgent"],
            ["On forme des patrouilles citoyennes", "On ignore pour l’instant", "Je reviens plus tard"],
            ["On installe un puits collectif", "On fera une réunion", "Pas de solution"],
            ["On crée une brigade de jeunes réparateurs", "On le notera plus tard", "Pas mon problème"]
        ]
        active_dialogue = dialogues[group_num]
        current_choices = choices[group_num]
        show_choices = True

    def draw_choices():
        for i, choice in enumerate(current_choices):
            pygame.draw.rect(screen, WHITE, (100, 400 + i*40, 600, 30))
            txt = font.render(f"{i + 1}. {choice}", True, BLACK)
            screen.blit(txt, (110, 405 + i*40))

    # Boucle principale
    running = True
    while running:
        screen.fill((30, 30, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if show_choices:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                        choice = (event.key - pygame.K_1)
                        if choice == 0:
                            draw_text("Groupe convaincu !", 400)
                            visited_groups.append(group_index)
                        else:
                            draw_text("Ils sont déçus de ta réponse...", 400)
                        show_choices = False
                        active_dialogue = None
                        current_choices = []

        # Mouvement joueur
        keys = pygame.key.get_pressed()
        if not show_choices and not finished:
            if keys[pygame.K_LEFT]: player.x -= player_speed
            if keys[pygame.K_RIGHT]: player.x += player_speed
            if keys[pygame.K_UP]: player.y -= player_speed
            if keys[pygame.K_DOWN]: player.y += player_speed

        # Dessiner groupes
        for i, group in enumerate(groups):
            color = GREEN if i in visited_groups else WHITE
            pygame.draw.rect(screen, color, group)

        # Détection de collision
        if not show_choices and not finished:
            for i, group in enumerate(groups):
                if player.colliderect(group) and i not in visited_groups:
                    group_index = i
                    show_dialogue(i)

        # Dessiner joueur
        pygame.draw.rect(screen, (0, 0, 255), player)

        # Afficher dialogue
        if active_dialogue:
            draw_text(active_dialogue, 100)
        if show_choices:
            draw_choices()

        # Affichage compteur
        compteur_text = font.render(f"Groupes convaincus : {len(visited_groups)} / {len(groups)}", True, WHITE)
        screen.blit(compteur_text, (10, 10))

        # Fin du niveau
        if len(visited_groups) == len(groups) and not finished:
            draw_text("TU ES L’UNIFICATEUR DE LA COMMUNAUTÉ !", 250)
            draw_text("L’union fait la force. Tu peux avancer.", 300)
            finished = True

        pygame.display.flip()
        clock.tick(30)
