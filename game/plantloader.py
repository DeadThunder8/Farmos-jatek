import pygame

KEY = (0,0,0)

class Novenyinit():
    def __init__(self,id:str,sheet:list) -> None:
        self.id = id
        self.act = 0 #max->5
        self.dragged = False

        self.map = (
        Allapot(sheet[0]),
        Allapot(sheet[1]),
        Allapot(sheet[2]),
        Allapot(sheet[3]),
        Allapot(sheet[4]),
        Allapot(sheet[5])
        )

    def get(self)->pygame.sprite.Sprite: 
        if self.act > 5: return None
        return self.map[self.act]

    def move(self,pos:tuple):
        self.get().rect.center = pos

    def drag(self,pos):
        if self.dragged:
            self.move(pos)
    
    def set(self,index:int):
        groups = self.get().groups()
        self.get().kill()

        pos = self.get().rect.center
        
        self.act = index
        for x in groups:
            x.add(self.get())
        self.get().rect.center = pos
    
    def place():pass

    def hover(self,pos:tuple):
        if pos[0] < self.get().rect.left or pos[0] > self.get().rect.right or pos[1] < self.get().rect.top or pos[1] > self.get().rect.bottom: return False
        return True
        
        


class Paradicsom(Novenyinit):
    def __init__(self,id:str) -> None:
        self.sheet = [
            './game/img/novenyek/paradicsom0.png',
            './game/img/novenyek/paradicsom1.png',
            './game/img/novenyek/paradicsom2.png',
            './game/img/novenyek/paradicsom3.png',
            './game/img/novenyek/paradicsom4.png',
            './game/img/novenyek/paradicsom5.png'
            ]
        super().__init__(id,self.sheet)

class Repa(Novenyinit):
    def __init__(self, id: str) -> None:
        self.sheet = [
            './game/img/novenyek/repa0.png',
            './game/img/novenyek/repa1.png',
            './game/img/novenyek/repa2.png',
            './game/img/novenyek/repa3.png',
            './game/img/novenyek/repa4.png',
            './game/img/novenyek/repa5.png'                        
        ]
        super().__init__(id, self.sheet)

class Buza(Novenyinit):
    def __init__(self, id: str) -> None:
        self.sheet = [
            './game/img/novenyek/buza0.png',
            './game/img/novenyek/buza1.png',
            './game/img/novenyek/buza2.png',
            './game/img/novenyek/buza3.png',
            './game/img/novenyek/buza4.png',
            './game/img/novenyek/buza5.png'
        ]
        super().__init__(id, self.sheet)

class Retek(Novenyinit):
    def __init__(self, id: str) -> None:
        self.sheet = [
            './game/img/novenyek/retek0.png',
            './game/img/novenyek/retek1.png',
            './game/img/novenyek/retek2.png',
            './game/img/novenyek/retek3.png',
            './game/img/novenyek/retek4.png',
            './game/img/novenyek/retek5.png'
        ]
        super().__init__(id, self.sheet)

class Kukorica(Novenyinit):
    def __init__(self, id: str) -> None:
        self.sheet = [
            './game/img/novenyek/kukorica0.png',
            './game/img/novenyek/kukorica1.png',
            './game/img/novenyek/kukorica2.png',
            './game/img/novenyek/kukorica3.png',
            './game/img/novenyek/kukorica4.png',
            './game/img/novenyek/kukorica5.png'
        ]
        super().__init__(id, self.sheet)

class Allapot(pygame.sprite.Sprite):
    def __init__(self, path:str)->None:
        super().__init__()
        self.image = pygame.Surface([0,0])
        self.image.fill(KEY)
        self.image.set_colorkey(KEY)

        self.image = pygame.image.load(path)

        self.rect = self.image.get_rect()