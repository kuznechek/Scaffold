import pygame
import random
import sys
from classes import *
#from playground import *

# Создаем игру и окно
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Виселица")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# Цикл игры
while True:
    # Спрайты декорации
    title = draw_decs(1, WIDTH / 2, 100)
    dunder = draw_decs(0, WIDTH / 2, 150)

    # Выбор слова
    words = get_content(0, None)
    word = random.choice(words).split('\n')[0]
    letters = not_discovered = len(word)
    s, used = list(), set()
    tries = 1000

    for i in range(letters):
        s.append('_')

    hidden_word = ''.join(s)
    write_word(hidden_word, all_sprites, a, b)
    for letter in draw_alphabet():
        all_sprites.add(letter)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for sprite in all_sprites:
                    sprite.update()
            # Рендеринг
            screen.fill(BLACK)
            all_sprites.draw(screen)
            # После отрисовки всего, переворачиваем экран
            pygame.display.flip()


pygame.quit()