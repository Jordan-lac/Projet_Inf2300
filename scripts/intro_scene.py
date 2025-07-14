import pygame

def intro_scene(screen, draw_text):
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
    for line in narration:
        screen.fill((0, 0, 0))
        draw_text(line, screen.get_height()//2)
        pygame.display.flip()
        pygame.time.wait(3000)
