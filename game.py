import pygame

pygame.init() #initalizes pygame

screen = pygame.display.set_mode(( 1000, 700 )) #creates screen 800 pixels wide, 600 pixels long

#Title
pygame.display.set_caption("Guess Who?")

#images

def images():
    screen.blit(im1,(im1X, im1Y))

im1 = pygame.image.load('Alex.png')
im1X = 0
im1Y = 0
'''
im2 = pygame.image.load('Aneesh.png')
im3 = pygame.image.load('Annabel.png')
im4 = pygame.image.load('Dashiell.png')
im5 = pygame.image.load('Ellie.png')
im6 = pygame.image.load('Evie.png')
im7 = pygame.image.load('Grant.png')
im8 = pygame.image.load('Hudson.png')
im9 = pygame.image.load('Jack.png')
im10 = pygame.image.load('Jonas.png')
im11 = pygame.image.load('Kate.png')
im12 = pygame.image.load('Kayla.png')
im13 = pygame.image.load('Mina.png')
im14 = pygame.image.load('Sam.png')
im15 = pygame.image.load('Will.png')
im16 = pygame.image.load('Yumn.png')
'''


# Game loop
running = True
while running:
    screen.fill((102, 178, 255))  # background RBG colors
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if close button is pressed, quit the game
            running = False

    images() #after screen.fill so it appears over the background
    pygame.display.update() #updates the screen

