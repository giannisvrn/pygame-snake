import random
import pygame 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
screen_color = (255,229,204)

player = pygame.Rect((300,250,20,20))
player_color = (255,0,0)

spawned = 0

def spawn():
    y = random.randint(100,200)
    x = random.randint(100,200)

    enemy = pygame.Rect((x,y,20,20))
    return enemy


while True:
    screen.fill(screen_color)

    pygame.draw.rect(screen,player_color,player)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
        
    if spawned == 0:
        enemy = spawn()
        spawned = 1
    
    pygame.draw.rect(screen,(0,0,0),enemy)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()
        
    pygame.display.update()