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
MUTE_BUTTON = 3
PAUSE_BUTTON = 0
NEXT_BUTTON = 5
PREV_BUTTON = 4

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
muted = False
last_volume = player.get_volume()
# MAIN GAME LOOP
while done == False:
    # EVENT PROCESSING    
    for event in pygame.event.get(pygame.JOYBUTTONDOWN):
	print "Button pressed: " + str(event.button)
	if event.button == PAUSE_BUTTON:
	    player.toggle_pause()
	elif event.button == MUTE_BUTTON:
	    if muted:
		player.volume_set(last_volume)
		muted = False
	    else:
		last_volume = player.get_volume()
		player.mute()
	        muted = True
	elif event.button == NEXT_BUTTON:
	    player.next_song()
	elif event.button == PREV_BUTTON:
	    player.previous_song()

    # CHANGE VOLUME
    hat = Controller.get_hat(HAT_VAL)
    margin = "2"
    if hat[1] == 1:
	player.volume_adjust("+" + margin)
    elif hat[1] == -1:
	player.volume_adjust("-" + margin)

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
