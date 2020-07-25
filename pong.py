import pygame
#Initialising the Environment
pygame.init()
win =pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
#Making the classes
class Block:
    def __init__(self,x,y,v):
        self.x=50
        self.y=50
        self.v=5
    def display(self):
        pygame.draw.rect(win,(255,0,0),[self.x,self.y,40,60])
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] and (self.y > 0):
            self.y-=self.v
        elif keys[pygame.K_DOWN] and (self.y < 480-60):
            self.y+=self.v
class Ball:
    def __init__(self,x,y,x_v,y_v,r):
        self.x=x
        self.y=y
        self.x_v=x_v
        self.y_v=y_v
        self.r=r
    def move(self):
        if (self.x<0) or (self.x>640):
            self.x_v= -(self.x_v)
        if (self.x>0) and (self.x<640 -self.r):
            self.x+=int(self.x_v*clock.get_time()*0.5) 
    def display(self):
        pygame.draw.circle(win,(255,255,255),[self.x,self.y],self.r)
#Initialising the Classes 
ball=Ball(320,240,5,5,10)
player=Block(50,50,5)
#Main game
state= True
while state==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state= False
    win.fill((0,0,0))
    ball.move()
    player.move()
    ball.display()
    player.display()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    