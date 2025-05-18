##<a href="https://www.flaticon.com/free-icons/attack" title="attack icons">Attack icons created by AbtoCreative - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/monster" title="monster icons">Monster icons created by Smashicons - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/xp" title="xp icons">Xp icons created by Freepik - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/xp" title="xp icons">Xp icons created by Falcone - Flaticon</a>
##<a href="https://www.flaticon.com/free-icons/fishing-net" title="fishing net icons">Fishing net icons created by Freepik - Flaticon</a>
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
    GREEN=(0,128,0)
    surface=pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Monsters")
    font=pg.font.Font('freesansbold.ttf',15)
class Object:
    def __init__(self,x,y,sizex,sizey,name):
        self.x=x
        self.y=y
        self.sx=x
        self.sy=y
        self.sizex=sizex
        self.sizey=sizey
        self.name=name
    def is_moused(self):
        self.mouse=pg.mouse.get_pos()
        self.mousex,self.mousey=self.mouse
        if self.mousex>=self.x and self.mousey>=self.y:
            if self.mousex<=self.x+self.sizex and self.mousey<=self.y+self.sizex:
                return True
        return False
    def draw(self):     
        surface.blit(self.img,(self.x,self.y))
class Game:
    def __init__(self):
        self.running=True
        self.click=False
        self.turn='friend'
        self.victory=False
class Text(Object):
    def __init__(self,x,y,sizex,sizey,name,level):
        super().__init__(x,y,sizex,sizey,name)
        self.level=level
    def draw(self):
        self.img=font.render(str(self.level),True,GREEN)
        surface.blit(self.img,(self.x,self.y))   
class Bar(Object):
    def __init__(self,x,y,sizex,sizey,name):
        super().__init__(x,y,sizex,sizey,name)
    def draw(self):
        pg.draw.rect(surface,GREEN,(self.x,self.y,self.sizex,self.sizey))
class Button(Object):
    def __init__(self,x,y,sizex,sizey,name):
        super().__init__(x,y,sizex,sizey,name)
        self.img=pg.image.load(os.path.join('buttons',name))
        self.img=pg.transform.scale(self.img,(sizex,sizey))
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
        self.img=pg.image.load(os.path.join('monsters',name+'.png'))
        self.img=pg.transform.scale(self.img,(sizex,sizey))
        self.hp_bar=Bar(self.x,self.y+self.sizey,self.hp/2,self.sizey-40,'bar')
        self.level=1
        self.level_counter=Text(self.x,self.y,10,10,'level',self.level)
    def move(self,game):
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
    friend=Monster(WIDTH-600,HEIGHT-400,50,50,'wang')
    enemy=Monster(WIDTH-200,HEIGHT-400,50,50,'freddy',friendly=False)
    atk_button=Button(400,600,50,50,'sword.png')
    victory=Button(275,350,300,100,'victory.png')
    xp=Button(300,375,50,50,'xp.png')
    net=Button(500,375,50,50,'net.png')
while game.running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            game.click=True
    if True:
        surface.fill((0,0,0))
        friend.draw()
        enemy.draw()
        atk_button.draw()
        friend.hp_bar.draw()
        enemy.hp_bar.draw()
        friend.move(game)
        enemy.move(game)
        if game.victory:
            victory.draw()
            xp.draw()
            net.draw()
        friend.level_counter.draw()
        pg.display.update()
    if atk_button.is_moused() and game.click:
        if game.turn=='friend':
            friend.attacking=True
            enemy.hp-=friend.atk
            enemy.hp_bar.sizex=enemy.hp/2
    if game.turn=='foe':
        enemy.attacking=True
    if enemy.hp<=0:
        game.victory=True
    if game.click:
        game.click=False
