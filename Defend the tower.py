import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
colour = (0, 255, 0)
rng1 = random.randint(1, 590)
rng2 = random.randint(1, 590)
rng3 = random.randint(1, 590)
point = 0
health = 600
dificulty = 3
move1 = 0
move2 = 0
move3 = 0
purchase = 0
jab = 15
end = 5
defensehealth = 10
deletedefense = 0
keys = pygame.key.get_pressed()
def draw(hitbox, colour):
    pygame.draw.rect(screen, colour, hitbox)
class enemy:
    def __init__(self, enyx, enyy):
        self.x, self.y = x, y
        self.eny = pygame.Rect(enyx, enyy, 10, 10)
        pygame.draw.rect(screen, (255, 0, 0), self.eny)
while True:
    shop = font.render("Press e when you have more", False, colour)
    shop2 = font.render("than 50 points to get a defense", False, colour)
    instuc = font.render("Press space to jab", False, colour)
    chat = font.render("Press v to close instructions", False, colour)
    chat3 = font.render("Press c to open chat", False, colour)
    screen.blit(shop, (0, 40))
    screen.blit(shop2, (0, 80))
    screen.blit(instuc, (0, 120))
    screen.blit(chat, (0, 160))
    screen.blit(chat3, (0, 200))
    keys = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    tower = pygame.Rect(0, 385, health, 15)
    defense = pygame.Rect(deletedefense, 350, 600, defensehealth)
    sword = pygame.Rect(x - 7.5, 240 + jab, 15, 60)
    player = pygame.Rect(x - 15, 300, 30, 30)
    draw(tower, (175, 175, 175))
    draw(defense, (240, 240, 240))
    draw(sword, (255, 0, 0))
    draw(player, (0, 0, 255))
    if keys[pygame.K_SPACE]:
        jab = 0
        sword = pygame.Rect(x - 7.5, 240 + jab, 15, 60)
        draw(sword, (255, 0, 0))
        for i in range(30):
            if i >= 29:
                jab = 15
    enemy1 = enemy(rng1, move1)
    enemy2 = enemy(rng2, move2)
    enemy3 = enemy(rng3, move3)
    if defense.colliderect(enemy1.eny):
        defensehealth -= 1
        rng1 = random.randint(1, 590)
        move1 = 0
    if defense.colliderect(enemy2.eny):
        defensehealth -= 1
        rng2 = random.randint(1, 590)
        move2 = 0
    if defense.colliderect(enemy3.eny):
        defensehealth -= 1
        rng3 = random.randint(1, 590)
        move3 = 0
    if defensehealth <= 0:
        deletedefense = 1000000
    if sword.colliderect(enemy1.eny):
        rng1 = random.randint(1, 590)
        move1 = 0
        point += 1
    if sword.colliderect(enemy2.eny):
        rng2 = random.randint(1, 590)
        move2 = 0
        point += 1
    if sword.colliderect(enemy3.eny):
        rng3 = random.randint(1, 590)
        move3 = 0
        point += 1
    if move1 >= 385:
        rng1 = random.randint(1, 590)
        move1 = 0
        health -= 30
    if move2 >= 385:
        rng2 = random.randint(1, 590)
        move2 = 0
        health -= 30
    if move3 >= 385:
        rng3 = random.randint(1, 590)
        move3 = 0
        health -= 30
    pointfinal = str(point + (50*purchase))
    if health <= 0:
        screen.fill((0, 0, 0))
        screen.blit(font.render("You got a total of" + pointfinal, False, (255, 255, 255)), (100, 180))
        end = 0
    if keys[pygame.K_e] and point >= 50:
        defensehealth = 10
        deletedefense = 0
        point -= 50
        purchase += 1
    if keys[pygame.K_v]:
        colour = (0, 0, 0)
    if keys[pygame.K_c]:
        colour = (0, 255, 0)
    move1 += end
    move2 += end
    move3 += end
    points = str(point)
    pointext = font.render("Points:" + points, False, (0, 255, 0))
    screen.blit(pointext, (0, 0))
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()