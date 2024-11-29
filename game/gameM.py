import pygame
import sys
import load
import plantloader
import eszkozok
import feladat

class Timer():
    """
    Fő időzítő...
    """
    def __init__(self) -> None:
        self.time = 0
        self.remaining = 30
        self.display = load.Text(str(self.remaining-self.time))

    def get(self):
        return self.remaining - self.time
    
    def setOut(self):
        self.display = load.Text(str(self.remaining-self.time))

    def move(self,pos:tuple[int,int]):
        self.display.rect.x = pos[0]
        self.display.rect.y = pos[1]
        self.setOut()

    def timerSet(self, rem:int, globTime:int=0):
        self.time = globTime // 1000
        self.remaining = self.time + 30

        self.setOut()

    def runTimer(self, globTime:int)->bool:
        self.time = globTime // 1000
        act = False
        if self.time >= self.remaining:
            act = True
        self.setOut()
        return act
    
    def add(self, sec:int):
        self.remaining+=sec
        self.setOut()

class Pontszam():
    def __init__(self) -> None:
        self.pont = 0
        self.display = load.Text(str(self.pont))

    def setOut(self): 
        self.display = load.Text(str(self.pont))

    def get(self):
        return self.pont
    
    def add(self, ertek:int):
        self.pont += ertek
        self.setOut()

    def move(self,pos:tuple[int,int]):
        self.display.rect.x = pos[0]
        self.display.rect.y = pos[1]
        self.setOut()
        

def main(display:pygame.Surface,clock:pygame.time.Clock):


    bg = load.BackGround('./game/img/bg.png')
    bgdisplay = pygame.sprite.Group()
    bg.add(bgdisplay)

    #Időzítő létrehozása
    timer = Timer()

    #pontszámláló
    pont = Pontszam()
    
    
    #alsó megjelenítőszint
    render = pygame.sprite.Group()

    # kert megjelenítő szint
    kertRender = pygame.sprite.Group()

    #bolt feletti megjelenítő szint
    belemek = pygame.sprite.Group()

    #feladat megjelenítő szint
    felemek = pygame.sprite.Group()

    #Növény megjelenítő szint
    novenykek = pygame.sprite.Group()

    #Index megjelenítő szint
    indexek = pygame.sprite.Group()

    #felső megjelenítőszint
    cover = pygame.sprite.Group()


    #kert létrehozása
    kert = load.Kert(3,3)
    kert.addall(kertRender)
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

    #nyeső
    nyeso = eszkozok.Nyeso()
    nyeso.add(cover)
    nyeso.rect.x = epanel.rect.x + 135
    nyeso.rect.y = epanel.rect.y + 5
    nyeso.helymentes()

    #feladatok
    nehezseg = 1
    actfeladat = feladat.ujfeladat(nehezseg)
    actfeladat.addAll(felemek)

    active = None

    isMain = True
    timer.timerSet(30,pygame.time.get_ticks())
    while isMain:
        pont.display.rect.right = 1000
        mouse = pygame.mouse.get_pos()
        event = pygame.event.get()
        time = pygame.time.get_ticks()
        #pre
        display.fill((0,0,0))
        indexek.update()
        indexek.empty()
        render.update()
        belemek.update()
        felemek.update()
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
                    return pont.get()
        
        # Vásárlást lebonyolító rész

        for ev in event:
            if active == None and ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

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

            if (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 ):
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
            if (ev.type == pygame.MOUSEBUTTONDOWN and kapa.hover(mouse) and ev.button == 1) or (active == None and ev.type == pygame.KEYDOWN and ev.key == pygame.K_w):
                active = kapa
            if (ev.type == pygame.MOUSEBUTTONUP and active == kapa and ev.button == 1)  or (active == kapa and ev.type == pygame.KEYUP and ev.key == pygame.K_w):
                kapal(mezokeres(kapa.rect.center,kert),kert)
                kapa.visszateres()
                active = None
        #locsolást lebonyolító rész

        for ev in event:
            #kanna kijelölése
            if (ev.type == pygame.MOUSEBUTTONDOWN and kanna.hover(mouse) and ev.button == 1) or (active == None and ev.type == pygame.KEYDOWN and ev.key == pygame.K_q):
                active = kanna
            if (ev.type == pygame.MOUSEBUTTONUP and active == kanna and ev.button == 1) or (active == kanna and ev.type == pygame.KEYUP and ev.key == pygame.K_q):
                locsol(mezokeres(kanna.rect.center,kert),kert)
                kanna.visszateres()
                active = None

        #aratást lebonyolító rész
        for ev in event:
            #nyisz nyisz kijelölése
            if (ev.type == pygame.MOUSEBUTTONDOWN and nyeso.hover(mouse) and ev.button == 1) or (active == None and ev.type == pygame.KEYDOWN and ev.key == pygame.K_e):
                active = nyeso
            if (ev.type == pygame.MOUSEBUTTONUP and active == nyeso and ev.button == 1) or (active == nyeso and ev.type == pygame.KEYUP and ev.key == pygame.K_e):
                if arat(mezokeres(nyeso.rect.center,kert),kert,actfeladat,pont): 
                    actfeladat.eliminate(felemek)
                    timer.add(2)
                nyeso.visszateres()
                active = None

        #feladat frissítés
        if actfeladat.ell(kert):
            nehezseg += 1
            timer.add(30 * actfeladat.blockCount if actfeladat.blockCount > 0 else 1)
            if timer.get() > 100: 
                nehezseg += 2
                pont.add(30)
            if timer.get() > 200:
                nehezseg += 5
                pont.add(5*20)
                
            actfeladat = feladat.ujfeladat(nehezseg)
            actfeladat.eliminate(felemek)
            kert.shuffle()

        #feladatok frissítése

        actfeladat.elhelyez(felemek,fpanel)
        
        #aktív objektum egérhez való mozgatása
        try:active.move(mouse)
        except:pass

        #kert frissítése
        timer.runTimer(time)
        if timer.get() <= 0: return pont.get()
        novenyNoves(kert, indexek)
        kert.update(novenykek)
        kert.addall(kertRender)

        #rajzolás szintenként
        render.draw(display)
        kertRender.draw(display)
        belemek.draw(display)
        felemek.draw(display)
        novenykek.draw(display)
        indexek.draw(display)
        display.blit(timer.display.text, timer.display.rect)
        display.blit(pont.display.text, pont.display.rect)
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
        parcella.ultet(plantloader.Repa('repa'))
    if tip == plantloader.Retek:
        parcella.ultet(plantloader.Retek('retek'))
    if tip == plantloader.Buza:
        parcella.ultet(plantloader.Buza('buza'))
    if tip == plantloader.Kukorica:
        parcella.ultet(plantloader.Kukorica('kukorica'))
    if tip == plantloader.Paradicsom:
        parcella.ultet(plantloader.Paradicsom('paradicsom'))

def novenyNoves(kert:load.Kert, group:pygame.sprite.Group):
    lista = kert.getAllNoveny()
    ido = pygame.time.get_ticks()

    for x in lista:
        if x == None: continue
        if x.growinterval == None: x.growinterval = idoIgeny(x)

        if x.act == 4: aratojel(x, group)

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

    repa = (1000,2000,2000,2000,10000)
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

def arat(pos:tuple,kert:load.Kert,task:feladat.Feladat,pont:Pontszam):
    if pos == None:return
    noveny = kert.get(pos[0],pos[1]).noveny
    if noveny == None: return
    if noveny.act != 4: return

    ki = task.eladas(noveny.id,pont)
    kapal(pos,kert)
    return ki

def aratojel(noveny:plantloader.Novenyinit,group:pygame.sprite.Group):
    pos = (noveny.get().rect.x,noveny.get().rect.y)
    nyisz = eszkozok.Aratojel()

    nyisz.rect.x = pos[0]
    nyisz.rect.y = pos[1]

    group.add(nyisz)

    