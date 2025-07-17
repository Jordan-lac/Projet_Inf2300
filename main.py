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
    pygame.quit()

if __name__ == "__main__":
    main()
