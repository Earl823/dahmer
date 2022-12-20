import os
import random
import time
import pygame
import character, wall

# Class for the player
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x):
        super(Player, self).__init__()
        self.width = 35
        self.height = 64
        self.x = x
        self.surf = pygame.Surface((100, 100))
        self.b = pygame.draw.rect(screen, (255, 255, 255), [200, 400, 15, 15])
        # self.surf.fill((255, 255, 255))
        self.rect1 = self.surf.get_rect()
        # self.img = pygame.image.load('pic/red-ball.png')
        # self.rect = rect
        self.rect = pygame.Rect(x, 35, self.width , self.height)
        # self.rect = pygame.Rect(27, 27, 27, 27)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

def collide(p1, p2):
    if p1.rect.colliderect(p2):
        print("player 1 win")
    if p2.rect.colliderect(end_rect):
        print("player 2 win")
        # sys.exit()
    

def bg():
    man = screen.blit(character.bg2, (0,0))

right = False
left = False
front = False
back = False
walk_count = 0

right1 = False
left1 = False
down1 = False
walk_count1 = 0

player1 = True
player2 = True

def draw_game1():
    global walk_count

    if walk_count >= 36:
        walk_count = 0
    if left:
        screen.blit(character.left[walk_count//4], player.rect)
        walk_count += 1
    elif right:
        screen.blit(character.right[walk_count//4], player.rect)
        walk_count += 1
    elif front:
        screen.blit(character.front[walk_count//4], player.rect)
        walk_count += 1
    elif back:
        screen.blit(character.back[walk_count//4], player.rect)
        walk_count += 1
    else:
        screen.blit(character.char, player.rect) 

    pygame.time.delay(30)

def draw_game2():
    global walk_count1

    if walk_count1 >= 36:
        walk_count1 = 0
    if left1:
        screen.blit(character.left[walk_count1//4], player2.rect)
        walk_count1 += 1
    elif right1:
        screen.blit(character.left[walk_count1//4], player2.rect)
        walk_count1 += 1
    elif down1:
        screen.blit(character.left[walk_count1//4], player2.rect)
        walk_count1 += 1
    else:
        screen.blit(character.char1, player2.rect) 


speed_boost_available = True
speedx = 2
speedy = -2
location_x = random.randint(200, 400)
location_y = random.randint(200, 400)
def speed_boost():
    global speed_boost_available
    global walk_count
    global location_x
    global location_y

    if walk_count == 30 and not speed_boost_available:
        speed_boost_available = True
        location_x = random.randint(25, 750)
        location_y = random.randint(25, 550)

speed_boost_available1 = True
location_x1 = random.randint(200, 500)
location_y1 = random.randint(200, 500)
def speed_boost1():
    global speed_boost_available1
    global walk_count
    global location_x1
    global location_y

    if walk_count == 30 and not speed_boost_available1:
        speed_boost_available1 = True
        location_x1 = random.randint(25, 600)
        location_y1 = random.randint(25, 500)
    

# class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

pygame.init()

width, height = 800, 590
pygame.display.set_caption("Dahmer")
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
walls = [] # List to hold the walls

# Create the player
player = Player(50)
player2 = Player(700)


power = screen.blit(character.ball, (500, 35))
# Parse the level string above. W = wall, E = exit
x = y = 0


for row in wall.level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    # p1()
    # p2()

    # player 1
    if player:
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            player.move(speedy, 0)
            left = True
            right = False
            front = False
            back = False

        elif key[pygame.K_d]:
            
            player.move(speedx, 0)
            left = False
            right = True
            front = False
            back = False
               
        elif key[pygame.K_w]:
            player.move(0, speedy)
            left = False
            right = False
            front = False
            back = True

        elif key[pygame.K_s]:
            player.move(0, speedx)
            left = False
            right = False
            front = True
            back = False

        else:
            left = False
            right = False
            walk_count = 0

    # player 2
    if player2:
        key1 = pygame.key.get_pressed()
    
        if key1[pygame.K_LEFT]:
            player2.move(-2, 0)
            left1 = True
            right1 = False
            down1 = False

        elif key1[pygame.K_RIGHT]:
            player2.move(2, 0)
            left1 = False
            right1 = True
            down1 = False

        elif key1[pygame.K_UP]:
            player2.move(0, -2)

        elif key1[pygame.K_DOWN]:
            player2.move(0, 2)
            left1 = False
            right1 = False
            down1 = True

        else:
            left1 = False
            right1 = False
            down1 = False
            walk_count1 = 0

 
    collide(player, player2)
    
    # Draw the scene
    screen.fill((0, 0, 0))
    bg()
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall.rect) # wall color white

    pygame.draw.rect(screen, (255, 0, 255), end_rect) # box stay color violet
    #player color
    # player.player()
    # player2.player()
    # screen.blit(character.char, player.rect) #player 1
    # screen.blit(character.char, player2.rect) #player 2
    draw_game1()
    draw_game2()
    speed_boost()
    speed_boost1()
   
    if speed_boost_available:
        boost = pygame.draw.rect(screen, (249, 10, 10), [location_x, location_y, 15, 15])
      
        if player.rect.colliderect(boost):
            speed_boost_available = False
            speedx = 10 
            speedy = -10

        elif player2.rect.colliderect(boost):
            speed_boost_available = False
            speedx = 10 
            speedy = -10

    if speed_boost_available1:
        boost1 = pygame.draw.rect(screen, (233, 249, 10), [location_x1, location_y1, 15, 15])
    
        if player.rect.colliderect(boost1):
            speed_boost_available1 = False
            speedx = 2
            speedy = -2

        elif player2.rect.colliderect(boost1):
            speed_boost_available1 = False
            speedx = 2
            speedy = -2


    pygame.display.flip()
    pygame.display.update()
    
pygame.quit()