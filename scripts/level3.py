import pygame

def level3(screen, draw_text, selected):
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 100, 200))  # Fond bleu
        draw_text("Félicitations ! Tu as réussi le niveau 2 !", 200)
        draw_text("Prépare-toi pour le niveau 3...", 250)
        draw_text("Appuie sur ESC pour quitter.", 300)

        pygame.display.flip()
        clock.tick(60)
