import pygame
import random


pygame.init()
cell_size = 40
cell_number = 20
clock = pygame.time.Clock()
done = False
score = 0

color_red  = (255,0,0)
color_green = (0,255,0)
color_white = (255,255,255)

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
font = pygame.font.Font("font/Pixeltype.ttf", 50)


x_pos = 0
y_pos = 0
x_f = 0
y_f = 0
x_ch = (cell_number // 2) * cell_size
y_ch = (cell_number // 2) * cell_size
length = 2
snake_lst = [[x_ch, y_ch]]
direction = "UP"
fps = 5
level = 1

def game_over(x, y):
    if x < -1 or x > (cell_number * cell_size)  or y < -1 or y > (cell_number * cell_size) :
        return True
    return False

def fruit():
    while True:
        x = random.randint(0, cell_number - 1) * cell_size
        y = random.randint(0, cell_number - 1) * cell_size
        if [x, y] not in snake_lst:  
            return x, y
x_f, y_f = fruit()


def draw_snake():
    for x in snake_lst:
        pygame.draw.rect(screen, color_green, (x[0], x[1], cell_size, cell_size))



while not done:
   
    pygame.display.set_caption(f"Score: {score} Level: {level}")
    screen.fill(color_white)
    if score == 5 and level == 1:
        score = 0
        level += 1
        fps = 10
    
    elif score == 10 and level == 2:
        score = 0
        level += 1
        fps = 15
    elif score == 5 and level == 3:
        score = 0
        level += 1
        fps = 30

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"

    
    if direction == "UP":
        y_pos = -cell_size
        x_pos = 0
    elif direction == "DOWN":
        y_pos = cell_size
        x_pos = 0
    elif direction == "RIGHT":
        x_pos = cell_size
        y_pos = 0
    elif direction == "LEFT":
        x_pos = -cell_size
        y_pos = 0



     
    x_ch += x_pos
    y_ch += y_pos
    
    if game_over(x_ch, y_ch) or [x_ch, y_ch] in snake_lst:
        screen.fill(color_white)
        message = font.render("GAME OVER", True, color_red)
        message_rect = message.get_rect(center=((cell_number * cell_size) // 2, (cell_number * cell_size) // 2))
        screen.blit(message, message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  
        done = True
        break  

    snake_lst.append([x_ch, y_ch])

    if len(snake_lst) > length:
        del snake_lst[0]
                
               

    if x_ch == x_f and y_ch == y_f:
        score += 1
        length += 1
        x_f, y_f = fruit() 

    
    pygame.draw.rect(screen, color_red, (x_f, y_f, cell_size, cell_size)) # fruits
    draw_snake()
   






            
            





    clock.tick(fps)
    pygame.display.flip()


        
pygame.quit()
