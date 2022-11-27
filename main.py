#pygame helye
import pygame
#könyvtárak betöltése
import sys

def importer():
    sys.path.insert(1,'./game/')
    sys.path.insert(2,'./credit/')
    sys.path.insert(3,'./scoreboard/')

importer()

#modulok betöltése
import button
import scoreboardM
import gameM
import fajlkezelo
import nevbeker


def main():
    pygame.init()

    #fixinit
    screen = pygame.display.set_mode((1000,600))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Farmos játék')
    pygame.display.set_icon(pygame.image.load('./icon.ico'))

    #button render
    render = pygame.sprite.Group()
    
    #buttons
    newGame = button.MenuButton(['./mainIMG/newGame.png',250,50],['./mainIMG/newGameHover.png',250,50])
    render.add(newGame.get())
    newGame.move((40,390))

    scoreboard = button.MenuButton(['./mainIMG/scoreboard.png',250,50],['./mainIMG/scoreboardHover.png',250,50])
    render.add(scoreboard.get())
    scoreboard.move((40,450))

    exitbutton = button.MenuButton(['./mainIMG/exit.png',250,50],['./mainIMG/exitHover.png',250,50])
    render.add(exitbutton.get())
    exitbutton.move((40,510))

    #background
    bg = pygame.image.load('./mainIMG/bg.png')

    #fajlkezeles
    rendszer = fajlkezelo.Toplista('./scoreboard/eredmeny.txt')
    rendszer.rendez()
    rendszer.ment()


    #gameloop
    isMain = True

    while isMain:
        # pre

        render.update()

        mouse = pygame.mouse.get_pos()
        screen.fill((0,0,0))

        screen.blit(bg,(0,0))

        #input
        for x in [newGame,scoreboard,exitbutton]:
            set(render, x, 0)

        for x in [newGame,scoreboard,exitbutton]:
            if x.hover(mouse):
                set(render,x,1)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isMain = False
            #menü léptetés
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if newGame.hover(mouse):
                    rendszer.beszur((gameM.main(screen,clock),nevbeker.main(screen,clock)))
                if scoreboard.hover(mouse):
                    scoreboardM.main(screen,clock,rendszer)
                if exitbutton.hover(mouse):
                    isMain = False

        #post
        render.draw(screen)
        
        #screen
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def set(group:pygame.sprite.Group,nev:button.MenuButton,stance:int):
    group.remove(nev.get())
    nev.set(stance)
    group.add(nev.get())


main()