import pygame

def intro_scene(screen, draw_text):
    narration = [
        "Haïti... Pays de liberté, de douleur et d’espoir...",
        "L'histoire est chargée de victoires... mais aussi de trahisons.",
        "La politique ne regarde plus vers le peuple.",
        "Les jeunes se sentent seuls, oubliés...",
        "Mais toi... tu es différent(e).",
        "Tu crois encore. Tu es la lumière dans l'obscurité.",
        "Tu es DESTINE.",
        "Ton voyage commence aujourd'hui... seul(e), mais avec un rêve.",
        "Voici le garçon.",
        "Voici la fille."
    ]

    # Charger les images avec les bons noms et chemins
    garcon_img = pygame.image.load("assets/images/garçon.jpg").convert_alpha()
    fille_img = pygame.image.load("assets/images/fille.jpg").convert_alpha()

    # Redimensionner si besoin
    garcon_img = pygame.transform.scale(garcon_img, (100, 150))
    fille_img = pygame.transform.scale(fille_img, (100, 150))

    for line in narration:
        screen.fill((0, 0, 0))
        y = screen.get_height()//2
        draw_text(line, y)
        # Affiche l'image du garçon à côté du mot 'garçon'
        if "garçon" in line.lower():
            screen.blit(garcon_img, (500, y-75))
        # Affiche l'image de la fille à côté du mot 'fille'
        if "fille" in line.lower():
            screen.blit(fille_img, (500, y-75))
        pygame.display.flip()
        pygame.time.wait(3000)