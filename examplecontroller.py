import pygame
from os import sys

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us printx to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class Textprintx:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printx(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to printx
textprintx = Textprintx()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textprintx.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textprintx.printx(screen, "Number of joysticks: {}".format(joystick_count) )
    textprintx.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textprintx.printx(screen, "Joystick {}".format(i) )
        textprintx.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textprintx.printx(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textprintx.printx(screen, "Number of axes: {}".format(axes) )
        textprintx.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textprintx.printx(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textprintx.unindent()
            
        buttons = joystick.get_numbuttons()
        textprintx.printx(screen, "Number of buttons: {}".format(buttons) )
        textprintx.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textprintx.printx(screen, "Button {:>2} value: {}".format(i,button) )
        textprintx.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textprintx.printx(screen, "Number of hats: {}".format(hats) )
        textprintx.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textprintx.printx(screen, "Hat {} value: {}".format(i, str(hat)) )
        textprintx.unindent()
        
        textprintx.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
    if joystick.get_button(1) == 1:
	done = True

