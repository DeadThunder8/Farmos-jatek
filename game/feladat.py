import pygame
import random
import plantloader

"""
Megjelenítés
"""

class Feladat(pygame.sprite.Sprite):
    def __init__(self, inp:list[(str,int),(str,int),(str,int)], pont:int) -> None:
        super().__init__()
        self.image = pygame.image.load('./game/feladat/alap.png')
        self.rect = self.image.get_rect()
        self.score = pont

        self.map = inp
        
        

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

