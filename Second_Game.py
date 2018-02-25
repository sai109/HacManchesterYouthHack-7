import pygame

# Initialises pygame's modules and acts as a second import for pygame
pygame.init()

# Sets the values of the window's dimensions
display_width = 800
display_height = 600

# Sets the values of colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Sets up height and width of window
# Requires tuple parameter
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Sets window title
pygame.display.set_caption('Winter Olympics - Silly Mode')

# Defines game's clock
clock = pygame.time.Clock()

# Loads sprites into program
stickmanImg = pygame.image.load('stickman.png')

def stickman(x,y):

    # Displaying image to window
    gameDisplay.blit(stickmanImg, (x,y))

x = (display_width * 0.5)
y = (display_height * 0.5)

# Defines breakout variable
crashed = False

while not crashed:

    # Creates a list of events that happend per frame per second
    for event in pygame.event.get():

        # When player presses 'x' button to close window, to close window
        if event.type == pygame.QUIT:

            crashed = True

    # Sets game's background to white
    gameDisplay.fill(white)

    # Displays stickman image
    stickman(x,y)
    
    # Updates whole game window
    pygame.display.update()

    # Defines fps
    clock.tick(60)

# Stops pygame from running
pygame.quit()

# CLoses window
quit()
