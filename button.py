import pygame

WHITE = (255,255,255)

class MenuButton():
    def __init__(self, s1:list, s2:list) -> None:
        self.act = 0

        self.x = 50
        self.y = 50

        self.s1 = Button(s1[0],s1[1],s1[2])
        self.s2 = Button(s2[0],s2[1],s2[2])
    
    def get(self):
        if self.act == 0: return self.s1
        elif self.act == 1: return self.s2
        else: return None
    
    def set(self, stance:int):
        self.act = stance
        
    
    def move(self, pos:tuple):
        self.s1.rect.x = pos[0]
        self.s1.rect.y = pos[1]

        self.s2.rect.x = pos[0]
        self.s2.rect.y = pos[1]
    
    def hover(self, pos:tuple) -> bool:
        x = self.get()
        if pos[0]< x.rect.x :return False
        if pos[0]> x.rect.x+x.rect.width :return False
        if pos[1]< x.rect.y :return False
        if pos[1]> x.rect.y+x.rect.height :return False
        
        return True

class Button(pygame.sprite.Sprite):
    def __init__(self, path:str, width, height) -> None:
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.image = pygame.image.load(path)

        self.rect = self.image.get_rect()


