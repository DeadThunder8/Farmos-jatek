import pygame
import random
import plantloader
import load

"""
Megjelenítés
"""

class FeladatIkon(pygame.sprite.Sprite):
    def __init__(self, typer:str) -> None:
        super().__init__()
        if typer == 'repa':
            self.image = pygame.image.load('./game/feladat/repa.png')
        elif typer == 'retek':
            self.image = pygame.image.load('./game/feladat/retek.png')
        elif typer == 'buza':
            self.image = pygame.image.load('./game/feladat/buza.png')
        elif typer == 'kukorica':
            self.image = pygame.image.load('./game/feladat/kukorica.png')
        elif typer == 'paradicsom':
            self.image = pygame.image.load('./game/feladat/paradicsom.png')
        else: raise ValueError('Érvénytelen gyümi...')

        self.rect = self.image.get_rect()

    def move(self,pos:tuple[int,int]):
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Feladat():
    def __init__(self, inp:list[(str,int),(str,int),(str,int)], pont:int) -> None:
        self.score = pont

        self.map = inp

        self.disply = []

        for x in self.map:
            self.disply.append(FeladatIkon(x[0]))
          
    def __str__(self) -> str:
        ki = ''
        for x in self.map:
            ki+=str(x)+'\n'
        return ki

    def eladas(self, gyumi:str,pont) -> bool:
        for x in self.map:
            if x[0] == gyumi:
                x[1]-=1
                if gyumi == 'repa': pont.add(1)
                if gyumi == 'retek': pont.add(2)
                if gyumi == 'buza': pont.add(3)
                if gyumi == 'kukorica': pont.add(4)
                if gyumi == 'paradicsom': pont.add(5)
                return True
        
        return False

    def ell(self)->bool:
        for x in self.map:
            if x[1]<=0:
                self.map.pop(self.map.index(x))
        if self.map == []: return True
        return False 

    def addAll(self, group:pygame.sprite.Group):
        group.empty()
        for x in self.disply:
            group.add(x)
    
    def killAll(self):
        for x in self.disply:
            x.kill()

    def elhelyez(self,group:pygame.sprite.Group,fpanel:load.Feladatpanel):
        tk = 6

        elemek = group.sprites()

        sx = fpanel.rect.x + tk
        sy = fpanel.rect.y + tk

        for x in elemek:
            x.move((sx,sy))
            sx += 30 + tk
            if sx >= fpanel.rect.x + tk + 4*(30+tk):
                sx = sx = fpanel.rect.x + tk
                sy += 30 + tk

    def eliminate(self, group:pygame.sprite.Group):
        self.killAll()
        self.disply = []
        for x in self.map:
            for _ in range(x[1]):
                self.disply.append(FeladatIkon(x[0]))
        self.addAll(group)
    
        
"""
Generálás
"""

def ujfeladat(nehezseg:int)->Feladat:
    """
    bekér egy nehézségi szintet

    létrehoz egy véletlenszerű feladatot, a nehézséget kielégítve
    """
    if nehezseg < 1 : raise ValueError('Ez a játék nem lehet 0 vagy kisebb nehézségű!')
    if nehezseg > 110: 
        nehezseg %= 110
        if nehezseg < 70: nehezseg = 100

    helper = random.randint(0,10)

    if helper >= 7 and nehezseg > 7: nehezseg = 6

    print(nehezseg)

    kovetelmeny = (1,2,3,4,5,6,7,8,9) #egyszerre termelendő zöldségek nehézségi sorrenben
    zoldsegek = ('repa','retek','buza','kukorica','paradicsom') #nehézségi sorrendben a zöldségek
    #               1      2      3        4            5
    perdarabszam = (1,2,3,4,5,6,7,8,9) #egy termény mennyisége

    actneh = 0 #a feladat jelenlegi nehézsége

    
    while actneh < nehezseg or actneh > nehezseg + 2:
        actneh = 0
        lista = []
        kov = kovetelmeny[random.randint(0,len(kovetelmeny)-1)]
        actneh += kov
        for _ in range(kov):
            zold = zoldsegek[random.randint(0,len(zoldsegek)-1)]
            perd = perdarabszam[random.randint(0,len(perdarabszam)-1)]
            actneh+=perd
            if zold == 'repa': actneh+=1
            if zold == 'retek': actneh+=2
            if zold == 'buza': actneh+=3
            if zold == 'kukorica': actneh+=4
            if zold == 'paradicsom': actneh+=5
            lista.append([zold,perd])

    return Feladat(lista,actneh)

