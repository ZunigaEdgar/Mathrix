# pygame demo 1 

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255,255,255)
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 510
FRAMES_PER_SECOND = 30
ZONEONE = 80
ZONETWO = 190
ZONETHREE = 330
ZONEFOUR = 510

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0,0), "pictures/mathBackground.png")


# 5 - Initialize variables
 
# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

    # 8  Do any "per frame" actions
    
    # 9 - Clear the screen

    
    # 10 - Draw all screen elements
    window.fill(BLACK)
    background.draw()
    
    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




