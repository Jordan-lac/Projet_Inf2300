import pygame
import sys

def intro_scene(screen, draw_text):
    pygame.mixer.init()
    musique2 = pygame.mixer.Sound("assets/musiques/Voice_off.mp3")
    channel2 = pygame.mixer.Channel(1)
    channel2.play(musique2)
    channel2.set_volume(0.6)

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
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    scene_images = [
        pygame.image.load("assets/images/scene1.png").convert_alpha(),
        pygame.image.load("assets/images/scene2.png").convert_alpha(),
        pygame.image.load("assets/images/scene 3.jpeg").convert_alpha(),
        pygame.image.load("assets/images/scene 4.jpeg").convert_alpha(),
        pygame.image.load("assets/images/scene5.png").convert_alpha(),
        pygame.image.load("assets/images/scene6.png").convert_alpha(),
        pygame.image.load("assets/images/scene7.png").convert_alpha(),
        pygame.image.load("assets/images/scene 8.jpeg").convert_alpha(),
        pygame.image.load("assets/images/scene 12.jpeg").convert_alpha(),
        pygame.image.load("assets/images/scene 10.jpeg").convert_alpha(),
        pygame.image.load("assets/images/scene 11.jpeg").convert_alpha()
    ]
    scene_images = [pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)) for img in scene_images]
    font = pygame.font.SysFont(None, 28)
    def draw_text_centered(surface, text, y):
        text_surface = font.render(text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
        surface.blit(text_surface, text_rect)
    for i, line in enumerate(narration):
        screen.blit(scene_images[i % len(scene_images)], (0, 0))
        draw_text_centered(screen, line, SCREEN_HEIGHT - 60)
        pygame.display.flip()
        pygame.time.wait(3000)
