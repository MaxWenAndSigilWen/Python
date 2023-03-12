import pygame
# Default variable
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
eny = 0
enym = 1
enx = 10
eny2 = 300
enx2 = 280
enym2 = -1
class bullet:
    def __init__(self, bx, by):
        self.x = bx
        self.y = by
        bullethit = pygame.Rect(bx, by, 20, 20)
        bullet1 = pygame.draw.rect(screen, (0,0,255), bullethit)
while True:
    # Variables
    x, y = pygame.mouse.get_pos()
    print(x, y)
    # Hitbox variables
    verticalaim = pygame.Rect(x - 1.5, 0, 3, 300)
    horizontalaim = pygame.Rect(0, y - 1.5, 300, 3)
    enemy = pygame.Rect(enx, eny, 10, 10)
    enemy2 = pygame.Rect(enx2, eny2, 10, 10)
    # Draw rects
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (255, 0, 0), enemy2)
    pygame.draw.circle(screen, (0,0,255), (150, 150), 10, 10)
    pygame.draw.rect(screen, (255, 255, 255), horizontalaim)
    pygame.draw.rect(screen, (255, 255, 255), verticalaim)
    # Movement
    if keys[pygame.K_SPACE]:
        bullet(x, y)
    eny += enym
    eny2 += enym2
    if eny2 <= 0:
        enx2 -= 5
        enym2 = 1
    if eny2 >= 300:
        enx2 -= 5
        enym2 = -1
    if eny >= 300:
        enym = -1
        enx += 5
    if eny <= 0:
        enym = 1
        enx += 5
    # Standard reset for pygame
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((0, 0, 0))
    pygame.display.flip()
