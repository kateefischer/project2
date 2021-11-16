# import pygame module in this program
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 1600
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
image1 = pygame.image.load('Ellie.png')
image2 = pygame.image.load('Yumn.png')
image3 = pygame.image.load('Grant.png')
image4 = pygame.image.load('Aneesh.png')
image5 = pygame.image.load('Annabel.png')
image6 = pygame.image.load('Kate.png')
image7 = pygame.image.load('Jonas.png')
image8 = pygame.image.load('Kayla.png')
# infinite loop
while True:

    # completely fill the surface object
    # with white colour
    display_surface.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image1, (0, 0))
    display_surface.blit(image2, (400, 0))
    display_surface.blit(image3, (800, 0))
    display_surface.blit(image4, (1200, 0))
    display_surface.blit(image5, (0, 400))
    display_surface.blit(image6, (400, 400))
    display_surface.blit(image7, (800, 400))
    display_surface.blit(image8, (1200, 400))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()



