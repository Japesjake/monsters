if True:
    pass
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
    pg.mixer.music.play(-1)
    WIDTH=800
    HEIGHT=800
    GREEN=(0,128,0)
    RED=(255,0,0)
    WHITE=(255,255,255)
    surface=pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Monsters")
    font=pg.font.Font('freesansbold.ttf',15)
    font2=pg.font.Font('freesansbold.ttf',5)
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
        self.friend=Monster(WIDTH-600,HEIGHT-400,50,50,'wang',True,worth=100,atk=40)
        self.enemy=Monster(WIDTH-200,HEIGHT-400,50,50,'freddy',False,worth=100,atk=10)
        self.level=1
        self.tier=1
    def store(self, monster):
        if monster.capture:
            monster.hp=monster.max
        monster.x=0
        if monster not in self.friendly_monsters:
            self.friendly_monsters.append(monster)
        for i in range(len(game.friendly_monsters)):
            game.friendly_monsters[i].position=i
        monster.y=monster.position*80+20
        monster.hp_bar.x=monster.x
        monster.hp_bar.y=monster.y+50
        if monster.hp>100:
            monster.hp_bar.sizex=50
        else: monster.hp_bar.sizex=monster.hp/2
        monster.level_counter.x=0
        monster.level_counter.y=monster.y-15
        monster.friendly=True
        monster.dead=False
        monster.hp_counter.x=-100
        monster.atk_counter.x=-100
    def retrieve(self, monster):
        monster.x=WIDTH-600
        monster.y=HEIGHT-400
        monster.level_counter.x=monster.x+15
        monster.level_counter.y=monster.y-15
        monster.hp_bar.x=monster.x
        monster.hp_bar.y=monster.y+50
        monster.dx=monster.x+50
        monster.sx=monster.x
        monster.hp_counter.level=str('hp: '+str(monster.hp))
        monster.atk_counter.level=str('atk: '+str(monster.atk))
        monster.atk_counter.x=monster.x
        monster.atk_counter.y=monster.y+70
        monster.hp_counter.x=monster.x
        monster.hp_counter.y=monster.y+90
        self.friend=monster
    def new_monster(self):
        i=random.randint(0,2)
        self.enemy=Monster(WIDTH-200,HEIGHT-400,50,50,m[i][0],m[i][1])
        self.tier=int((self.level+3)/5)
        self.enemy.level=self.tier
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
    def __init__(self,x,y,sizex,sizey,name,friendly,level=1,hp=100,atk=10,worth=100):
        super().__init__(x,y,sizex,sizey,name)
        self.hp=hp
        self.max=hp
        self.atk=atk
        self.attacking=False
        self.reversed=False
        self.friendly=friendly
        self.xp=0
        self.worth=worth
        self.level=level
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
        self.atk_counter=Text(self.x,self.y+70,10,10,'atk',str('atk: '+str(self.atk)))
        self.hp_counter=Text(self.x,self.y+90,10,10,'hp',str('hp:'+str(self.hp)))
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
            if self.level==level[0]:
                self.atk=level[1]
                self.max=level[2]
                self.worth=level[3]
        self.level_counter.level=self.level
if True:
    game=Game()
    game.friendly_monsters.append(game.friend)
    atk_button=Button(400,600,50,50,'sword.png')
    victory=Button(275,350,300,100,'victory.png')
    xp=Button(300,375,50,50,'xp.png')
    net=Button(500,375,50,50,'net.png')
    heart=Button(WIDTH/2,HEIGHT/2+50,50,50,'heart.png')
while game.running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            game.running=False
        if event.type==pg.MOUSEBUTTONDOWN:
            game.click=True
    if True:
        surface.fill((0,0,0))
        game.friend.draw()
        game.enemy.draw()
        atk_button.draw()
        game.friend.hp_bar.draw()
        game.enemy.hp_bar.draw()
        if game.friend.attacking or game.enemy.attacking:
            game.friend.move(game)
            game.enemy.move(game)
        if game.victory:
            victory.draw()
            xp.draw()
            net.draw()
            heart.draw()
        game.friend.level_counter.draw()
        game.enemy.level_counter.draw()
        for monster in game.friendly_monsters:
            monster.draw()
            monster.hp_bar.draw()
            monster.level_counter.draw()
            monster.atk_counter.draw()
            monster.hp_counter.draw()
        game.enemy.hp_counter.draw()
        game.enemy.atk_counter.draw()
        pg.display.update()
    if atk_button.is_moused() and game.click:
        if game.turn=='friend' and game.friend.dead==False:
            game.friend.attacking=True
            game.enemy.hp-=game.friend.atk
            game.friend.hp-=game.enemy.atk
            game.enemy.hp_bar.sizex=game.enemy.hp/2
            game.friend.hp_bar.sizex=game.friend.hp/2
            game.friend.hp_counter.level=str('hp: '+str(game.friend.hp))
            game.enemy.hp_counter.level=str('hp: '+str(game.enemy.hp))
    if game.turn=='foe':
        game.enemy.attacking=True
    if game.enemy.hp<=0 and not game.enemy.dead:
        game.victory=True
        game.enemy.dead=True
        game.friend.attacking=False
        game.enemy.attacking=False
    if game.friend.hp<=0 and not game.victory:
        game.friend.dead=True
    if game.victory and game.click:
        if xp.is_moused():
            game.friend.xp+=game.enemy.worth
            game.friend.hp_bar.sizex=game.friend.hp/2
            game.friend.dead=False
            for i in range(len(thresholds)):
                if i!=len(thresholds)-1 and thresholds[i+1]>=game.friend.xp and thresholds[i]<=game.friend.xp:
                    game.friend.level=i+1
            game.friend.level_counter.level=game.friend.level
            game.victory=False
            game.friend.update_stats()
            game.level+=1
            game.friend.atk_counter.level=str('atk: '+str(game.friend.atk))
            game.friend.hp_counter.level=str('hp: '+str(game.friend.hp))
            game.new_monster()
            game.enemy.update_stats()
            game.enemy.atk_counter.level=str('atk: '+str(game.enemy.atk))            
            game.enemy.hp_counter.level=str('hp: '+str(game.enemy.hp))            
        if net.is_moused():
            game.enemy.capture=True
            game.store(game.enemy)
            game.enemy.capture=False
            game.victory=False
            game.level+=1
            game.new_monster()
            game.enemy.update_stats()
            game.enemy.atk_counter.level=str('atk: '+str(game.enemy.atk))
            game.enemy.hp_counter.level=str('hp: '+str(game.enemy.hp))
        if heart.is_moused():
            game.friend.hp+=game.friend.max
            if game.friend.hp>game.friend.max:
                game.friend.hp=game.friend.max
            game.friend.hp_bar.sizex=game.friend.hp/2
            if game.friend.hp>100:
                game.friend.hp_bar.sizex=50
            game.victory=False
            game.level+=1
            game.friend.hp_counter.level=str('hp: '+str(game.friend.hp))
            game.new_monster()
            game.enemy.update_stats()
            game.enemy.atk_counter.level=str('atk: '+str(game.enemy.atk))
            game.enemy.hp_counter.level=str('hp: '+str(game.enemy.hp))

    if game.click:
        for monster in game.friendly_monsters:
            if monster.is_moused():
                game.store(game.friend)
                friend=monster
                game.retrieve(monster)
    for i in range(len(game.friendly_monsters)):
        if len(game.friendly_monsters)==i:
            break
        if game.friendly_monsters[i].hp<=0:
            del game.friendly_monsters[i]
    if game.click: game.click=False
