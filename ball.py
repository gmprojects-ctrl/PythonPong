import pygame
#Initialising the Environment
height=480
width=640
pygame.init()
win =pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()
#Making the classes
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
    def checkx_v(self):
        if (self.x <= (0+self.r)):
            self.x=0+self.r
            self.x_v*=-1
        elif (self.x >= (width-self.r)):
            self.x=width-self.r
            self.x_v*=-1
    def move(self):
        self.x+=self.x_v*clock.get_rawtime() 
        self.y+=self.y_v*clock.get_rawtime()
    def display(self):
        pygame.draw.circle(win,(255,255,255),[self.x,self.y],self.r)
#Initialising the Classes 
ball=Ball(320,240,3,3,10)
#Main game
state= True
while state==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state= False
    win.fill((0,0,0))
    ball.checkx_v()
    ball.checky_v()
    ball.move()
    ball.display()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    
