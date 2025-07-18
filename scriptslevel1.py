import pygame
import sys
import time # Gardez time ici pour les calculs de durée

# Assurez-vous que ces éléments sont définis globalement ou passés en paramètre
# WIDTH, HEIGHT, screen, draw_text (depuis votre script principal)

# Exemple de définitions globales si elles ne sont pas dans le script principal pour tester cette fonction
# pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Level 1 Test")
font = pygame.font.SysFont("arial", 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 180, 255)
LIGHT_GRAY = (100, 100, 100)
def draw_text(text, y, color=WHITE, center=True):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        rect = rendered.get_rect(center=(WIDTH//2, y + i*30)) if center else rendered.get_rect(topleft=(50, y + i*30))
        screen.blit(rendered, rect)


def level1(screen, draw_text, selected_character_info):
    done = False
    
    # Définition de la police pour le texte de résultat
    result_font = pygame.font.SysFont(None, 28) 

    # --- Configuration initiale de la scène (avant la boucle principale) ---
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    
    # Images spécifiques pour l'arrière-plan du résultat du choix 1.
    # Vous pouvez utiliser un sous-ensemble des images de narration ou des images différentes.
    # Pour simuler une "vidéo", nous allons en utiliser quelques-unes et les faire défiler.
    result_image_paths = [
        "assets/images/scene5.png",  # Exemple d'images inspirantes
        "assets/images/scene6.png",
        "assets/images/scene7.png",
        "assets/images/scene 8.jpeg",
        "assets/images/scene 12.jpeg"
    ]
    
    loaded_result_images = []
    for path in result_image_paths:
        try:
            img = pygame.image.load(path).convert_alpha()
            loaded_result_images.append(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)))
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image de résultat {path}: {e}")
            # Fallback: Ajoute un placeholder gris foncé transparent si l'image ne peut pas être chargée
            placeholder = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) 
            placeholder.fill((50, 50, 50, 255)) 
            loaded_result_images.append(placeholder)

    # Supprime la définition des lignes de narration et la logique associée
    # narration_lines = [...] # Supprimé
    # def draw_narration_text_centered(...) # Supprimé si plus utilisé ailleurs

    # État initial pour l'écran de sélection de choix
    current_scene_state = "initial_choice"
    
    # Horloge pour un framerate cohérent
    clock = pygame.time.Clock()

    while not done:
        # --- Gestion des événements ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Gère les pressions de touches uniquement si nous sommes dans l'état de choix initial
            if event.type == pygame.KEYDOWN and current_scene_state == "initial_choice":
                if event.key == pygame.K_1:
                    current_scene_state = "choice_1_result"
                    # Pas besoin de `proceed_to_narration` car nous allons gérer la séquence ici
                elif event.key == pygame.K_2:
                    current_scene_state = "choice_2_result"
        
        # --- Logique de Dessin ---
        screen.fill(BLACK) # Efface l'écran à chaque frame

        if current_scene_state == "initial_choice":
            # Affiche les options de choix initiales
            draw_text("Niveau 1 - Quartier sale et abandonné", 50)
            draw_text("Tu proposes de nettoyer... personne ne vient.", 100)
            draw_text("1. Tu le fais seul(e)", 200)
            draw_text("2. Tu ignores", 250)
            
            # Mise à jour de l'affichage et contrôle du framerate pour le choix initial
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
