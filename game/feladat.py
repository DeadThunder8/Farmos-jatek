import pygame
import random
import plantloader

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
            self.image = pygame.image.load('./game/feladat/tomato.png')
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

    def eladas(self, gyumi:str) -> bool:
        for x in self.map:
            if x[0] == gyumi:
                x[1]-=1
                print(self.map)
                return True
        
        return False

    def ell(self)->bool:
        for x in self.map:
            if x[1]<=0:
                self.map.pop(self.map.index(x))
                print(self.map)
        if self.map == []: return True
        return False 

    def addAll(self, group:pygame.sprite.Group):
        for x in self.disply:
            group.add(x)
    
    def killAll(self):
        for x in self.disply:
            x.kill()

    def elhelyez(self, boltpanel:pygame.sprite.Sprite):
        pass


    def eliminate(self, group:pygame.sprite.Group):
        self.disply = []
        for x in self.map:
            self.disply.append(FeladatIkon(x[0]))
        self.killAll()
        self.addAll(group)
        elhelyez()
    
        
"""
Generálás
"""

def ujfeladat(nehezseg:int)->Feladat:
    """
    bekéri egy nehézségi szintet

    létrehoz egy véletlenszerű feladatot, a nehézséget kielégítve
    """
    if nehezseg < 1 : raise ValueError('Ez a játék nem lehet 0 vagy kisebb nehézségű!')
    if nehezseg > 30: nehezseg %= 30

    helper = random.randint(0,10)

    if helper >= 7 and nehezseg > 7: nehezseg = 3

    kovetelmeny = (1,2,3,4,5) #egyszerre termelendő zöldségek nehézségi sorrenben
    zoldsegek = ('repa','retek','buza','kukorica','paradicsom') #nehézségi sorrendben a zöldségek
    #               1      2      3        4            5
    perdarabszam = (1,2,3,4,5,6) #egy termény mennyisége

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

