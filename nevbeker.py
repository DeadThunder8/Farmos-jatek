import pygame
import load
import sys

class Alap(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface([410,50])

        self.image.fill((10,100,255))

        self.rect = self.image.get_rect()


def main(display:pygame.Surface,clock:pygame.time.Clock) -> str:

    bg = pygame.image.load('./mainIMG/bg.png')

    alap = Alap()
    alapg = pygame.sprite.Group()
    alap.rect.x = 10
    alap.rect.y = 70

    nev = load.Text('Név:')

    adat = load.Text('',42)

    alap.add(alapg)

    isMain = True
    while isMain:
        alapg.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isMain = False
                pygame.quit()
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE: return ''
                elif ev.key == pygame.K_RETURN: return adat.textv
                elif ev.key == pygame.K_BACKSPACE:
                    adat = load.Text(adat.textv[:-1],42)
                else: adat = load.Text(adat.textv + ev.unicode,42)
                if len(adat.textv)>len('Ren Fangrun Superstar'): adat = load.Text(adat.textv[:-1],42)

        display.blit(bg, [0,0])

        display.blit(nev.text, (nev.rect.x,nev.rect.y))

        alapg.draw(display)

        display.blit(adat.text, (15,75))
        
        pygame.display.update()
        clock.tick(60)
    return