import pygame
import random
pygame.init()
# variables
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
killx, killy = 300, 1000
killx2, killy2 = 300, 1000
killx3 , killy3 = 300, 1000
kill1c = 0
kill2c = 0 
kill3c = 0
kill1off = False
kill2off = False
kill3off = False
y = 200
sped = 5
G = 5
Gac = 3 # gravity acceleration
point = 0
font = pygame.font.Font(None, 40)
sped = 5
while True:
    screen.fill((135, 206, 235))
    # variables     
    RNG = random.randint(0, 2)
    points = str(point)
    keys = pygame.key.get_pressed()
    pointext = font.render("Points:" + points, False, (0, 255, 0))   
    # killx position
    killx2 -= sped
    killx3 -= sped
    killx -= sped
    # gravity
    y += G
    G += Gac
    # rect variables
    floor = pygame.Rect(0, 240, 300, 60)
    birb = pygame.Rect(100, y, 30, 30)
    killbrick = pygame.Rect(killx, killy, 30, 30)
    wall = pygame.Rect(killx2, killy2, 60, 50)
    killwall = pygame.Rect(killx2, killy2 + 5, 30, 45)
    killbrick2 = pygame.Rect(killx3, killy3, 30, 45)
    # output variables
    screen.blit(pointext, (0, 0))
    pygame.draw.rect(screen, (255, 0, 255), birb)
    pygame.draw.rect(screen, (0, 255, 0), floor)
    pygame.draw.rect(screen, (255, 0, 0), killbrick)
    pygame.draw.rect(screen, (255, 0, 0), killbrick2)
    pygame.draw.rect(screen, (0, 255, 0), wall)
    # if statments    
    # obstical teleport  
    if killx <= -60:
        killy = 1000
        kill1off = True
    if killx2 <= -60:
        killy2 = 1000
        kill2off = True
    if killx3 <= -60:
        killy3 = 1000
        kill3off = True
    if RNG == 0 and kill1c >= 30:
        killy = 215
        killx = 300
        kill1off = False
        kill1c = 0
    if RNG == 1 and kill2c >= 60:
        killy2 = 195
        killx2 = 300
        kill2off = False
        kill2c = 0
    if RNG == 2 and kill3c >= 90:
        killy3 = 200
        killx3 = 300
        kill3off = False
        kill3c = 0
    # waiting
    if kill1off: kill1c += 1
    if kill2off: kill2c += 1
    if kill3off: kill3c += 1
    # floor
    if birb.colliderect(floor) or birb.colliderect(wall):
        G = 0
        Gac = 2
        G -= Gac
        if keys[pygame.K_SPACE]:
            G -= 20
    # kill make kill
    if birb.colliderect(killbrick) or birb.colliderect(killwall) or birb.colliderect(killbrick2):
        exit()
    # standard reset for pygame
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
