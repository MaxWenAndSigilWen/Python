import pygame
import random
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
blocksize = 200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
x, y = 0, 0
x1, y1 = 1000, 1000
x2, y2 = 1000, 1000
grid1 = pygame.Rect(0, 0, blocksize - 10, blocksize - 10)
grid2 = pygame.Rect(200, 0, blocksize - 10, blocksize - 10)
grid3 = pygame.Rect(0, 200, blocksize - 10, blocksize - 10)
grid4 = pygame.Rect(200, 200, blocksize - 10, blocksize - 10)
def draw(hitbox, colour):
    pygame.draw.rect(screen, colour, hitbox)
while True:
    draw(grid1, GRAY)
    draw(grid2, GRAY)
    draw(grid3, GRAY)
    draw(grid4, GRAY)
    block1 = pygame.Rect(x, y, blocksize, blocksize)
    block12 = pygame.Rect(x1, y1, blocksize, blocksize)
    draw(block12, WHITE)
    block13 = pygame.Rect(x2, y2, blocksize, blocksize)
    collidelist = [block1, block12, block13]
    for i in range(1, 9):
        rng = random.randint(1, 4)
        if rng == 1 and not grid1.colliderect(block1) and not grid1.colliderect(block12) and not grid1.colliderect(block13):
            if x == 1000 and y == 1000:
                x = 0
                y = 0
                draw(block1, WHITE)
        if rng == 2 and not grid1.colliderect(block1) and not grid1.colliderect(block12) and not grid1.colliderect(block13):
            if x1 == 1000 and y1 == 1000:
                x1 = 200
                y1 = 0
                draw(block12, WHITE)
        if rng == 3 and not grid1.colliderect(block1) and not grid1.colliderect(block12) and not grid1.colliderect(block13):
            if x2 == 1000 and y2 == 1000:
                x2 = 0
                y2 = 200
                draw(block13, WHITE)
        if rng == 4 and not grid1.colliderect(block1) and not grid1.colliderect(block12) and not grid1.colliderect(block13):
            if x == 1000 and y == 1000:
                x = 200
                y = 200
                draw(block1, WHITE)
            if x1 == 1000 and y1 == 1000:
                x1 = 200
                y1 = 200
                draw(block12, WHITE)
            if x2 == 1000 and y2 == 1000:
                x1 = 200
                y1 = 200
                draw(block13, WHITE)
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
        
        
        
        