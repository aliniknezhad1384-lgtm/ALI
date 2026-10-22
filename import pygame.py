import pygame
import time
import random
pygame.init()
x=1200
y=800        
abi=(0,0,255)
ghermez=(255,0,0)
sefid=(255,255,255)
meshki=(0,0,0)
screen= pygame.display.set_mode([x,y])
pygame.display.set_caption('hone')
ghalb=pygame.image.load('ghalb.png')

def coount(scoore):
    f=pygame.font.SysFont(None,60)
    t= f.render("score:"+str(scoore),True,ghermez)
    screen.blit(t,(0,0))

def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(screen,color,[stuffx,stuffy,stuffw,stuffh])

def show(a,b):
    screen.blit(ghalb,(a,b))




def ghobject(text,font):
    g2 = font.render(text,True,ghermez)
    return g2 , g2.get_rect()


def massage_display(text):
    ltext=pygame.font.Font('freesansbold.ttf',115)
    g,h=ghobject(text,ltext)
    h.center = ((x/2),(y/2))
    screen.blit(g,h)
    pygame.display.update()

    time.sleep(2)
    loop()


def crash():
    massage_display('YOU CRASHED!!!')

clock=pygame.time.Clock()
def loop():    
    gexit=False
    a=x*0.45
    b=y*0.82
    rah=0
    yrah=0
    width=random.randrange(350,650)
    sx = random.randrange(0,x-width)
    sy= -600
    speed= 7
    height=100
    scoore=0
    while gexit==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gexit=True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rah=8
                elif event.key == pygame.K_LEFT:
                    rah=-8
                elif event.key == pygame.K_DOWN:
                    yrah=5
                elif event.key == pygame.K_UP:
                    yrah=-5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    rah=0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yrah=0
                

        a+=rah
        b+=yrah
        screen.fill(sefid)
        stuff(sx,sy,width,height,meshki)
        sy+=speed
        coount(scoore)
        show(a,b)
        if a>x-122 or a<0:
            crash()
        if sy > y :
            sy = 0 - height
            width=random.randrange(350,650)
            sx=random.randrange(0,x-width)
            speed+=0.25
            scoore+=1
        if b<sy+height:
            if a>sx and a<sx+width or a+122> sx and a+122 < sx+width:
                crash()


        pygame.display.update()
        clock.tick(60)

loop()
pygame.quit()
quit()