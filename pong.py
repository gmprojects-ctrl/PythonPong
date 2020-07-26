import pygame
#Initialising the Environment
width=640 #Width and height of the screen
height=480
pygame.init()
win =pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock() #Initialsing the score
#Making the classes
class Block:
    def __init__(self,width,height,x,y,v): #Initialising the size, position and velocity of each block
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.v=v
    def display(self): # Drawing each block
        pygame.draw.rect(win,(255,0,0),[self.x,self.y,self.width,self.height])
    def move(self): # Allowing the player character to move
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP] and (self.y > 0):
            self.y-=self.v
        elif keys[pygame.K_DOWN] and (self.y < height-self.height):
            self.y+=self.v
    def emove(self,ball_y): # Allow the bot character to move based on the position of the ball
        if (ball_y>height/2):
            self.y+=self.v
        elif(ball_y<height/2):
            self.y-=self.v
        else:
            pass
    def echeck(self): #Stopping the bot from going out of bounds
        if (self.y<=0):
            self.y=0
        elif (self.y>=height-self.height):
            self.y=height -self.height
        else:
            pass
        
class Ball: 
    def __init__(self,x,y,x_v,y_v,r): #Setting up the positon and velocity of the ball
        self.x=x
        self.y=y
        self.x_v=x_v
        self.y_v=y_v
        self.r=r
    def checky_v(self): #Checking the ball's the horizontal sides and making sure it bounces (assuming perfectly elasticity)  
        if (self.y <= (0+self.r)):
            self.y=0+self.r
            self.y_v*=-1
        elif (self.y >= (height-self.r)):
            self.y=height-self.r
            self.y_v*=-1
    def hit(self,block_x,block_y,block_width,block_height,who):
        #The hit detection of the ball must be seperate for the bot and the player beacuse of their relative postions
        #in the screen
        if who=="P": #If the player hits the ball
            if (self.x == (block_x+block_width)) and (self.y>=block_y) and (self.y<=block_y+block_height):
                self.x_v*=-1
            else:
                pass
        elif who=="E": #If the bot hits the ball
            if (self.x == (block_x)) and (self.y>=block_y) and (self.y<=block_y+block_height):
                self.x_v*=-1
            else:
                pass
        else:
            pass
    def outbounds(self):
        #Checking if the ball is out of bounds and returning it to the original position 
        if (self.x <= (0+self.r)) or (self.x >= (width-self.r)) :
            self.x=int(width/2)
            self.y=int(height/2)
            self.x_v*=-1
            pygame.display.update() #Time delay of a 1 second in order for the ball to not glitch.
            pygame.time.wait(1000)
        else:
            pass
    def move(self): #Moving the ball
        self.x+=self.x_v
        self.y+=self.y_v
    def display(self):#Drawing the ball
        pygame.draw.circle(win,(255,255,255),[self.x,self.y],self.r)
#Initialising the Classes 
ball=Ball(int(width/2),int(height/2),5,5,10,)
player=Block(20,100,50,50,5)
enemy=Block(20,100,width-player.x,player.y,10)
#Main game
state= True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state= False
    win.fill((0,0,0))
    #Checking the ball's properties
    ball.outbounds()
    ball.checky_v()
    ball.hit(enemy.x,enemy.y,enemy.width,enemy.height,"E")
    ball.hit(player.x,player.y,player.width,player.height,"P")
    ball.move()
    #Allowing the agents of the game to move to postion 
    player.move()
    enemy.emove(ball.y)
    enemy.echeck()
    #Rendering the game
    ball.display()
    enemy.display()
    player.display()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    
