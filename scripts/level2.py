import pygame
import os

def level2(screen, draw_text, selected):
    clock = pygame.time.Clock()
    running = True

    # === Chargement des images ===
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
    speaker_img = pygame.image.load(os.path.join(assets_dir, "speaker.jpeg")).convert_alpha()
    environment_img = pygame.image.load(os.path.join(assets_dir, "environment.jpeg")).convert_alpha()
    audience_img = pygame.image.load(os.path.join(assets_dir, "audience.jpeg")).convert_alpha()

    speaker_img = pygame.transform.scale(speaker_img, (150, 200))
    environment_img = pygame.transform.scale(environment_img, (800, 300))
    audience_img = pygame.transform.scale(audience_img, (300, 150))

    user_text = ""
    font = pygame.font.SysFont(None, 32)
    input_active = True
    feedback = ""
    niveau_suivant = False  # flag pour déclencher le passage au niveau 3

    # Mots-clés
    mots_cles_positifs = ["nature", "environnement", "arbres", "eau", "pollution", "protéger", "sauvons", "planète",
                          "écologie", "biodiversité", "protection", "sauver", "respecter", "préserver", "aider",
                          "soutenir", "agir", "responsabilité", "engagement", "sensibiliser", "éducation", "conscience",
                          "respect", "écosystème", "vivre", "harmonie", "équilibre", "avenir", "générations futures",
                          "sustainable", "durable", "bon"]
    mots_cles_negatifs = ["haine", "guerre", "idiot", "violence", "sale", "tuer", "brûler", "rien", "polluer",
                          "détruire", "abattre", "ignorer", "mépriser", "polluant", "toxique", "danger", "menace",
                          "crise", "désastre", "catastrophe", "destruction", "perte", "sacrifier","vide", "inutile",
                          "mauvais", "échec", "triste", "déception", "perdre", "abandonner", "laisser tomber",
                          "désespérer", "désespoir", "pessimisme", "négation", "indifférence", "ignorance", "haineux", "nuisible"]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if input_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    texte_min = user_text.lower()

                    if any(mot in texte_min for mot in mots_cles_negatifs):
                        feedback = "Discours inacceptable. Game Over."
                        input_active = False
                    elif any(mot in texte_min for mot in mots_cles_positifs):
                        feedback = "Tu es un protecteur de l'environnement."
                        input_active = False
                        niveau_suivant = True  # activer le passage au niveau suivant
                        feedback_start_time = pygame.time.get_ticks()
                    else:
                        feedback = "Discours hors sujet. Game Over."
                        input_active = False

                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # Affichage de la scène
        screen.fill((180, 220, 180))
        screen.blit(environment_img, (0, 350))
        screen.blit(speaker_img, (150, 270))
        screen.blit(audience_img, (350, 400))

        draw_text("Level 2 - Écris un discours pour sensibiliser à la nature :", 30)

        input_box = pygame.Rect(50, 100, 700, 150)
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)

        text_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        if feedback:
            draw_text(feedback, 300, color=(255, 0, 0))

        pygame.display.flip()
        clock.tick(60)

        # Si le feedback positif a été donné, attendre un délai avant de passer
        if niveau_suivant:
            now = pygame.time.get_ticks()
            if now - feedback_start_time > 2000:  # attendre 2 secondes
                return "success"
