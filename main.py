import pygame
from os import sys

# Colors
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)

pygame.init()

# Size [width, height]
size = [500, 700] 
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Music Control")

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

# MAIN GAME LOOP
while done == False:
    # EVENT PROCESSING
    for even in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            print "button press"
        if event.type == pygame.JOYBUTTONUP:
            print "button release"

    # DRAWING
    screen.fill(WHITE)

    # Limit to 20 fps
    clock.tick(20)
    
    if joystick.get_button(7) == 1:
        done = True

# END
pygame.joystick.quit()
pygame.quit
sys.exit()
