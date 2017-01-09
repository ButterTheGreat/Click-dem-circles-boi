import pygame
import time
import random

#^^^^ spazio dove importare le librerie
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
mouse1 = pygame.mouse.get_pos()
click1 = pygame.mouse.get_pressed()
backgroundImg = pygame.image.load("background.png")
pygame.display.set_caption('Click dem circles boi')
circleImg = pygame.image.load("circle.png")
red=(255,0,0)

def score(count,n):
    font = pygame.font.SysFont("calibri", 30)
    text = font.render("Score: "+str(count)+" out of "+str(n), True, red)
    gameDisplay.blit(text,(50,50))
def diff(count):
    font = pygame.font.SysFont("calibri", 30)
    text = font.render("Difficulty: "+str(count), True, red)
    gameDisplay.blit(text,(300,50))

def circle(x,y):
    gameDisplay.blit(circleImg, (x,y))
def click():
    if pygame.mouse.get_pressed()== (1,0,0):
        return 1;
    elif pygame.mouse.get_pressed()== (0,0,0):
        return 0;

def mouse(xy):
    if xy=="x":
        return pygame.mouse.get_pos()[0]
    else:
        return pygame.mouse.get_pos()[1]
def background():
    gameDisplay.blit(backgroundImg, (0,0))
def game_loop():
    gameExit = False
    stimer=100
    x=random.randrange(100,600)
    y=random.randrange(100,500)
    points=0
    timer=stimer
    nofcircles=0
    difficulty=5
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    timer += 20
                    difficulty -= 1
                    stimer += 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    timer += 20
                    difficulty += 1
                    stimer -= 10
        background()
        score(points,nofcircles)
        diff(difficulty)
        if timer != 0:
            timer= timer-1
        if timer ==0:
            x=random.randrange(100,600)
            y=random.randrange(100,500)
            timer=stimer
            nofcircles+=1
        if timer != stimer:
            circle(x,y)
        if click()==1 and mouse("x")>x and mouse("x")<x+110 and mouse("y")>y and mouse("y")<y+110:
            timer=0
            points +=1
       #^^^^^ spazio dove mettere controlli ogni 1/60 secondi
        
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
        
