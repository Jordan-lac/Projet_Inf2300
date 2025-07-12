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
        "Ton voyage commence aujourd'hui... seul(e), mais avec un rêve."
    ]
    for line in narration:
        screen.fill((0, 0, 0))
        draw_text(line, screen.get_height()//2)
        pygame.display.flip()
        pygame.time.wait(3000)
