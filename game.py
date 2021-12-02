from grid import makeGrid
import pygame
import dropdown
import grid
from dropdown import DropDown
import guessing
import random
pygame.init()
guessCount = 0

guessWhoList = ["Alex", "Aneesh", "Annabel", "Dashiell", "Ellie", "Evie", "Grant", "Hudson", "Jack", "Jonas", "Kate", "Kayla", "Mina", "Sam", "Will", "Yumn"]
guessWho = guessWhoList[random.randint(0,15)]
print(guessWho)

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Guess Who?")

pygameSurface = pilImageToSurface(makeGrid())

COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    800, 50, 300, 30,
    pygame.font.SysFont(None, 20),
    "Questions", ["Is the person a girl?", "Is the person a boy?", "Are they smiling with teeth?","Are they smiling without teeth?",
                  "Are they wearing red?", "Are they wearing blue?", "Are they wearing black?", "Are they wearing grey?", "Are they wearing tan?",
                  "Are they wearing white?", "Are they wearing purple?", "Are they wearing mint?", "Are they wearing plaid?","Do they have brown hair?",
                  "Do they have black hair?", "Do they have blonde hair?", "Do they have curly hair?", "Do they have straight hair?", "Do they have short hair?", "Do they have long hair?"])


run = True
while run:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        guessCount = guessCount+1
        sound = pygame.mixer.Sound("370180__mpaol2023__3-tone-chime-up.wav")
        pygame.mixer.Sound.play(sound)
        list1.main = list1.options[selected_option]
        if selected_option == 0:
            if (guessWho in guessing.girls):
                guessing.guessChecker(guessing.boys)
            else:
                guessing.guessChecker(guessing.girls)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 1:
            if (guessWho in guessing.boys):
                guessing.guessChecker(guessing.girls)
            else:
                guessing.guessChecker(guessing.boys)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 2:
            if (guessWho in guessing.noTeeth):
                guessing.guessChecker(guessing.teeth)
            else:
                guessing.guessChecker(guessing.noTeeth)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 3:
            if (guessWho in guessing.teeth):
                guessing.guessChecker(guessing.noTeeth)
            else:
                guessing.guessChecker(guessing.teeth)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 4:
            if (guessWho in guessing.red):
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.red)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 5:
            if (guessWho in guessing.blue):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.blue)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 6:
            if (guessWho in guessing.black):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.black)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 7:
            if (guessWho in guessing.grey):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.grey)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 8:
            if (guessWho in guessing.tan):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.tan)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 9:
            if (guessWho in guessing.white):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.white)
            pygameSurface = pilImageToSurface(makeGrid())

        if selected_option == 10:
            if (guessWho in guessing.purple):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.mint)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.purple)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 11:
            if (guessWho in guessing.mint):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.plaid)
            else:
                guessing.guessChecker(guessing.mint)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 12:
            if (guessWho in guessing.plaid):
                guessing.guessChecker(guessing.red)
                guessing.guessChecker(guessing.black)
                guessing.guessChecker(guessing.blue)
                guessing.guessChecker(guessing.tan)
                guessing.guessChecker(guessing.white)
                guessing.guessChecker(guessing.purple)
                guessing.guessChecker(guessing.grey)
                guessing.guessChecker(guessing.mint)
            else:
                guessing.guessChecker(guessing.plaid)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 13:
            if (guessWho in guessing.brownHair):
                guessing.guessChecker(guessing.blackHair)
                guessing.guessChecker(guessing.blondeHair)
            else:
                guessing.guessChecker(guessing.brownHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 14:
            if (guessWho in guessing.blackHair):
                guessing.guessChecker(guessing.brownHair)
                guessing.guessChecker(guessing.blondeHair)
            else:
                guessing.guessChecker(guessing.blackHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 15:
            if (guessWho in guessing.blondeHair):
                guessing.guessChecker(guessing.brownHair)
                guessing.guessChecker(guessing.blackHair)
            else:
                guessing.guessChecker(guessing.blondeHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 16:
            if (guessWho in guessing.curlyHair):
                guessing.guessChecker(guessing.straightHair)
            else:
                guessing.guessChecker(guessing.curlyHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 17:
            if (guessWho in guessing.blondeHair):
                guessing.guessChecker(guessing.curlyHair)
            else:
                guessing.guessChecker(guessing.straightHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 18:
            if (guessWho in guessing.longHair):
                guessing.guessChecker(guessing.shortHair)
            else:
                guessing.guessChecker(guessing.longHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 19:
            if (guessWho in guessing.shortHair):
                guessing.guessChecker(guessing.longHair)
            else:
                guessing.guessChecker(guessing.shortHair)
            pygameSurface = pilImageToSurface(makeGrid())
    if grid.numTrue() == 1:
        # define the RGB value for white,
        #  green, blue colour .
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)

        # assigning values to X and Y variable
        X = 400
        Y = 100
        Y2= 300

        # create the display surface object
        # of specific dimension..e(X, Y).
        display_surface = pygame.display.set_mode((500, 400))

        # set the pygame window name
        pygame.display.set_caption('Show Text')

        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        font = pygame.font.Font('freesansbold.ttf', 32)

        # create a text surface object,
        # on which text is drawn on it.
        guesses = "It took you " + str(guessCount) + " guesses!"
        person = "The person was " + str(guessWho) + "!"
        text = font.render(guesses , True, blue, white)
        text2 = font.render(person , True, blue, white)

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        textRect2 = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (500 // 2, 400 // 2)
        textRect2.center = (500 // 2, 200 // 2)
        # infinite loop
        while True:

            # completely fill the surface object
            # with white color
            display_surface.fill(white)

            # copying the text surface object
            # to the display surface object
            # at the center coordinate.
            display_surface.blit(text, textRect)
            display_surface.blit(text2, textRect2)

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


    window.fill((255, 255, 255))
    list1.draw(window)
    window.blit(pygameSurface, pygameSurface.get_rect(center = (400, 400)))
    pygame.display.flip()
