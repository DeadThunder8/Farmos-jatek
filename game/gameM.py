import pygame
import sys
import load
import plantloader
import eszkozok

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

    #Index megjelenítő szint
    indexek = pygame.sprite.Group()

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

    #eszközök létrehozása
    #kanna
    kanna = eszkozok.Khanna()
    kanna.add(cover)
    kanna.rect.x = epanel.rect.x + 5
    kanna.rect.y = epanel.rect.y + 5
    kanna.helymentes()

    #kapa
    kapa = eszkozok.Kapa()
    kapa.add(cover)
    kapa.rect.x = epanel.rect.x + 70
    kapa.rect.y = epanel.rect.y + 5
    kapa.helymentes()
    

    active = None

    isMain = True
    while isMain:
        mouse = pygame.mouse.get_pos()
        event = pygame.event.get()
        #pre
        display.fill((0,0,0))
        indexek.update()
        indexek.empty()
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

        #kikapálás
        for ev in event:
            if ev.type == pygame.MOUSEBUTTONDOWN and kapa.hover(mouse) and ev.button == 1:
                active = kapa
            if ev.type == pygame.MOUSEBUTTONUP and active == kapa and ev.button == 1:
                kapal(mezokeres(kapa.rect.center,kert),kert)
                kapa.visszateres()
                active = None
        #locsolást lebonyolító rész
        for ev in event:
            #kanna kijelölése
            if ev.type == pygame.MOUSEBUTTONDOWN and kanna.hover(mouse) and ev.button == 1:
                active = kanna
            if ev.type == pygame.MOUSEBUTTONUP and active == kanna and ev.button == 1:
                locsol(mezokeres(kanna.rect.center,kert),kert)
                kanna.visszateres()
                active = None

        #aktív objektum egérhez való mozgatása
        try:active.move(mouse)
        except:pass

        #kert frissítése
        novenyNoves(kert, indexek)
        kert.update(novenykek)

        #rajzolás szintenként
        render.draw(display)
        belemek.draw(display)
        novenykek.draw(display)
        indexek.draw(display)
        cover.draw(display)

        #post
        pygame.display.update()
        clock.tick(60)
    return

def mezokeres(pos, kert:load.Kert):
    return kert.cellakeres(pos)

def buy(pos:tuple[int, int],active:plantloader.Novenyinit,kert:load.Kert):
    if pos == None:return

    parcella = kert.get(pos[0],pos[1])
    tip = type(active)

    if tip == plantloader.Repa:
        parcella.ultet(plantloader.Repa('réépaaa'))
    if tip == plantloader.Retek:
        parcella.ultet(plantloader.Retek('reteeeeeeeek'))
    if tip == plantloader.Buza:
        parcella.ultet(plantloader.Buza('búúúzaá'))
    if tip == plantloader.Kukorica:
        parcella.ultet(plantloader.Kukorica('kukoric'))
    if tip == plantloader.Paradicsom:
        parcella.ultet(plantloader.Paradicsom('nagy piros izé'))

def novenyNoves(kert:load.Kert, group:pygame.sprite.Group):
    lista = kert.getAllNoveny()
    ido = pygame.time.get_ticks()

    for x in lista:
        if x == None: continue
        if x.growinterval == None: x.growinterval = idoIgeny(x)
        if x.locsolva == False: 
            x.water = vizIgeny(x)

        if x.water == True:
            x.time = ido
            vizcsepp(x, group)

        if x.growinterval == None: continue
        if ido >= x.time + x.growinterval: 
            x.grow()
            x.locsolva = False
            x.time = ido
            x.growinterval = idoIgeny(x)

def idoIgeny(objektum:plantloader.Novenyinit):
    """
    Ez a függvény megmondja adott növényről, mennyi időt kell várni a következő növésig/lerohadásig...
    """
    act = objektum.act
    if act > 4: return None

    #Az itt felsorolt adatoknak köze sincs a valósághoz, úgy vannak kitalálva, hogy kellemetlenséget okozzanak a játékosnak.
    repa = (1000,2000,2000,1000,10000)
    retek = (2000,3000,3000,2000,9000)
    buza = (3000,5000,5000,5000,7500)
    kukorica = (2000,3000,6000,2000,5000)
    paradicsom = (3000,4000,7000,3000,4000)

    if type(objektum)==plantloader.Repa:
        return repa[act]

    if type(objektum)==plantloader.Retek:
        return retek[act]

    if type(objektum)==plantloader.Buza:
        return buza[act]

    if type(objektum)==plantloader.Kukorica:
        return kukorica[act]

    if type(objektum)==plantloader.Paradicsom:
        return paradicsom[act]

    raise TypeError('Ez nem növény...')

def vizIgeny(objektum:plantloader.Novenyinit):
    """
    Ez a függvény megmondja, hogy a növényt kell-e locsolni, hogy tovább nőhessen
    """

    act = objektum.act
    if act > 4: return False

    repa = (True,False,False,False,False)
    retek = (True,True,False,False,False)
    buza = (False,False,True,True,False)
    kukorica = (True,True,False,True,False)
    paradicsom = (True,True,True,True,False)

    if type(objektum) == plantloader.Repa: return repa[act]
    if type(objektum) == plantloader.Retek: return retek[act]
    if type(objektum) == plantloader.Buza: return buza[act]
    if type(objektum) == plantloader.Kukorica: return kukorica[act]
    if type(objektum) == plantloader.Paradicsom: return paradicsom[act]

    raise TypeError('Ez nem növény...')

def vizcsepp(obj:plantloader.Novenyinit, group:pygame.sprite.Group):
    pos = (obj.get().rect.x,obj.get().rect.y)
    csepp = eszkozok.Vizcsepp()

    csepp.rect.x = pos[0]
    csepp.rect.y = pos[1]

    group.add(csepp)

def locsol(pos:tuple,kert:load.Kert):
    if pos == None: return
    if kert.get(pos[0],pos[1]).noveny == None: return
    if kert.get(pos[0],pos[1]).noveny.water == True: 
        kert.get(pos[0],pos[1]).noveny.water = False
        kert.get(pos[0],pos[1]).noveny.locsolva = True

def kapal(pos:tuple,kert:load.Kert):
    if pos == None: return
    kert.get(pos[0],pos[1]).noveny = None
    