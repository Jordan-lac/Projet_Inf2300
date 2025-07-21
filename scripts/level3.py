import pygame
import os

def safe_load(path, size):
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)
    else:
        print(f"Image non trouvée : {path}")
        return pygame.Surface(size)

def level3(screen, draw_text, selected):
    pygame.init()
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = screen.get_size()

    # Chargement images
    background = safe_load("assets/images/background_level3.jpeg", (WIDTH, HEIGHT))
    player_img = safe_load("assets/images/player.jpg", (60, 80))  # ✅ image agrandie

    # Joueur — ✅ position de départ mise en dehors des zones interdites
    player = pygame.Rect(50, 50, 60, 80)
    speed = 4

    # Groupes avec messages uniques
    groups = [
        {"name": "group1", "rect": pygame.Rect(200, 300, 70, 70), "image": safe_load("assets/images/groupe 6.jpeg", (70, 70)), "message": "L’union fait la force."},
        {"name": "group2", "rect": pygame.Rect(500, 150, 70, 70), "image": safe_load("assets/images/group2.jpeg", (70, 70)), "message": "Ensemble, on peut tout rebâtir."},
        {"name": "group3", "rect": pygame.Rect(150, 450, 70, 70), "image": safe_load("assets/images/group3.jpeg", (70, 70)), "message": "Un seul peuple, un seul destin."},
        {"name": "group4", "rect": pygame.Rect(400, 500, 70, 70), "image": safe_load("assets/images/group4.jpeg", (70, 70)), "message": "Haïti, c’est nous tous !"},
        {"name": "group5", "rect": pygame.Rect(600, 350, 70, 70), "image": safe_load("assets/images/group5.jpeg", (70, 70)), "message": "Le changement commence avec nous."},
    ]

    visited = set()

    # ✅ Zones interdites plus petites
    forbidden_zones = [
        pygame.Rect(300, 200, 60, 60),
        pygame.Rect(600, 420, 50, 50),
        pygame.Rect(170, 170, 60, 40)
    ]

    running = True
    while running:
        screen.blit(background, (0, 0))

        # Affichage des groupes
        for group in groups:
            screen.blit(group["image"], group["rect"].topleft)

        # Zones interdites (en rouge)
        for zone in forbidden_zones:
            pygame.draw.rect(screen, (255, 0, 0), zone)

        # Sauvegarde de la position avant déplacement
        old_pos = player.topleft

        # Contrôle clavier
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        # Collision avec zone interdite → Game Over
        if any(player.colliderect(zone) for zone in forbidden_zones):
            draw_text("Tu es entré dans une zone interdite.\nGAME OVER.", 250)
            pygame.display.update()
            pygame.time.wait(2500)
            return selected

        # Interaction avec groupes
        for group in groups:
            if player.colliderect(group["rect"]) and group["name"] not in visited:
                draw_text(group["message"], 250)
                visited.add(group["name"])
                pygame.display.update()
                pygame.time.wait(1500)

        # Affichage du joueur
        screen.blit(player_img, player.topleft)

        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Victoire : tous les groupes visités
        if len(visited) == len(groups):
            draw_text("Tu es un leader des masses.", 300)
            pygame.display.update()
            pygame.time.wait(3000)
            running = False

        pygame.display.update()
        clock.tick(60)

    return selected
