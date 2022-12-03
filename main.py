
import os
import random
import pygame
import character, wall

# Class for the orange dude
class Player(object):
    
    def __init__(self):
        # self.img = pygame.image.load('pic/red-ball.png')
        # self.rect = rect
        self.rect = pygame.Rect(100, 100, 100, 100)

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

    # def player(self):
    #     p1 = screen.blit(character.rect, (16, 16))
    #     p2 = screen.blit(character.rect1, (16, 16))

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


# class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
# os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

width, height = 800, 590
pygame.display.set_caption("Dahmer")
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
walls = [] # List to hold the walls

# Create the player
player = Player()
player2 = Player() 

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
    key = pygame.key.get_pressed()

    # player 1
    if key[pygame.K_a]:
        player.move(-2, 0)
    if key[pygame.K_d]:
        player.move(2, 0)
    if key[pygame.K_w]:
        player.move(0, -2)
    if key[pygame.K_s]:
        player.move(0, 2)

    #player 2
    if key[pygame.K_LEFT]:
        player2.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player2.move(2, 0)
    if key[pygame.K_UP]:
        player2.move(0, -2)
    if key[pygame.K_DOWN]:
        player2.move(0, 2)

    player_1 = 0 
    player_2 = 0
    # bg(character.bg2)
    collide(player, player2)
    
    # Just added this to make it slightly fun ;)
    # if player2.rect.colliderect(end_rect):
    #     print("player 2 win")
    # if player.rect.colliderect(player2):
    #     # print("player 1 win")
    #     player_1 += 1
    # print(player_1)
    
    # Draw the scene

    screen.fill((0, 0, 0))
    bg()
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall.rect) # wall color white

    pygame.draw.rect(screen, (255, 0, 255), end_rect) # box stay color violet
    #player color
    # player.player()
    # player2.player()
    screen.blit(character.char, player.rect) #player 1
    screen.blit(character.char2, player2.rect) #player 2
    pygame.display.flip()
    pygame.display.update()
    
pygame.quit()