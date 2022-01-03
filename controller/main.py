import os, sys 

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
    
from player import Player
from asteroid import Asteroid
from shot import Shot
import pygame
import random


pygame.init()

display = pygame.display.set_mode([840, 400])
pygame.display.set_caption('2D GAME')

objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

'''
bg = pygame.sprit.Sprite(objectGroup)
bg.image = pygame.image.load()
bg.image = pygame.transform.scale(bg.image, [840, 400])
bg.rect = bg.image.get_rect()
'''

player = Player(objectGroup)

pygame.mixer.music.load("audio/music.ogg")
pygame.mixer.music.play(-1)

effect = pygame.mixer.Sound('audio/laser.wav')

gameLoop = True
gameOver = False
timer = 20
clock = pygame.time.Clock()
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    effect.play()
                    shot = Shot(objectGroup, shotGroup)
                    shot.rect.center = player.rect.center
        if not gameOver:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    asteroid = Asteroid(objectGroup, asteroidGroup)

            collisions = pygame.sprite.spritecollide(
                player, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("Game Over!")
                gameOver = True

            hits = pygame.sprite.groupcollide(
                shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

        display.fill([0, 0, 0])  # DRAW GAME
        objectGroup.draw(display)

        pygame.display.update()
