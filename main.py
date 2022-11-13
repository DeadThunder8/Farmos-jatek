#pygame helye
import pygame

#könyvtárak betöltése
import sys
sys.path.insert(1,'./game/')
sys.path.insert(2,'./credit/')
sys.path.insert(3,'./scoreboard/')

#modulok betöltése
import button
import newgameM
import scoreboardM
import gameM
import creditM

def main():
    pygame.init()

    #fixinit
    screen = pygame.display.set_mode((1000,600))
    clock = pygame.time.Clock()

    #button render
    render = pygame.sprite.Group()
    
    #buttons
    newGame = button.MenuButton(['./mainIMG/newGame.png',250,50],['./mainIMG/newGameHover.png',250,50])
    render.add(newGame.get())
    newGame.move((40,300))

    scoreboard = button.MenuButton(['./mainIMG/scoreboard.png',250,50],['./mainIMG/scoreboardHover.png',250,50])
    render.add(scoreboard.get())
    scoreboard.move((40,370))

    credit = button.MenuButton(['./mainIMG/credit.png',250,50],['./mainIMG/creditHover.png',250,50])
    render.add(credit.get())
    credit.move((40,440))

    exitbutton = button.MenuButton(['./mainIMG/exit.png',250,50],['./mainIMG/exitHover.png',250,50])
    render.add(exitbutton.get())
    exitbutton.move((40,510))

    #background
    bg = pygame.image.load('./mainIMG/bg.png')
   

    #gameloop
    isMain = True

    while isMain:
        # pre

        render.update()

        mouse = pygame.mouse.get_pos()
        screen.fill((0,0,0))

        screen.blit(bg,(0,0))

        #input
        for x in [newGame,scoreboard,credit,exitbutton]:
            set(render, x, 0)

        for x in [newGame,scoreboard,credit,exitbutton]:
            if x.hover(mouse):
                set(render,x,1)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                isMain = False
            #menü léptetés
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if newGame.hover(mouse):
                    gameM.main(screen,clock)
                if scoreboard.hover(mouse):
                    scoreboardM.main(screen,clock)
                if credit.hover(mouse):
                    creditM.main(screen,clock)
                if exitbutton.hover(mouse):
                    isMain = False

        #post
        render.draw(screen)
        
        #screen
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def set(group:pygame.sprite.Group,nev:button.MenuButton,stance:int):
    group.remove(nev.get())
    nev.set(stance)
    group.add(nev.get())


main()
sys.exit()