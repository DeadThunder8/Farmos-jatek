import pygame

def main(display:pygame.Surface,clock:pygame.time.Clock):
    isMain = True
    while isMain:
        display.fill((0,0,0))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isMain = False

        pygame.display.update()
        clock.tick(60)
    