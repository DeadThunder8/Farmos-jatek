import pygame

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
class Kert():
    def __init__(self,sor:int,oszlop:int) -> None:
        self.sheet = []
        self.x = 0
        self.y = 0
        for _ in range(sor):
            self.sheet.append([])
        
        for x in range(len(self.sheet)):
            for y in range(oszlop):
                self.sheet[x].append(Parcella('./game/img/fold.png',(x,y)))

        
        
    def get(self, sor:int,oszlop:int)->pygame.sprite.Sprite:
        """
        Kikeresi a kert adott mezőjét
        """
        try: return  self.sheet[sor][oszlop]
        except: return None
    
    def addall(self, group:pygame.sprite.Group):
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
      
class Parcella(pygame.sprite.Sprite):
    def __init__(self, path,id) -> None:
        super().__init__()
        self.id = id
        self.image = pygame.Surface([0,0])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        try: self.image = pygame.image.load(path)
        except: self.image = pygame.draw.rect(self.image, (255,0,255), [0,0,30,30])

        self.planted = 0

        self.rect = self.image.get_rect()

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

        self.rect.right = 1000
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


