import os
import sys
import pygame

pygame.init()
FPS = 50
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

sound = pygame.mixer.Sound('data/in.wav')
vol = 1

# Главный Игровой цикл
running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            channel = sound.play()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            vol += 0.1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            vol -= .1
    sound.set_volume(vol)
    screen.fill(pygame.Color(0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
