import pygame
#Initialising the Environment
pygame.init()
win =pygame.display.set_mode((640,480))
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
    def move(self):
        self.x= self.x+(self.x_v*clock.get_rawtime())         
    def display(self):
        pygame.draw.circle(win,(255,255,255),[self.x,self.y],self.r)
#Initialising the Classes 
ball=Ball(320,240,5,5,10)
#Main game
state= True
while state==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state= False
    win.fill((0,0,0))
    ball.display() 
    ball.move()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    
