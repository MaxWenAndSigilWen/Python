import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
blocksize = 200
replay = 1
grid1 = pygame.Rect(0, 0, blocksize - 10, blocksize - 10)
grid2 = pygame.Rect(200, 0, blocksize - 10, blocksize - 10)
grid3 = pygame.Rect(0, 200, blocksize - 10, blocksize - 10)
grid4 = pygame.Rect(200, 200, blocksize - 10, blocksize - 10)
def draw(hitbox, colour):
    pygame.draw.rect(screen, colour, hitbox)

class block:
    def __init__(self, x, y, cubed) -> None:
        self.keys = [x,y,cubed]
    def build(self):
        return pygame.Rect(self.keys[0], self.keys[1], self.keys[2], self.keys[2])
    
    @property
    def getX(self):
        return self.keys[0]
    @getX.setter
    def getX(self, val):
        self.keys[0] = val
    @property
    def getY(self):
        return self.keys[1]
    @getY.setter
    def getY(self, val):
        self.keys[1] = val

objects = [] # type: list[block]
for i in range(9):
    objects.append(block(1000, 1000, 200))
while True:
    draw(grid1, GRAY)
    draw(grid2, GRAY)
    draw(grid3, GRAY)
    draw(grid4, GRAY)
    if keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s]:
        rand = random.randint(0, len(objects) - 1)
        draw(objects[rand].build(), WHITE)
    RNG = random.randint(1, 4)
    for i in objects:
        collide_list = [x.build() for x in objects]
        if RNG == 1 and len(grid1.collidelistall(collide_list)) == 0:
            if i.getX == 1000 and i.getY == 1000:
                i.getX = 0
                i.getY = 0
        if RNG == 2 and len(grid2.collidelistall(collide_list)) == 0:
            if i.getX == 1000 and i.getY == 1000:
                i.getX = 200
                i.getY = 0
        if RNG == 3 and len(grid3.collidelistall(collide_list)) == 0:
            if i.getX == 1000 and i.getY == 1000:
                i.getX = 0
                i.getY = 200
        if RNG == 4 and len(grid4.collidelistall(collide_list)) == 0:
            if i.getX == 1000 and i.getY == 1000:
                i.getX = 200
                i.getY = 200
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
