import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()


cell_size = 30
cell_number = 20
Score = 0
Level = 1

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)


class Player:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.im = pygame.image.load("PygameTutorial_3_0/Player.png")
        self.im = pygame.transform.scale(self.im, (70,100))
        
    
    def image(self):
        return self.im.get_rect(center = (self.x, self.y))
    

    def damage(self):
        pass




class Enemy:
    def __init__(self, x_pos , y_pos, speed):
        self.im = pygame.image.load("PygameTutorial_3_0/Enemy.png")
        self.x = x_pos
        self.y = y_pos
        self.speed = speed


    def image(self):
        enemy = self.im.get_rect(midbottom = (self.x, self.y))
        return enemy


    






        


screen = pygame.display.set_mode((cell_size * cell_number, cell_number * cell_size))

font = pygame.font.Font("font/Pixeltype.ttf", 50)
message = font.render("GAME OVER", True, Red)
message_rect = message.get_rect(center=((cell_number * cell_size) // 2, (cell_number * cell_size) // 2))

bg = pygame.image.load("PygameTutorial_3_0/AnimatedStreet.png")
bg = pygame.transform.scale(bg, (cell_size * cell_number, cell_number * cell_size))
bg_rect = bg.get_rect(topleft = (0, 0))


done = False
pl_x = 300
pl_y = 500
enemy_pos_y = -1
# enemy_pos_x = random.randint(1, cell_number) * cell_size
enemy_pos_x = random.randint(100, 500)
speed = 5


while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    pygame.display.set_caption(f"Level: {Level}         RACER         Score: {Score}")

        
        


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        pl_x -= 10
    elif key[pygame.K_RIGHT]:
        pl_x += 10        


    




    
    player = Player(pl_x, pl_y)
    enemy = Enemy(enemy_pos_x,enemy_pos_y, speed)
    
    enem = enemy.image()
    car = player.image()
    enemy_pos_y += speed




    if car.colliderect(enem) or car.left > 500 or car.right < 100:
        screen.fill(White)
        screen.blit(message, message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  
        done = True
        break  


    
    
    screen.blit(bg, bg_rect)
    screen.blit(player.im, car)
    screen.blit(enemy.im, enem)


    if enem.top > 600:
        enemy_pos_x = random.randint(100, 500) 
        enemy_pos_y = -1
        Score += 1

    if Score > 5:
        Level += 1
        Score = 0
        speed += 5


   

    
    pygame.display.flip()
    clock.tick(60)


