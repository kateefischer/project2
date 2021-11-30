from grid import startGrid
from dropdown import DropDown
import pygame

pygame.init()

def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

pygame.init()
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Guess Who?")

pygameSurface = pilImageToSurface(startGrid)

COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    800, 50, 200, 50,
    pygame.font.SysFont(None, 30),
    "Questions", ["Calibration", "Test"])


run = True
while run:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.main = list1.options[selected_option]

    window.fill((255, 255, 255))
    list1.draw(window)


    window.blit(pygameSurface, pygameSurface.get_rect(center = (400, 400)))
    pygame.display.flip()
