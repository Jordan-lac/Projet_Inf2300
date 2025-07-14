import pygame

def intro_scene(screen, draw_text):
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
        "Men gason an.",
        "Men fi a."
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