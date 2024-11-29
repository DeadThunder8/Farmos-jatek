from random import shuffle

import pygame
import plantloader

WHITE = (255,255,255)

class BackGround(pygame.sprite.Sprite):
    def __init__(self,path) -> None:
        super().__init__()
        #transzparens bigyó létrehozása
        self.image = pygame.Surface([0,0])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)


        self.image = pygame.image.load(path)

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0


#Kert, parcellák
class Parcella(pygame.sprite.Sprite):
    def __init__(self, path, pathBlocked, id) -> None:
        super().__init__()
        self.id = id
        self.image = pygame.Surface([0,0])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        self.noveny = None

        self.blocked:bool = False
        self.defaultImg = pygame.image.load(path)
        self.blockedImg = pygame.image.load(pathBlocked)

        try: self.image = self.defaultImg
        except: self.image = pygame.draw.rect(self.image, (255,0,255), [0,0,30,30])

        self.planted = 0

        self.rect = self.image.get_rect()
    
    def ultet(self, noveny:plantloader.Novenyinit):
        if type(noveny) not in [plantloader.Repa,plantloader.Buza,plantloader.Retek,plantloader.Kukorica,plantloader.Paradicsom]: return None
        if self.noveny is not None or self.blocked:return None
        self.noveny = noveny
        self.noveny.move(self.rect.center)

    def block(self):
        if self.noveny is not None: return False

        self.blocked = True
        self.image = self.blockedImg
        return True

    def unBlock(self):
        self.blocked = False
        self.image = self.defaultImg

    def setId(self, newID):
        self.id = newID

class Kert():
    def __init__(self,sor:int,oszlop:int) -> None:
        self.sheet:list[list[Parcella]] = []
        self.blockOrder:list[Parcella] = []
        self.x = 0
        self.y = 0
        for _ in range(sor):
            self.sheet.append([])
        
        for x in range(len(self.sheet)):
            for y in range(oszlop):
                actParcella = Parcella('./game/img/fold.png', './game/img/foldBlocked.png' ,(x,y))
                self.sheet[x].append(actParcella)
                self.blockOrder.append(actParcella)


    def update(self, group:pygame.sprite.Group):
        """
        felfrissíti a kert alá rendelt grafikus elemeket
        """
        group.empty()

        for x in range(len(self.sheet)):
            for y in range(len(self.sheet[x])):
                if self.getnoveny((x,y)) == None: continue
                self.getnoveny((x,y)).get().add(group)
                
        
    def getnoveny(self, cord)->plantloader.Novenyinit:
        return self.get(cord[0],cord[1]).noveny

        
    def get(self, sor:int,oszlop:int)->Parcella:
        """
        Kikeresi a kert adott mezőjét
        """
        try: return  self.sheet[sor][oszlop]
        except: return None

    def getAllNoveny(self)->list[plantloader.Novenyinit]:
        ki = []
        for x in range(len(self.sheet)):
            for y in range(len(self.sheet[x])):
                ki.append(self.sheet[x][y].noveny)
        return ki

    def cellakeres(self, pos):
        for x in range(len(self.sheet)):
            for y in range(len(self.sheet[x])):
                if self.hover(pos, (x,y)):
                    return (x,y)
        return None

    def addall(self, group:pygame.sprite.Group):
        group.empty()
        for x in self.sheet:
            for y in x:
                group.add(y)
    
    def draw(self, position:tuple,space:int):
        self.x = position[0]
        self.y = position[1]
        px = self.x
        py = self.y
        for x in self.sheet:
            for y in range(len(x)):
                x[y].rect.x = px
                x[y].rect.y = py
                px += 140 + space
            px = self.x
            py += 140 + space

    def hover(self,pos:tuple,loc:tuple):
        if pos[0] < self.get(loc[0],loc[1]).rect.left or pos[0] > self.get(loc[0],loc[1]).rect.right or pos[1] < self.get(loc[0],loc[1]).rect.top or pos[1] > self.get(loc[0],loc[1]).rect.bottom: return False
        return True

    def blockParcella(self, taskAmnt:int, blockCount:int):
        if taskAmnt == 0: return

        if taskAmnt > 9: taskAmnt = 9
        blockNumber = (9 - taskAmnt)
        if blockNumber < blockCount: blockNumber = blockCount

        self.unblockAll()

        for tile in self.blockOrder:
            if blockNumber == 0: break
            if tile.block():
                blockNumber-=1

    def unblockAll(self):
        for x in self.sheet:
            for tile in x:
                tile.unBlock()

    def shuffle(self):
        shuffle(self.blockOrder)


#Panelek

class Feladatpanel(pygame.sprite.Sprite):
    def __init__(self, path:str) -> None:
        super().__init__()
        self.image = pygame.Surface([0,0])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        self.image = pygame.image.load(path)

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 75

class Eszkozpanel(pygame.sprite.Sprite):
    def __init__(self, path:str) -> None:
        super().__init__()
        self.image = pygame.Surface([0,0])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        self.rect.right = 1040
        self.rect.bottom = 600

class Boltpanel(pygame.sprite.Sprite):
    def __init__(self, path:str) -> None:
        super().__init__()

        self.image = pygame.Surface([0,0])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        self.image = pygame.image.load(path)

        self.rect = self.image.get_rect()

        self.rect.right = 1000
        self.rect.centery = 300

class Boltbutton(pygame.sprite.Sprite):
    def __init__(self, typex:str, loc:tuple):
        super().__init__()
        self.type = typex

        self.image = pygame.Surface([0,0])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        if type(typex) != str: raise TypeError()

        if typex == 'paradicsom':
            self.image = pygame.image.load('./game/img/novenyek/icons/paradicsom.png')
        elif typex == 'repa':
            self.image = pygame.image.load('./game/img/novenyek/icons/repa.png')
        elif typex == 'buza':
            self.image = pygame.image.load('./game/img/novenyek/icons/buza.png')
        elif typex == 'retek':
            self.image = pygame.image.load('./game/img/novenyek/icons/retek.png')
        elif typex == 'kukorica':
            self.image = pygame.image.load('./game/img/novenyek/icons/kukorica.png')
        else: raise ValueError('A megadott tipus nincs az adatbázisban')

        self.rect = self.image.get_rect()

        self.rect.x = loc[0]
        self.rect.y = loc[1]

    def replace(self,loc:tuple):
        self.rect.x = loc[0]
        self.rect.y = loc[1]

    def hover(self, mouse:tuple):
        if mouse[0] > self.rect.right or mouse[0] < self.rect.left: return False
        if mouse[1] < self.rect.top or mouse[1] > self.rect.bottom: return False
        return True

class Text():
    def __init__(self, text:str, size=72) -> None:
        font = pygame.font.SysFont('Calibri', size, True)
        self.text = font.render(text, True, (10,10,10))

        self.textv = text

        self.rect = self.text.get_rect()





