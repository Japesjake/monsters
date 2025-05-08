##<a href="https://www.flaticon.com/free-icons/attack" title="attack icons">Attack icons created by AbtoCreative - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/monster" title="monster icons">Monster icons created by Smashicons - Flaticon</a>
import pygame as pg
import os
if True:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,50)
    pg.init()
    pg.mixer.init()
    music=pg.mixer.music.load("battle2.wav")
    pg.mixer.music.play(-1)
    WIDTH=800
    HEIGHT=800
    surface=pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Monsters")
class Object:
    def __init__(self,x,y,sizex,sizey,name):
        self.x=x
        self.y=y
        self.sx=x
        self.sy=y
        self.sizex=sizex
        self.sizey=sizey
        self.img=pg.image.load(name)
        self.img=pg.transform.scale(self.img,(sizex,sizey))
    def draw(self):
        surface.blit(self.img,(self.x,self.y))
class Game:
    def __init__(self):
        self.running=True
        self.click=False
        self.turn='friend'
class Button(Object):
    def __init__(self,x,y,sizex,sizey,name):
        super().__init__(x,y,sizex,sizey,name)
    def is_moused(self):
        self.mouse=pg.mouse.get_pos()
        self.mousex,self.mousey=self.mouse
        if self.mousex>=self.x and self.mousey>=self.y:
            if self.mousex<=self.x+self.sizex and self.mousey<=self.y+self.sizex:
                return True
        return False
class Monster(Object):
    def __init__(self,x,y,sizex,sizey,name,hp=100,atk=10,friendly=True):
        super().__init__(x,y,sizex,sizey,name)
        self.hp=hp
        self.atk=atk
        self.attacking=False
        self.reversed=False
        self.friendly=friendly
        if self.friendly: self.dx=self.x+50
        else: self.dx=self.x-50
    def attack(self,game):
        if self.attacking:
            if self.friendly:
                if self.x<=self.dx and self.reversed==False:
                    self.x+=1
                if self.x==self.dx:
                    self.reversed=True
                if self.reversed==True:
                    self.x-=1
                if self.x==self.sx and self.reversed==True:
                    self.attacking=False
                    self.reversed=False
                    game.turn='foe'
            else:
                if self.x>=self.dx and self.reversed==False:
                    self.x-=1
                if self.x==self.dx:
                    self.reversed=True
                if self.reversed==True:
                    self.x+=1
                if self.x==self.sx and self.reversed==True:
                    self.attacking=False
                    self.reversed=False
                    game.turn='friend'
if True:
    game=Game()
    monster=Monster(200,400,50,50,'monster.png')
    monster2=Monster(HEIGHT-200,400,50,50,'freddy.png',friendly=False)
    atk_button=Button(400,600,50,50,'sword.png')
while game.running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            game.click=True
    monster.draw()
    monster2.draw()
    atk_button.draw()
    monster.attack(game)
    monster2.attack(game)
    if atk_button.is_moused() and game.click:
        if game.turn=='friend':
            monster.attacking=True
    if game.turn=='foe':
        monster2.attacking=True
    if game.click:
        game.click=False
    pg.display.update()
