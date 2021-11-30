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
                  "Are they wearing white?", "Are they wearing purple?", "Are they wearing mint?", "Do they have brown hair?",
                  "Do they have black hair?", "Do they have blonde hair?", "Do they have curly hair?", "Do they have straight hair?"])


run = True
while run:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        guessCount = guessCount+1
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
            else:
                guessing.guessChecker(guessing.mint)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 12:
            if (guessWho in guessing.brownHair):
                guessing.guessChecker(guessing.blackHair)
                guessing.guessChecker(guessing.blondeHair)
            else:
                guessing.guessChecker(guessing.brownHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 13:
            if (guessWho in guessing.blackHair):
                guessing.guessChecker(guessing.brownHair)
                guessing.guessChecker(guessing.blondeHair)
            else:
                guessing.guessChecker(guessing.blackHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 14:
            if (guessWho in guessing.blondeHair):
                guessing.guessChecker(guessing.brownHair)
                guessing.guessChecker(guessing.blackHair)
            else:
                guessing.guessChecker(guessing.blondeHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 15:
            if (guessWho in guessing.curlyHair):
                guessing.guessChecker(guessing.straightHair)
            else:
                guessing.guessChecker(guessing.curlyHair)
            pygameSurface = pilImageToSurface(makeGrid())
        if selected_option == 16:
            if (guessWho in guessing.blondeHair):
                guessing.guessChecker(guessing.curlyHair)
            else:
                guessing.guessChecker(guessing.straightHair)
            pygameSurface = pilImageToSurface(makeGrid())
    if grid.numTrue() == 1:
        run = False
        print(guessCount)


    window.fill((255, 255, 255))
    list1.draw(window)
    window.blit(pygameSurface, pygameSurface.get_rect(center = (400, 400)))
    pygame.display.flip()
