import pygame
import sys

def level1(screen, draw_text, selected):
    done = False
    choice_made = False


    while not done:
        screen.fill((0, 0, 0))
        draw_text("Niveau 1 - Quartier sale et abandonné", 50)
        draw_text("Tu proposes de nettoyer... personne ne vient.", 100)
        draw_text("1. Tu le fais seul(e)", 200)
        draw_text("2. Tu ignores", 250)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Gère les pressions de touches uniquement si nous sommes dans l'état de choix initial
            if event.type == pygame.KEYDOWN and current_scene_state == "initial_choice":
                if event.key == pygame.K_1:
                    choice_made = True
                    screen.fill((0, 0, 0))
                    draw_text("Tu nettoies seul(e)... Les gens te regardent, émus.", 300)
                    draw_text("5 jeunes sont inspirés. L'espoir naît.", 350)
                elif event.key == pygame.K_2:
                    choice_made = True
                    screen.fill((0, 0, 0))
                    draw_text("Tu ignores... L'odeur empire. Le quartier s'effondre.", 300)
                    draw_text("GAME OVER - L'indifférence détruit tout.", 350)
        if choice_made:
            pygame.display.flip()
            clock.tick(60)
            
        elif current_scene_state == "choice_1_result":
            # --- Séquence de résultat du choix 1 avec arrière-plan dynamique ---
            
            # Durée pendant laquelle cette scène de résultat sera affichée (en millisecondes)
            display_duration_ms = 5000 # 5 secondes
            result_start_time = pygame.time.get_ticks()
            
            # Boucle interne pour afficher le résultat du choix 1 avec l'animation d'arrière-plan
            result_display_active = True
            while result_display_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                elapsed_result_time = pygame.time.get_ticks() - result_start_time
                if elapsed_result_time >= display_duration_ms:
                    result_display_active = False # Termine la boucle interne
                    done = True # Termine le niveau après l'affichage du résultat
                    break # Sort de la boucle interne
                
                # Calcule l'image à afficher pour l'arrière-plan dynamique
                # Fait défiler les images en fonction du temps écoulé
                if loaded_result_images: # S'assure qu'il y a des images à afficher
                    image_index = (elapsed_result_time // (display_duration_ms // len(loaded_result_images))) % len(loaded_result_images)
                    screen.blit(loaded_result_images[image_index], (0, 0))
                else:
                    screen.fill(BLACK) # Fallback si aucune image n'a été chargée

                # Affiche le texte de résultat sur l'arrière-plan
                draw_text("Tu nettoies seul(e)... Les gens te regardent, émus.", 300)
                draw_text("5 jeunes sont inspirés. L'espoir naît.", 350)
                
                pygame.display.flip() # Met à jour l'écran
                clock.tick(60) # Contrôle le framerate de cette séquence

        elif current_scene_state == "choice_2_result":
            # Affiche le résultat du choix 2 (scénario de Game Over)
            draw_text("Tu ignores... L'odeur empire. Le quartier s'effondre.", 300)
            draw_text("GAME OVER - L'indifférence détruit tout.", 350)
            pygame.display.flip() # Affiche le texte du game over
            pygame.time.wait(5000) # Attend 5 secondes
            done = True # Quitte la boucle, terminant le niveau

        # Si 'done' est True (le niveau est terminé), la boucle principale 'while not done' se terminera.
        # Les `pygame.display.flip()` et `clock.tick(60)` sont maintenant gérés
        # à l'intérieur des blocs `if/elif` pour chaque état, ou dans la boucle interne du résultat.
        # Donc, pas besoin de les appeler ici si on est dans un état bloquant.
        # Pour les états non bloquants comme "initial_choice", ils sont déjà appelés.
