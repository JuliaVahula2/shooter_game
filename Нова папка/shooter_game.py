from pygame import*
from random import *


font.init()
font2=font.Font(None,36)
lose=font2.render("YOU LOSE", True, (180,0,0))
win=font2.render("YOU WIN", True,(255,255,255))


width=700
height=500
lost=0
score=0
window=display.set_mode((width,height))
background=transform.scale(image.load("galaxy.jpg"),(700,500))
clock=time.Clock()
display.set_caption("Шутер")
finish=False

class GameSrite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSrite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x-=self.speed
        if keys[K_RIGHT]:
            self.rect.x+=self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet) 

 
class Enemy(GameSrite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        global lost
        # зникає, якщо дійде до краю екрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSrite):
    # рух ворога
    def update(self):
        self.rect.y += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.y < 0:
            self.kill()
win_width = 700
win_height = 500
img_monsters="ufo.png"
player=Player("rocket.png",300,400,65,65,10)
monsters=sprite.Group()
for m in range(1,6):
    monster=Enemy(img_monsters, randint(
        80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)


bullets = sprite.Group()
mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.5)
mixer.music.play()
 
font.init()
font2=font.Font(None,30)
win=font2.render("YOU WIN",True,(255,255,255))
lose=font2.render("YOU LOST",True,(180,0,0))
bullets = sprite.Group()
run=True
finish=False

while run:

    for e in event.get():
        if e. type== QUIT:
            run=False
        if e.type==KEYDOWN:
            if e.key==K_SPACE:
                player.fire()
    if not finish:
        window.blit(background,(0,0))

        text=font2.render("ПРОПУСКИ:"+str(lost),1,(255,255,255))
        window.blit(text,(10,20))
        text2=font2.render("РАХУНОК:"+str(score),1,(255,255,255))
        window.blit(text2,(10,50))
        bullets.update()

        bullets.draw(window)
        player.update()
        player.reset()
        monsters.update()
        
        monsters.draw(window)
        collidergroup=sprite.groupcollide(bullets,monsters,True,True)
        for c in collidergroup:
            score=score+1
            monster=Enemy(img_monsters, randint(
                  80, win_width - 80), -40, 80, 50, randint(1,5))
            monsters.add(monster)
   


        if sprite .spritecollide(player, monsters,False ) or lost>= 3 :
            finish=True
            window.blit(lose,(250,250))
            
        if score>=10:
            finish=True
            window.blit(win,(250,250))



    display.update()
    clock.tick(60)
 
    
    