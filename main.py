import pygame
import sys
from scripts.character_select import character_select
from scripts.intro_scene import intro_scene
from scripts.level1 import level1
from scripts.level2 import level2
from scripts.level3 import level3  # Tu dois créer ce fichier level3.py


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

def draw_text(text, y, color=WHITE, center=True):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        rect = rendered.get_rect(center=(WIDTH//2, y + i*30)) if center else rendered.get_rect(topleft=(50, y + i*30))
        screen.blit(rendered, rect)

def main():
    selected = character_select(screen, draw_text)
    intro_scene(screen, draw_text)
    level1(screen, draw_text, selected)

    result = level2(screen, draw_text, selected)

    if result == "success":
        level3(screen, draw_text, selected)
    else:
        screen.fill((0, 0, 0))
        draw_text("Discours non valide. GAME OVER.", 250, color=(255, 0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter

    pygame.quit()

if __name__ == "__main__":
    main()
