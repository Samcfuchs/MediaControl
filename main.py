import pygame
import os
from os import sys
from musicplayer import MusicPlayer

# Colors
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)

# START PYGAME
pygame.init()
# Size [width, height]
size = [500, 700] 
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Music Control")
clock = pygame.time.Clock()
pygame.joystick.init()
player = MusicPlayer()

# BUTTON VALUES
Controller = pygame.joystick.Joystick(0)
Controller.init()
HAT_VAL = 0
MUTE_BUTTON = 6
PAUSE_BUTTON = 0

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
        print "Too many joysticks"

done = False
# MAIN GAME LOOP
while done == False:
    # EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            print "button press"
        if event.type == pygame.JOYBUTTONUP:
            print "button release"
    
    # CHANGE VOLUME
    hat = Controller.get_hat(HAT_VAL)
    margin = "2"
    if hat[1] == 1:
	player.volume_adjust("+" + margin)
    if hat[1] == -1:
	player.volume_adjust("-" + margin)

    # MUTING
    if Controller.get_button(MUTE_BUTTON) == 1:
	player.mute()

    # PAUSING
    if Controller.get_button(PAUSE_BUTTON) == 1:
	player.pause()
    
    # DRAWING
    #screen.fill(WHITE)

    # Limit fps
    clock.tick(10)
    
    if Controller.get_button(8) == 1:
        done = True

# END
pygame.joystick.quit()
pygame.quit
sys.exit()
