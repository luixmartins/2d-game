import pygame as pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.speed += self.acceleration
            self.rect.y += 1
        elif keys[pygame.K_w]:
            self.speed -= self.acceleration
            self.rect.y -= 1
        else:
            self.speed *= 0.95

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 400:
            self.rect.bottom = 400
            self.speed = 0
