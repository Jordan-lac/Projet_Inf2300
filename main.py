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
    bar_width = 400
    bar_height = 30
    x = (WIDTH - bar_width) // 2
    y = HEIGHT // 2
    start = time.time()
    while True:
        elapsed = time.time() - start
        percent = min(1, elapsed / duration)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (x, y, bar_width, bar_height), 2)
        pygame.draw.rect(screen, (0,180,255), (x+2, y+2, int((bar_width-4)*percent), bar_height-4))
        draw_text(f"Chargement... {int(percent*100)}%", y+50)
        pygame.display.flip()
        if percent >= 1:
            break
        pygame.time.wait(30)

def main():
    show_loading_circle(screen, duration=2)
    selected = character_select(screen, draw_text)
    show_loading_bar_with_percentage(screen, duration=2)
    intro_scene(screen, draw_text)
    level1(screen, draw_text, selected)
    pygame.quit()

if __name__ == "__main__":
    main()
