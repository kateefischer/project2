from grid import startGrid
import pygame

pygame.init()
def pilImageToSurface(pilImage):
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Guess Who?")
clock = pygame.time.Clock()

pygameSurface = pilImageToSurface(startGrid)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(pygameSurface, pygameSurface.get_rect(center = (400, 400)))
    pygame.display.flip()


