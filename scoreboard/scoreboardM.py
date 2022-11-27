import pygame
import fajlkezelo
import load
import sys

def main(display:pygame.Surface,clock:pygame.time.Clock,rendszer:fajlkezelo.Toplista):

    bg = pygame.image.load('./mainIMG/bg.png')

    ttoplista = rendszer.listaki()
    toplista = []

    print(toplista)

    for x in range(len(ttoplista)):
        if ttoplista[x][0] == -1: continue
        toplista.append(ttoplista[x])
    
    del ttoplista

    print(toplista)

    isMain = True
    while isMain:
        display.fill((0,0,0))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return

        display.blit(bg, [0,0])


        dx = 50
        dy = 50
        display.blit(load.Text('Toplista:',50).text,(dx,dy))
        dy+=60
        if len(toplista)==0:
            display.blit(load.Text('De hisz még nem is játszottál...',35).text, (dx,dy))
        for i in range(len(toplista)):
            act = load.Text(f'{i+1}. {toplista[i][1]} - {toplista[i][0]}',35)
            display.blit(act.text, (dx,dy))
            dy += 40
        display.blit(load.Text('ESC - Visszalépés',40).text, (20,550))
        pygame.display.update()
        clock.tick(60)
    return