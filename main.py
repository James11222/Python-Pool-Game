import pygame
from pygame.locals import *
import random, math, sys
import time

pygame.init()
#initialize and create some variables
songs = ['Elevator Music.mp3', 'Finisher_2.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
width, height = 800, 500
Surface = pygame.display.set_mode((800,500))
bg = pygame.image.load("pooltable.png")
bg = pygame.transform.scale(bg,(800,500))
#colors
red = (255,0,0)
green = (0,200,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,250)
brown = (165,42,42)
pink = (255,200,200)
#defining what a ball is
#JAMES'S CODE ---------------------------------------------------
class Ball:
    def __init__(self,x,y,c):
        self.radius = 10
        self.color = c
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.mass = 1

#here we define a vector class which will make our lives much easier, here we can rewrite operators that deal with these vectors and make our own
#much thanks to a CS student named Dhruba Ghosh who recommended the idea of utilizing a vector based approach. Will be acknowledged in
#our write up.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #all the properties of vectors and the tools we can use with them. We could use numpy, but this made more intuitive sense to make our own
    #class, and rewrite our own operators. It is nice to stay consistent with the class and object style from before with the balls.
    def len(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)
    def angle(self):
        return math.atan2(self.y, self.x)
    def norm(self):
        if self.x == 0 and self.y == 0:
            return Vector(0, 0)
        return self / self.len()
    def dot(self, other):
        return self.x*other.x + self.y*other.y

#make a list of balls
queball = Ball(222,250,white)
queball.mass = 0.9
striped_1 = Ball(410,250,red)
striped_2 = Ball(483,295,red)
striped_3 = Ball(429,239,red)
striped_4 = Ball(447,272,red)
striped_5 = Ball(483,205,red)
striped_6 = Ball(465,217,red)
striped_7 = Ball(483,250,red)
solid_1 = Ball(465,261,blue)
solid_2 = Ball(465,239,blue)
solid_3 = Ball(447,228,blue)
solid_4 = Ball(429,261,blue)
solid_5 = Ball(483,273,blue)
solid_6 = Ball(465,283,blue)
solid_7 = Ball(483,227,blue)
solid_8 = Ball(447,250,black)
Balls = [queball,
striped_1,
striped_2,
striped_3,
striped_4,
striped_5,
striped_6,
striped_7,
solid_1,
solid_2,
solid_3,
solid_4,
solid_5,
solid_6,
solid_7,
solid_8]

def Game_won():
    if len(Balls) == 1:
        return True
    else:
        return False

def play_next():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
#JAMES'S CODE ---------------------------------------------------

#FRENLY'S CODE --------------------------------------------------
class QueStick:
    def __init__(self):
        self.color = brown
        self.position1 = Vector(0,0)
        self.position2 = Vector(0,0)
        self.position3 = Vector(0,0)
        self.position4 = Vector(0,0)
que = QueStick()

#FRENLY'S CODE --------------------------------------------------

#DARBY'S CODE ---------------------------------------------------
class Pocket:
  def __init__(self,x,y):
    self.radius = 20
    self.x = x
    self.y = y

#setting the pocket's locations
rtpocket = Pocket(50,50)
mtpocket = Pocket(400,40)
ltpocket = Pocket(750,50)
rbpocket = Pocket(50,450)
mbpocket = Pocket(400,460)
lbpocket = Pocket(750,450)
pockets = [rtpocket, mtpocket, ltpocket, rbpocket, mbpocket, lbpocket]

def pocket_collision():
    for ball in Balls:
        x2,y2 = ball.position.x, ball.position.y
        if ball != queball and ball != solid_8:
            for poc in pockets:
                distance = math.hypot(poc.x-x2, poc.y-y2)
                if distance <= (poc.radius)+(ball.radius):
                    Balls.remove(ball)
        elif ball == queball:
            for poc in pockets:
                distance = math.hypot(poc.x-x2, poc.y-y2)
                if distance <= (poc.radius)+(ball.radius):
                    ball.position = Vector(222,250)
                    ball.velocity = Vector(0,0)
        elif ball == solid_8:
            if len(Balls) >= 1:
                for poc in pockets:
                    distance = math.hypot(poc.x-x2, poc.y-y2)
                    if distance <= (poc.radius)+(ball.radius):
                        print("GAME OVER!")
                        Balls.remove(ball)
                        queball.position = Vector(100,250)
                        striped_1.position = Vector(410,250)
                        striped_2.position = Vector(483,295)
                        striped_3.position = Vector(429,239)
                        striped_4.position = Vector(447,272)
                        striped_5.position = Vector(483,205)
                        striped_6.position = Vector(465,217)
                        striped_7.position = Vector(483,250)
                        solid_1.position = Vector(465,261)
                        solid_2.position = Vector(465,239)
                        solid_3.position = Vector(447,228)
                        solid_4.position = Vector(429,261)
                        solid_5.position = Vector(483,273)
                        solid_6.position = Vector(465,283)
                        solid_7.position = Vector(483,227)
                        solid_8.position = Vector(447,250)
                        queball.velocity = Vector(0,0)
                        striped_1.velocity = Vector(0,0)
                        striped_2.velocity = Vector(0,0)
                        striped_3.velocity = Vector(0,0)
                        striped_4.velocity = Vector(0,0)
                        striped_5.velocity = Vector(0,0)
                        striped_6.velocity = Vector(0,0)
                        striped_7.velocity = Vector(0,0)
                        solid_1.velocity = Vector(0,0)
                        solid_2.velocity = Vector(0,0)
                        solid_3.velocity = Vector(0,0)
                        solid_4.velocity = Vector(0,0)
                        solid_5.velocity = Vector(0,0)
                        solid_6.velocity = Vector(0,0)
                        solid_7.velocity = Vector(0,0)
                        solid_8.velocity = Vector(0,0)
            elif len(Balls) == 0:
                for poc in pockets:
                    distance = math.hypot(poc.x-x2, poc.y-y2)
                    if distance <= (poc.radius)+(ball.radius):
                        print("YOU WIN!")
                        Balls.remove(ball)


#calculate the number of sunk balls by color (prints on screen)
red_balls = []
blue_balls = []
for ball in Balls:
    if ball.color == red:
        red_balls.append(ball)
    if ball.color == blue:
        blue_balls.append(ball)

def score():
    x = len(red_balls)
    y = len(blue_balls)
    pocket_collision()
    red_balls_2 = []
    blue_balls_2 = []
    for ball in Balls:
        if ball.color == red:
            red_balls_2.append(ball)
        if ball.color == blue:
            blue_balls_2.append(ball)
    x_new = len(red_balls_2)
    y_new = len(blue_balls_2)
    score_red = x - x_new
    score_blue = y - y_new
    return score_red, score_blue
#DARBY'S CODE -------------------------------------------------

#JAMES'S CODE -------------------------------------------------
#resolve collisions between 2 balls, the most confusing part of project, so lots of comments will be added to guide the reader.
def BallsCollide(C1,C2):
    #these factors are to add realism. Ellasticity is usually a little less than 1 because of the loss of energy
    #due to friction, sound, and heat.
    #for fun try and manipulate this factor, will deviate from real collision mechanics
    ELASTICITY = 0.95
    #we define the center to be the average of the two positions
    #diff is just a unit vector of the difference between their position vectors. Diagram will make more sense in write up
    center = (C1.position + C2.position) / 2
    diff = (C2.position - C1.position).norm()
    C1.position = center - diff * C1.radius
    C2.position = center + diff * C1.radius
    #update their positions according to this new frame
    #we calculate the new speeds that are attributing to the collision (see diagram) to be just a dot product of velocity vector with the
    #difference unit vector
    speed_1 = C1.velocity.dot(diff)
    speed_2 = C2.velocity.dot(diff)
    #the effective impulse from the collision is just the other balls effective speed (times the mass and ellasticity factors) - that balls speed
    Impulse_1 = speed_2 * (2*C2.mass)/(C1.mass+C2.mass) - speed_1
    Impulse_2 = speed_1 * (2*C1.mass)/(C2.mass+C1.mass) - speed_2
    #the new velocity vectors are just the effective impulse (time ellasticity factor) in the unit difference vector added to the original velocity vector
    C1.velocity = C1.velocity + diff * Impulse_1 * ELASTICITY
    C2.velocity = C2.velocity + diff * Impulse_2 * ELASTICITY

#the function we call to calculate movement
def Move(secs):
    for ball in Balls:
        friction = 1200 #friction is a big value simply because we are multiplying by seconds
        #basically if if a ball is moving with a magnitude v, then if v < friction stop moving. if v >= friction*secs(fraction of a second)
        #then we multiply friction factor to the unit vector in the direction of v and subtract
        ball.position = ball.position + ball.velocity * secs
        speed = ball.velocity.len()
        if speed < friction * secs:
            ball.velocity = Vector(0, 0)
        else:
            ball.velocity = ball.velocity - ball.velocity * (friction / speed * secs)

#this function is the way we detect a collision has occured
def CollisionDetect():
    for ball in Balls:
        Circle = ball
        #collision with a wall, checks if ball is out of bounds and flips it back. So the balls dont roll off screen  (50 is the edge of table)
        if Circle.position.x < Circle.radius + 50 and Circle.velocity.x < 0:
            Circle.velocity.x *= -1
        if Circle.position.x > width-Circle.radius-50 and Circle.velocity.x > 0:
            Circle.velocity.x *= -1
        if Circle.position.y < Circle.radius + 50 and Circle.velocity.y < 0:
            Circle.velocity.y *= -1
        if Circle.position.y > height-Circle.radius-50 and Circle.velocity.y > 0:
            Circle.velocity.y *= -1
    #loop through all the balls and check if there was a collision between that ball and another, careful not to over account for it by counting twice
    for i in range(len(Balls)):
        for j in range(i+1,len(Balls)):
            Circle = Balls[i]
            Circle2 = Balls[j]
            #we find the length of the vector between the two balls, if that is greater than both their radii then dont collide, otherwise
            #we call our collision function to tell the balls what to do
            if (Circle.position - Circle2.position).len() <= (Circle.radius+Circle2.radius):
                BallsCollide(Circle,Circle2)
#JAMES'S CODE -------------------------------------------------------

#DARBY'S CODE -------------------------------------------------------
                sound1 = pygame.mixer.Sound("poolballhit.wav")
                sound2 = pygame.mixer.Sound("billiards+2.wav")
                sound3 = pygame.mixer.Sound("Billiards+3.wav")
                sound4 = pygame.mixer.Sound("poolhall.wav")
                sounds = [sound1, sound2, sound3, sound4]
                random_num = random.randrange(0,3)
                random_sound = sounds[random_num]
                pygame.mixer.Sound.play(random_sound)
#DARBY'S CODE -------------------------------------------------------

#JAMES'S CODE -------------------------------------------------------
#Our drawing function
def Draw():
    clock = pygame.time.Clock()
    Surface.blit(bg,(0,0))
    for ball in Balls:
        pygame.draw.circle(Surface,ball.color,(int(ball.position.x),int(ball.position.y)),ball.radius)
    queball = Balls[0]
    speed = queball.velocity.len()
    if speed == 0:
        pygame.draw.line(Surface,que.color,[que.position1.x,que.position1.y],[que.position2.x,que.position2.y],7)
        pygame.draw.line(Surface,white,[que.position3.x,que.position3.y],[que.position4.x,que.position4.y],1)
    if Balls[len(Balls)-1] != solid_8:
        if len(Balls) > 1:
            font = pygame.font.Font('batmfa__.ttf', 80)
            text = font.render('GAME OVER!', True, black)
            textRect = text.get_rect()
            textRect.center = (400,250)
            Surface.blit(text, textRect)
        elif len(Balls) == 1:
            font = pygame.font.Font('batmfa__.ttf', 80)
            text = font.render('YOU WIN!', True, black)
            textRect = text.get_rect()
            textRect.center = (400,250)
            Surface.blit(text, textRect)
#JAMES'S CODE ------------------------------------------------------

#DARBY'S CODE ------------------------------------------------------
    x,y = score()
    font = pygame.font.Font('batmfa__.ttf', 18)
    text = font.render('Score of red balls: {0:1.0f}'.format(x), True, red,black)
    textRect = text.get_rect()
    textRect.center = (210,25)
    Surface.blit(text, textRect)
    font2 = pygame.font.Font('batmfa__.ttf', 18)
    text2 = font.render('Score of blue balls: {0:1.0f}'.format(y), True, blue,black)
    textRect2 = text2.get_rect()
    textRect2.center = (590,25)
    Surface.blit(text2, textRect2)
    
    secs = clock.tick(100) / 1000
    pygame.display.flip()
#DARBY'S CODE -------------------------------------------------------

    #we return the amount of seconds it takes to draw to the screen, very small number. This will essentially be what tells the
    #move function how fast the balls need to move and change their positions and velocities.
    return secs
#our main game loop function that the heart of the game runs on

def Game_won():
    if len(Balls) == 1:
        return True
    else:
        return False

def main():
    #this deltaTime variable allows us to update our game in a way that is movement per second instead of pixels per frame; makes our game smoother
    deltaTime = 1000 / 60
    check = 0
    while True:
#FRENLY'S CODE ---------------------------------------------
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keystate[K_ESCAPE]:
                pygame.quit(); sys.exit()
            queball = Balls[0]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("CHEAT CODE")
                    solid_8.position = Vector(50,50)
                    solid_8.velocity = Vector(0,0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    for ball in Balls[0:len(Balls)-1]:
                        print("CHEAT CODE")
                        ball.position = Vector(50,50)
                        ball.velocity = Vector(0,0)
            if event.type == pygame.MOUSEMOTION:
                cursor_position = pygame.mouse.get_pos() #this records the position of the mouse on the window
                x = cursor_position[0]
                y = cursor_position[1]
                dx = x - queball.position.x
                dy = y - queball.position.y
                theta = math.atan2(dy,dx)
                que.position1.x = 20*math.cos(theta) + queball.position.x
                que.position1.y = 20*math.sin(theta) + queball.position.y
                que.position2.x = 350*math.cos(theta) + queball.position.x
                que.position2.y = 350*math.sin(theta) + queball.position.y
                que.position3.x = 20*math.cos(theta + math.pi) + queball.position.x
                que.position3.y = 20*math.sin(theta + math.pi) + queball.position.y
                que.position4.x = 700*math.cos(theta + math.pi) + queball.position.x
                que.position4.y = 700*math.sin(theta + math.pi) + queball.position.y

            speed = queball.velocity.len()
            if speed == 0:
                if event.type == pygame.KEYDOWN: #space bar is pressed down here
                    if event.key == pygame.K_SPACE:
                        t_0 = time.process_time() #time is recorded when space bar is pressed down
                if event.type == pygame.KEYUP: #space bar is released here, space bar gets unpressed
                    if event.key == pygame.K_SPACE:
                        t_1 = time.process_time() #time is recorded when space bar is released/unpressed
                        power = 50*(t_1 - t_0) #this makes the power of cue ball hit depend on how long you hold the space bar for, its up to the player
                        queball.velocity.x += -power*math.cos(theta) *40 #the power has a factor of 50 because any number lower, then the ball would either go too slow or you'd have to hold the space bar fot a very long time, which is boring
                        queball.velocity.y += -power*math.sin(theta) *40
#FRENLY'S CODE -----------------------------------------------
            if check == 0:
                if Game_won() == True:
                    play_next()
                    check += 1

        Move(deltaTime)
        CollisionDetect()
        deltaTime = Draw()

if __name__ == '__main__': main()
