import pygame
import sys
from scripts.character_select import character_select
from scripts.intro_scene import intro_scene
from scripts.level1 import level1

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DESTINE - Se Bati yon Nasyon")


# === Mettre la fenêtre au premier plan sous Windows ===
try:
    import ctypes
    hwnd = pygame.display.get_wm_info()['window']
    ctypes.windll.user32.SetForegroundWindow(hwnd)
except Exception as e:
    print("Impossible de mettre la fenêtre au premier plan :", e)


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


def draw_text(text, y, color=WHITE, center=True):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        rect = rendered.get_rect(center=(WIDTH//2, y + i*30)) if center else rendered.get_rect(topleft=(50, y + i*30))
        screen.blit(rendered, rect)

def show_loading_circle(screen, duration=2):
    import time
    center = (WIDTH // 2, HEIGHT // 2)
    radius = 40
    start = time.time()
    angle = 0
    while time.time() - start < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, center, radius, 2)
        # Arc animé
        end_angle = angle + 120
        pygame.draw.arc(
            screen, (0, 180, 255),
            (center[0]-radius, center[1]-radius, radius*2, radius*2),
            angle * 3.14 / 180, end_angle * 3.14 / 180, 6
        )
        draw_text("Chargement...", center[1]+60)
        pygame.display.flip()
        angle = (angle + 8) % 360
        pygame.time.wait(30)

def show_loading_bar_with_percentage(screen, duration=2):
    import time
    
    # Chemin vers votre image de fond. Assurez-vous que ce chemin est correct !
    # Remplacez 'assets/images/background.jpeg' par le chemin réel de votre image.
    try:
        background_image = pygame.image.load('assets/images/background.jpeg').convert()
        # Redimensionne l'image pour qu'elle corresponde à la taille de l'écran si nécessaire.
        # Utilisez .convert_alpha() si votre image a des transparences.
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    except pygame.error as e:
        print(f"Erreur lors du chargement de l'image de fond : {e}")
        background_image = None # Aucune image de fond si elle ne peut pas être chargée
    
    bar_width = 400
    bar_height = 30
    x = (WIDTH - bar_width) // 2
    y = HEIGHT // 2
    
    # Utilisation de pygame.time.get_ticks() pour une meilleure précision du temps
    start_time = pygame.time.get_ticks() 
    
    clock = pygame.time.Clock() # Pour contrôler le framerate

    while True:
        # Temps écoulé depuis le début de l'animation en secondes
        elapsed = (pygame.time.get_ticks() - start_time) / 1000.0
        # Pourcentage de progression (limité à 1, soit 100%)
        percent = min(1, elapsed / duration)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # --- Dessin de l'arrière-plan ---
        # Cette ligne DOIT être à l'intérieur de la boucle pour être redessinée à chaque frame.
        if background_image:
            screen.blit(background_image, (0, 0)) 
        else:
            # Si l'image n'a pas pu être chargée, remplir l'écran en noir comme fallback.
            screen.fill(BLACK) 

        # Dessine le contour de la barre de chargement
        pygame.draw.rect(screen, WHITE, (x, y, bar_width, bar_height), 2)
        
        # Dessine la barre de progression remplie
        # Le "-4" et "+2" sont pour créer une marge interne par rapport au contour
        pygame.draw.rect(screen, (0,180,255), (x + 2, y + 2, int((bar_width - 4) * percent), bar_height - 4))
        
        # Affiche le texte de chargement avec le pourcentage
        draw_text(f"Chargement... {int(percent * 100)}%", y + 50)
        
        # Met à jour l'affichage de l'écran
        pygame.display.flip()
        
        # Si le chargement est terminé (100%), sort de la boucle
        if percent >= 1:
            break
        
        # Limite le framerate à 60 FPS pour une animation fluide
        clock.tick(60)

def main():
    show_loading_circle(screen, duration=2)
    selected = character_select(screen, draw_text)
    # show_loading_bar_with_percentage(screen, duration=2)
    intro_scene(screen, draw_text)
    ###############
    show_loading_bar_with_percentage(screen, duration=2)
    ###############
    level1(screen, draw_text, selected)
    pygame.quit()

if __name__ == "__main__":
    main()
