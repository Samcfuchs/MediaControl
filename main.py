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
clock = pygame.time.Clock()
pygame.joystick.init()

done = False

# CHEX MIX
# TODO add pygame printing
nogo = True
while nogo:
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print "Please connect a joystick"
	nogo = True
    if joystick_count == 1:
	print "Joystick Recognized"
	nogo = False
    if joystick_count > 1:
	# Pick a joystick

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
