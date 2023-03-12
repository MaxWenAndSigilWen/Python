import pygame
import random
RNG = random.randint(0, 2)
pygame.init()
screen = pygame.display.set_mode((300, 200))
x = 30
y = 100
ya = 90
xa = 275
speed = 15
lev = 0
point = 0
font = pygame.font.Font(None, 40)
text = font.render("Press e to start", False, (0, 255, 0))
text2 = font.render("Press space to jump", False, (0, 255, 0))
textlev1 = font.render("You have", False, (0, 255, 0))
textlev2 = font.render("selected:", False, (0, 255, 0))
text3 = font.render("Choose a difficulty", False, (0, 255, 0))
text32 = font.render("by entering a number:", False, (0, 255, 0))
text4 = font.render("1easy 2medium 3hard", False, (0, 255, 0))
clock = pygame.time.Clock()
pointval = 1
while True:
   screen.blit(text, (50, 100))
   screen.blit(text2, (20, 150))
   screen.blit(text3, (0, 0))
   screen.blit(text32, (0, 30))
   screen.blit(text4, (0, 60))
   keys = pygame.key.get_pressed()
   if keys[pygame.K_1]:
       speed = 10
       lev = 1
       pointval = 1
   elif keys[pygame.K_2]:
       speed = 15
       lev = 2
       pointval = 2
   elif keys[pygame.K_3]:
       speed = 20
       lev = 3
       pointval = 3
   if lev == 1:
       screen.fill((0, 0, 0))
       screen.blit(text, (50, 100))
       screen.blit(text2, (20, 150))
       screen.blit(textlev1, (0, 0))
       screen.blit(textlev2, (0, 30))
       screen.blit(font.render("easy mode", False, (0, 255, 0)), (0, 60))
       pygame.display.update()
   elif lev == 2:
       screen.fill((0, 0, 0))
       screen.blit(text, (50, 100))
       screen.blit(text2, (20, 150))
       screen.blit(textlev1, (0, 0))
       screen.blit(textlev2, (0, 30))
       screen.blit(font.render("medium mode", False, (0, 255, 0)), (0, 60))
       pygame.display.update()
   elif lev == 3:
       screen.fill((0, 0, 0))
       screen.blit(text, (50, 100))
       screen.blit(text2, (20, 150))
       screen.blit(textlev1, (0, 0))
       screen.blit(textlev2, (0, 30))
       screen.blit(font.render("hard mode", False, (0, 255, 0)), (0, 60))
       pygame.display.update()
   keys = pygame.key.get_pressed()
   if keys[pygame.K_e]:
       while True:
           screen.fill((50, 0, 0))
           points = str(point)
           pointext = font.render("Points:" + points, False, (0, 255, 0))
           birb = pygame.Rect(x, y, 25, 25)
           attack = pygame.Rect(xa, ya, 50, 25)
           pygame.draw.rect(screen, (255, 255, 0), birb, 100, 100)
           pygame.draw.rect(screen, (255, 0, 0), attack)
           if RNG == 0:
               ya = 40
               xa -= speed
               if xa <= 0:
                   xa = 275
                   RNG = random.randint(0, 2)
                   point += pointval
           elif RNG == 1:
               ya = 90
               xa -= speed
               if xa <= 0:
                   xa = 275
                   RNG = random.randint(0, 2)
                   point += pointval
           elif RNG == 2:
               ya = 140
               xa -= speed
               if xa <= 0:
                   xa = 275
                   RNG = random.randint(0, 2)
                   point += pointval
           y += 3
           keys = pygame.key.get_pressed()
           if keys[pygame.K_SPACE]:
               y -= 6
           floor = pygame.Rect(0, 185, 300, 15)
           roof = pygame.Rect(0, 0, 300, 15)
           pygame.draw.rect(screen, (255, 0, 0), floor)
           pygame.draw.rect(screen, (255, 0, 0), roof)
           screen.blit(pointext, (0, 0))
           if birb.colliderect(floor) or birb.colliderect(roof) or birb.colliderect(attack):
               exit()
           pygame.display.update()
           clock.tick(30)
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit()
           screen.fill((0, 0, 0))
           pygame.display.flip()
   pygame.display.update()
   clock.tick(30)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit()
   screen.fill((0, 0, 0))
   pygame.display.flip()
