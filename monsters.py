if True:
    pass
    ##<a href="https://www.flaticon.com/free-icons/attack" title="attack icons">Attack icons created by AbtoCreative - Flaticon</a>
    ##<a href="https://www.flaticon.com/free-icons/monster" title="monster icons">Monster icons created by Smashicons - Flaticon</a>
    ##<a href="https://www.flaticon.com/free-icons/xp" title="xp icons">Xp icons created by Freepik - Flaticon</a>
    ##<a href="https://www.flaticon.com/free-icons/xp" title="xp icons">Xp icons created by Falcone - Flaticon</a>
    ##<a href="https://www.flaticon.com/free-icons/fishing-net" title="fishing net icons">Fishing net icons created by Freepik - Flaticon</a>
    ##<a href="https://www.flaticon.com/free-icons/monster" title="monster icons">Monster icons created by Smashicons - Flaticon</a>
    import pygame as pg
    import os, random
    from thresholds import thresholds
    from m import m
    from l import l
if True:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,50)
    pg.init()
    pg.mixer.init()
    music=pg.mixer.music.load("battle2.wav")
    # pg.mixer.music.play(-1)
    WIDTH=800
    HEIGHT=800
    GREEN=(0,128,0)
    RED=(255,0,0)
    WHITE=(255,255,255)
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
        self.friendly_monsters=list()
    def store(self, monster):
        if monster.capture:
            monster.hp=monster.max
        monster.x=0
        if monster not in self.friendly_monsters:
            self.friendly_monsters.append(monster)
        for i in range(len(game.friendly_monsters)):
            game.friendly_monsters[i].position=i
        monster.y=monster.position*80
        monster.hp_bar.x=monster.x
        monster.hp_bar.y=monster.y+50
        monster.hp_bar.sizex=monster.hp/2
        monster.level_counter.x=0
        monster.level_counter.y=monster.y-15
        monster.friendly=True
        monster.dead=False
    def retrieve(self, monster):
        friend.x=WIDTH-600
        friend.y=HEIGHT-400
        friend.level_counter.x=friend.x+15
        friend.level_counter.y=friend.y-15
        friend.hp_bar.x=friend.x
        friend.hp_bar.y=friend.y+50
        friend.dx=friend.x+50
        friend.sx=friend.x
class Text(Object):
    def __init__(self,x,y,sizex,sizey,name,level):
        super().__init__(x,y,sizex,sizey,name)
        self.level=level
    def draw(self):
        self.img=font.render(str(self.level),True,WHITE)
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
    def __init__(self,x,y,sizex,sizey,name,friendly,hp=100,atk=10,worth=100):
        super().__init__(x,y,sizex,sizey,name)
        self.hp=hp
        self.max=hp
        self.atk=atk
        self.attacking=False
        self.reversed=False
        self.friendly=friendly
        self.xp=0
        self.worth=worth
        if self.friendly: self.dx=self.x+50
        else: self.dx=self.x-50
        self.img=pg.image.load(os.path.join('monsters',name+'.png'))
        self.img=pg.transform.scale(self.img,(sizex,sizey))
        self.hp_bar=Bar(self.x,self.y+self.sizey,self.hp/2,self.sizey-40,'bar')
        self.level=1
        self.level_counter=Text(self.x+15,self.y-15,10,10,'level',self.level)
        self.position=0
        self.dead=False
        self.capture=False
    def move(self,game):
        if self.attacking and self.dead==False:
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
    def update_stats(self):
        for level in l:
            if friend.level==level[0]:
                friend.atk=level[1]
                friend.max=level[2]
                print(friend.atk)
if True:
    game=Game()
    friend=Monster(WIDTH-600,HEIGHT-400,50,50,'wang',True,worth=100,atk=50)
    enemy=Monster(WIDTH-200,HEIGHT-400,50,50,'freddy',False,worth=100,atk=10)
    game.friendly_monsters.append(friend)
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
        if friend.attacking or enemy.attacking:############
            friend.move(game)
            enemy.move(game)
        if game.victory:
            victory.draw()
            xp.draw()
            net.draw()
        friend.level_counter.draw()
        enemy.level_counter.draw()
        for monster in game.friendly_monsters:
            monster.draw()
            monster.hp_bar.draw()
            monster.level_counter.draw()
        pg.display.update()
    if atk_button.is_moused() and game.click:
        if game.turn=='friend' and friend.dead==False:
            friend.attacking=True
            enemy.hp-=friend.atk
            friend.hp-=enemy.atk
            enemy.hp_bar.sizex=enemy.hp/2
            friend.hp_bar.sizex=friend.hp/2
    if game.turn=='foe':
        enemy.attacking=True
    if enemy.hp<=0 and not enemy.dead:
        game.victory=True
        enemy.dead=True
        friend.attacking=False
        enemy.attacking=False
    if friend.hp<=0:
        friend.dead=True
    if game.victory and game.click:
        if xp.is_moused():
            friend.xp+=enemy.worth
            friend.hp_bar.sizex=friend.hp/2
            friend.dead=False
            for i in range(len(thresholds)):
                if i!=len(thresholds)-1 and thresholds[i+1]>=friend.xp and thresholds[i]<=friend.xp:
                    friend.level=i+1
            friend.level_counter.level=friend.level
            game.victory=False
            friend.update_stats()
            i=random.randint(0,2)
            enemy=Monster(WIDTH-200,HEIGHT-400,50,50,m[i][0],m[i][1])
        if net.is_moused():
            enemy.capture=True
            game.store(enemy)
            enemy.capture=False
            game.victory=False
            i=random.randint(0,2)
            enemy=Monster(WIDTH-200,HEIGHT-400,50,50,m[i][0],m[i][1])
    if game.click:
        for monster in game.friendly_monsters:
            if monster.is_moused():
                game.store(friend)
                friend=monster
                game.retrieve(monster)
    if game.click: game.click=False