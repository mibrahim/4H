#!/usr/bin/python3
 
import math
import pygame
import random
 
# Define some colors
BLACK = (0 ,0, 0)
WHITE = (255, 255, 255)
 
 
# This class represents the ball
# It derives from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):
 
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the ball
        self.image = pygame.Surface([10, 10])
 
        # Color the ball
        self.image.fill(WHITE)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        # Speed in pixels per cycle
        self.speed = 0
 
        # Floating point representation of where the ball is
        self.x = 0
        self.y = 0
 
        # Direction of ball in degrees
        self.direction = 0
 
        # Height and width of the ball
        self.width = 10
        self.height = 10
 
        # Set the initial ball speed and position
        self.reset()
 
    def reset(self):
        self.x = random.randrange(50,750)
        self.y = 350.0
        self.speed=5.0
 
        # Direction of ball (in degrees)
        self.direction = 45 #random.randrange(-45,45)
 
        # Flip a 'coin'
        if random.randrange(2) == 0 :
            # Reverse ball direction, let the other guy get it first
            self.direction += 180
            self.y = 50
 
    # Update the position of the ball
    def update(self):
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
 
        if self.y < 0:
            self.direction = (180 - self.direction) % 360
 
        if self.y > 600:
            self.direction = (180 - self.direction) % 360
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction)%360
 
        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth-self.width:
            self.direction = (360-self.direction)%360
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Pong')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Create the ball
ball = Ball()

movingsprites = pygame.sprite.Group()
movingsprites.add(ball)
 
clock = pygame.time.Clock()
while 1 == 1:
 
    # Clear the screen
    screen.fill(BLACK)
 
    ball.update()
 
    # Draw Everything
    movingsprites.draw(screen)
 
    # Update the screen
    pygame.display.flip()
     
    clock.tick(200)
