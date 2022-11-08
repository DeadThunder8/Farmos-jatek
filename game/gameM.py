import pygame
import sys
import load
import plantloader

def main(display:pygame.Surface,clock:pygame.time.Clock):

    bg = load.BackGround('./game/img/bg.png')
    bgdisplay = pygame.sprite.Group()
    bg.add(bgdisplay)

    
    #alsó megjelenítőszint
    render = pygame.sprite.Group()

    #felső megjelenítőszint
    cover = pygame.sprite.Group()

    #tesztzöldség létrehozása
    retek = plantloader.Retek('r0')
    retek.get().add(cover)

    #kert létrehozása
    kert = load.Kert(3,3)
    kert.addall(render)
    kert.draw((270,130), 10)

    #feladatpanel létrehozása
    fpanel = load.Feladatpanel('./game/img/feladatpanel.png')
    render.add(fpanel)

    #eszközpanel létrehozása
    epanel = load.Eszkozpanel('./game/img/eszkozpanel.png')
    render.add(epanel)

    #boltpanel
    bpanel = load.Boltpanel('./game/img/bolt.png')
    render.add(bpanel)

    isMain = True
    while isMain:
        mouse = pygame.mouse.get_pos()
        #pre
        display.fill((0,0,0))
        render.update()
        bgdisplay.update()
        bgdisplay.draw(display)

        retek.move(mouse)
        if retek.hover(mouse) and kert.hover(mouse,(1,1)):
            retek.move(kert.get(1,1).rect.center)




        #input
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isMain = False

        #post
        render.draw(display)
        cover.draw(display)
        pygame.display.update()
        clock.tick(60)
    return
