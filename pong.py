import pygame
#Initialising the Environment
width = 640  #Width and height of the screen
height = 480
pygame.init()
screen = pygame.display.set_mode((width, height))  #Initialising the screen
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()  #Initialsing the clock (setting fps)
font = pygame.font.SysFont("Liberation Mono", 40, bold=False, italic=False)


#Initialising some functions
#A function to refresh the screen
def Refresh(clock, screen):
    pygame.display.update()
    clock.tick(60)


#A fucntion to render the screen (did it to make the code easier to read)
def RenderScreen(screen, ball, player, enemy, clock):
    screen.fill((0, 0, 0))
    ball.display()
    enemy.display()
    player.display()
    pygame.display.update()
    clock.tick(60)


#A function to write and render text
def WriteText(font, screen, text):
    image = font.render(text, True, (255, 255, 255), None)
    position = (
        int((width / 2) -
            (font.size(text)[0] /
             2)),  #Allow the the text to be centered on the screen
        int((height / 2) - (font.size(text)[1] / 2)))
    screen.fill((0, 0, 0))
    screen.blit(image, position)


#A function to render the actual game
def GameRender(ball, player, enemy, screen, clock):
    #Checking the ball's properties
    ball.outbounds(player, enemy)
    ball.checky_v()
    ball.hit(enemy.x, enemy.y, enemy.width, enemy.height, "E")
    ball.hit(player.x, player.y, player.width, player.height, "P")
    ball.move()
    #Alloscreeng the agents of the game to move to postion
    player.move()
    enemy.emove(ball)
    enemy.echeck()
    #Rendering the game
    RenderScreen(screen, ball, player, enemy, clock)


#A function to show game over
def GameOver(agent, clock, screen, font):
    WriteText(font, screen, f"The {agent} wins")
    Refresh(clock, screen)
    pygame.time.wait(3000)
    WriteText(font, screen, "Press x to quit or wait to start again")
    Refresh(clock, screen)
    pygame.time.wait(3000)


#Making the classes
class Block:
    def __init__(
            self, block_width, block_height, x, y,
            v):  #Initialising the size, position and velocity of each block
        self.width = block_width
        self.height = block_height
        self.x = x
        self.y = y
        self.v = v
        self.points = 0

    def display(self):  # Drascreeng each block
        pygame.draw.rect(screen, (255, 0, 0),
                         [self.x, self.y, self.width, self.height])

    def move(self):  # Alloscreeng the player character to move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and (self.y > 0):
            self.y -= self.v
        elif keys[pygame.K_DOWN] and (self.y < height - self.height):
            self.y += self.v

    def emove(
        self, ball
    ):  # Allow the bot character to move based on the position of the ball
        centre_x = self.x + 0.5 * self.width
        centre_y = self.y - 0.5 * self.height
        angle = abs(centre_y - ball.y / centre_x - ball.x)
        if (ball.x_v > 0 and angle > 0.7 ):
            if (ball.y < centre_y):
                self.y -= self.v
            elif ( ball.y > centre_y):
                self.y += self.v
            else:
                pass
        else:
            pass

    def echeck(self):  #Stopping the bot from going out of bounds
        if (self.y <= 0):
            self.y = 0
        elif (self.y >= height - self.height):
            self.y = height - self.height
        else:
            pass

    def reset(self):  #Reset the point socre
        self.points = 0


class Ball:
    def __init__(self, x, y, x_v, y_v,
                 r):  #Setting up the positon and velocity of the ball
        self.x = x
        self.y = y
        self.x_v = x_v
        self.y_v = y_v
        self.r = r

    def checky_v(
        self
    ):  #Checking the ball's the horizontal sides and making sure it bounces (assuming perfectly elasticity)
        if (self.y <= (0 + self.r)):
            self.y = 0 + self.r
            self.y_v *= -1
        elif (self.y >= (height - self.r)):
            self.y = height - self.r
            self.y_v *= -1

    def hit(self, block_x, block_y, block_width, block_height, who):
        #The hit detection of the ball must be seperate for the bot and the player beacuse of their relative postions
        #in the screen
        if who == "P":  #If the player hits the ball
            if (self.x == (block_x + block_width)) and (
                    self.y >= block_y) and (self.y <= block_y + block_height):
                self.x_v *= -1
            else:
                pass
        elif who == "E":  #If the bot hits the ball
            if (self.x == (block_x)) and (self.y >= block_y) and (
                    self.y <= block_y + block_height):
                self.x_v *= -1
            else:
                pass
        else:
            pass

    def outbounds(self, player, enemy):
        #Checking if the ball is out of bounds and returning it to the original position
        if (self.x <= (0 + self.r)) or (self.x >= (width - self.r)):
            if (self.x <= (0 + self.r)):
                enemy.points += 1
            else:
                player.points += 1
            self.x = int(width / 2)
            self.y = int(height / 2)
            self.x_v *= -1
            WriteText(font, screen,
                      f"Player {player.points} | Bot {enemy.points}")
            pygame.display.update(
            )  #Time delay of a 1 second in order for the ball to not glitch.
            pygame.time.wait(1000)
        else:
            pass

    def move(self):  #Moving the ball
        self.x += self.x_v
        self.y += self.y_v

    def display(self):  #Drascreeng the ball
        pygame.draw.circle(screen, (255, 255, 255), [self.x, self.y], self.r)


#Initialising the Classes and variables
player_speed = 5
ball = Ball(
    int(width / 2),
    int(height / 2),
    player_speed/2,
    player_speed/2,
    10,
)
player_speed = 5
player = Block(20, 100, 50, 50, player_speed)
enemy = Block(20, 100, width - player.x, player.y, player_speed)
winscore = 5
#Main game
state = True
WriteText(font, screen, "Pong by GM projects v1.0.0")
Refresh(clock, screen)
pygame.time.wait(1000)
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    GameRender(ball, player, enemy, screen, clock)
    if (player.points >= winscore
        ):  # If the player or bot wins, shows it and refreshes the game)
        player.points = 0
        enemy.points = 0
        GameOver("Player", clock, screen, font)
    elif (enemy.points >= winscore):
        player.points = 0
        enemy.points = 0
        GameOver("Opponent", clock, screen, font)
    else:
        pass
pygame.quit()
quit()
