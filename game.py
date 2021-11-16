import pygame

pygame.init() #initalizes pygame

screen = pygame.display.set_mode(( 800, 600 )) #creates screen 800 pixels wide, 600 pixels long

#Title and icon
pygame.display.set_caption("Guess Who?")

#images


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if close button is pressed, quit the game
            running = False
    screen.fill((102, 178, 255)) #background RBG colors
    pygame.display.update() #updates the screen

