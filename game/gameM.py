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

    #bolt feletti megjelenítő szint
    belemek = pygame.sprite.Group()

    #Növény megjelenítő szint
    novenykek = pygame.sprite.Group()

    #felső megjelenítőszint
    cover = pygame.sprite.Group()


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

    #boltelemek
    brep = load.Boltbutton('repa', (bpanel.rect.left+30, bpanel.rect.top+30))
    bret = load.Boltbutton('retek', (bpanel.rect.left+130, bpanel.rect.top+30))
    bbuz = load.Boltbutton('buza', (bpanel.rect.left+30, bpanel.rect.top+130))
    bkuk = load.Boltbutton('kukorica', (bpanel.rect.left+130, bpanel.rect.top+130))
    bpar = load.Boltbutton('paradicsom', (bpanel.rect.left+80, bpanel.rect.top+230))

    belemek.add(bpar)
    belemek.add(brep)
    belemek.add(bret)
    belemek.add(bbuz)
    belemek.add(bkuk)


    active = None


    isMain = True
    while isMain:
        mouse = pygame.mouse.get_pos()
        event = pygame.event.get()
        #pre
        display.fill((0,0,0))
        render.update()
        belemek.update()
        novenykek.update()
        bgdisplay.update()
        bgdisplay.draw(display)

        #input
        for ev in event:
            if ev.type == pygame.QUIT:
                sys.exit()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    isMain = False
        
        # Vásárlást lebonyolító rész

        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

                #répa
                if brep.hover(mouse):
                    active = plantloader.Repa('repa')
                    active.get().add(cover)
                    active.dragged = 1
                #retek
                if bret.hover(mouse):
                    active = plantloader.Retek('retek')
                    active.get().add(cover)
                    active.dragged = 1
                #buza
                if bbuz.hover(mouse):
                    active = plantloader.Buza('buza')
                    active.get().add(cover)
                    active.dragged = 1
                #paradicsom
                if bpar.hover(mouse):
                    active = plantloader.Paradicsom('paradicsom')
                    active.get().add(cover)
                    active.dragged = 1
                #kukorica
                if bkuk.hover(mouse):
                    active = plantloader.Kukorica('kukorica')
                    active.get().add(cover)
                    active.dragged = 1

            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if type(active) == plantloader.Kukorica:
                    active.dragged == 0
                    active.get().kill()
                    buy(mezokeres(active.get().rect.center,kert),active,kert)
                    active = None

                if type(active)==plantloader.Paradicsom:
                    active.dragged = 0
                    active.get().kill()
                    buy(mezokeres(active.get().rect.center,kert),active,kert)
                    active = None

                if type(active)==plantloader.Buza:
                    active.dragged == 0
                    active.get().kill()
                    buy(mezokeres(active.get().rect.center,kert),active,kert)
                    active = None

                if type(active)==plantloader.Repa:
                    active.dragged = 0
                    active.get().kill()
                    buy(mezokeres(active.get().rect.center,kert),active,kert)
                    active = None
                
                if type(active)==plantloader.Retek:
                    active.dragged = 0
                    active.get().kill()
                    buy(mezokeres(active.get().rect.center,kert),active,kert)
                    active = None

        #aktív objektum egérhez való mozgatása
        try: 
            active.move(mouse)
        except:pass

        #kert frissítése
        kert.update(novenykek)

        #post
        render.draw(display)
        belemek.draw(display)
        novenykek.draw(display)
        cover.draw(display)

        pygame.display.update()
        clock.tick(60)
    return

def mezokeres(pos, kert:load.Kert):
    return kert.cellakeres(pos)

def buy(pos:tuple[int, int],active:plantloader.Novenyinit,kert:load.Kert):
    if pos == None: 
        return

    parcella = kert.get(pos[0],pos[1])
    tip = type(active)

    if tip == plantloader.Repa:
        parcella.ultet(plantloader.Repa('réépaaa'))
    if tip == plantloader.Retek:
        parcella.ultet(plantloader.Retek('reteeeeeeeek'))
    if tip == plantloader.Buza:
        parcella.ultet(plantloader.Buza('búúúzaá'))
    if tip == plantloader.Kukorica:
        parcella.ultet(plantloader.Kukorica('kukii'))
    if tip == plantloader.Paradicsom:
        parcella.ultet(plantloader.Paradicsom('nagy piros izé'))

def placeBuy():
    pass
