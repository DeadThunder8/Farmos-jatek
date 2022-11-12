import pygame
import plantloader

class Vizcsepp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./game/img/eszkozok/vizjel.png')

        self.rect = self.image.get_rect()


class Khanna(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface([100,100])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        self.mpos = (0,0)

        self.image = pygame.image.load('./game/img/eszkozok/kanna.png')

        self.rect = self.image.get_rect()

    def hover(self,pos:tuple[int,int])->bool:
        if pos[0] < self.rect.left or pos[0] > self.rect.right or pos[1] < self.rect.top or pos[1] > self.rect.bottom: return False
        return True

    def helymentes(self):
        self.mpos = (self.rect.x,self.rect.y)

    def visszateres(self):
        self.rect.x = self.mpos[0]
        self.rect.y = self.mpos[1]
    
    def move(self,pos:tuple):
        self.rect.center = pos

    

