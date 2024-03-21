import pygame 
import time 
import os
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1400, 800))


ANIMALS_WIDTH, ANIMALS_HEIGHT = 1000, 1000

# Load dog image
dog_image = pygame.image.load(os.path.join("pictures_forest", "dog.png"))
# Scale and rotate the dog 
dog = pygame.transform.rotate(pygame.transform.scale(dog_image, (ANIMALS_WIDTH, ANIMALS_HEIGHT)), 30)


# Load cat image
cat_image = pygame.image.load(os.path.join("pictures_forest", "cat.png"))
# Scale and rotate the cat 
cat = pygame.transform.rotate(pygame.transform.scale(cat_image, (ANIMALS_WIDTH, ANIMALS_HEIGHT)), 1000)


bg_image = pygame.image.load(os.path.join("pictures_forest", "forest.jpg"))


# Initial positions for dog and cat
dog_x = 0
dog_y = 0
cat_x = 1000
cat_y = 0

# Movement keys lists thing
keys_dog = [False, False, False, False]
keys_cat = [False, False, False, False]

background_color = (115, 215, 255)  
screen.fill(background_color)

# Main game loop for dog and cat 
running = True
while running:
    screen.blit(bg_image, (0, 0))
    screen.blit(dog_image, (dog_x, dog_y))
    screen.blit(cat_image, (cat_x, cat_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys_dog[0] = True
            elif event.key == pygame.K_LEFT:
                keys_dog[1] = True
            elif event.key == pygame.K_DOWN:
                keys_dog[2] = True
            elif event.key == pygame.K_RIGHT:
                keys_dog[3] = True
            elif event.key == pygame.K_w:
                keys_cat[0] = True
            elif event.key == pygame.K_a:
                keys_cat[1] = True
            elif event.key == pygame.K_s:
                keys_cat[2] = True
            elif event.key == pygame.K_d:
                keys_cat[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys_dog[0] = False
            elif event.key == pygame.K_LEFT:
                keys_dog[1] = False
            elif event.key == pygame.K_DOWN:
                keys_dog[2] = False
            elif event.key == pygame.K_RIGHT:
                keys_dog[3] = False
            elif event.key == pygame.K_w:
                keys_cat[0] = False
            elif event.key == pygame.K_a:
                keys_cat[1] = False
            elif event.key == pygame.K_s:
                keys_cat[2] = False
            elif event.key == pygame.K_d:
                keys_cat[3] = False

    # Dog movement 
    if keys_dog[0] and dog_y > 0:
        dog_y -= 20 
    if keys_dog[2] and dog_y < 400:
        dog_y += 20
    if keys_dog[1] and dog_x > 0:
        dog_x -= 8
    if keys_dog[3] and dog_x < 1100:
        dog_x += 8

    # Cat movement
    if keys_cat[0] and cat_y > 0:
        cat_y -= 20 
    if keys_cat[2] and cat_y < 400:
        cat_y += 20
    if keys_cat[1] and cat_x > 0:
        cat_x -= 8
    if keys_cat[3] and cat_x < 1100:
        cat_x += 8

    time.sleep(0.05)

pygame.quit()