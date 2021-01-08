import pygame
import random
from classes import *
#from playground import *


# Создаем игру и окно
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scaffold")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

title = draw_decs(1, WIDTH/2, 100)
dunder = draw_decs(0, WIDTH/2, 150)

#death = draw_decs(2, 800, 450)
#all_sprites.add(death)

all_sprites.add(title)
all_sprites.add(dunder)

words = get_content(0, None)
word = random.choice(words).split('\n')[0]
letters = not_discovered = len(word)
s, used = list(), set()
tries = 1000


for i in range(letters):
    s.append('_')

m = ''.join(s)
write_word(m, all_sprites, a, b)

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    letter = input()
    if letter in word:
        indexes = list()
        l = len(word)
        for i in range(l):
            if word[i] == letter:
                indexes.append(i)

        for ind in indexes:
            s[ind] = letter
        m = ''.join(s)
        write_word(m, all_sprites, a, b)

pygame.quit()