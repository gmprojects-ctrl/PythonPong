import pygame
#Initialising the Environment
width=640
height=480
pygame.init()
win =pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
#Making the classes
class Block:
    def __init__(self,width,height,x,y,v):
        self.width=width
        self.height=height
        self.x=50
        self.y=50
        self.v=5
    def display(self):
        pygame.draw.rect(win,(255,0,0),[self.x,self.y,self.width,self.height])
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
    def checky_v(self):
        if (self.y <= (0+self.r)):
            self.y=0+self.r
            self.y_v*=-1
        elif (self.y >= (height-self.r)):
            self.y=height-self.r
            self.y_v*=-1
    def checkx_v(self,block_x,block_y,block_width,block_height):
        if (self.x <= (block_x+block_width)) and (self.y >= block_y) and (self.y <= block_y+block_height):
            self.x_v*=-1
        if (self.x <= (0+self.r)):
            self.x=0+self.r
            self.x_v*=-1
        elif (self.x >= (width-self.r)):
            self.x=width-self.r
            self.x_v*=-1
    def move(self):
        self.x+=self.x_v
        self.y+=self.y_v
    def display(self):
        pygame.draw.circle(win,(255,255,255),[self.x,self.y],self.r)
#Initialising the Classes 
ball=Ball(int(width/2),int(height/2),5,5,10,)
player=Block(20,100,50,50,5)
#Main game
state= True
while state==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state= False
    win.fill((0,0,0))
    ball.checkx_v(player.x,player.y,player.width,player.height)
    ball.checky_v()
    ball.move()
    player.move()
    ball.display()
    player.display()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    
