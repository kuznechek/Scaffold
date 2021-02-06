import pygame
import random
import os
import string

game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, 'Assets')

files = ['done_dic.txt', 'rep.txt', 'die.txt']
decorations = ['Dunder.png', 'Title.png', 'FineFin.png']

indexes = list()

# Задаем цвета
WHITE = (240, 240, 240)
BLACK = (0, 0, 15)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (130, 155, 205, 255)

WIDTH = 1040
HEIGHT = 720
FPS = 30

a = 100
b = HEIGHT/2 - 100

class Word():
    def __init__(self, fullname, hidden):
        self.full = fullname
        self.game = hidden
        self.letters = len(fullname)
        self.undiscovered = set(fullname)

    def update(self, letter):
        progress = list(self.game)
        for i in range(len(self.full)):
            if self.full[i] == letter:
                progress[i] = letter
        self.undiscovered.remove(letter)
        self.game = ''.join(progress)

    def draw(self, group, a, b):
        for k in self.game:
            block = draw_block(k, a, b)
            group.add(block)
            a += 70

def draw_block(letter, x, y):
    letter = letter.upper()
    image = pygame.image.load(os.path.join(assets_folder, letter+'.png'))
    block = Rectangle(letter, image, x, y)
    return block

def draw_decs(n, x, y):
    image = pygame.image.load(os.path.join(assets_folder, decorations[n]))
    block = Rectangle('dec',image, x, y)
    return block

def draw_alphabet():
    w0 = WIDTH / 10
    w,k,h = w0, 80, HEIGHT / 1.7
    x, y = 1040, 1051
    alphabet = set()
    for j in range(3):
        for i in range(x, y):
            alphabet.add(draw_block(chr(i), w, h))
            w += k
        w, x, y, h = w0, x+11, y+11, h+100
    return alphabet

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, name, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def check_collisions(self, coord):
        x, y = coord[0], coord[1]
        if x >= self.rect[0] and x <= self.rect[2] + self.rect[0]:
            if y >= self.rect[1] and y <= self.rect[3] + self.rect[1]:
                #self.kill()
                return True
        return False

    def kill_me(self):
        print('"' + self.name + '" WAS KILLED.')
        self.kill()

class Click(pygame.sprite.Sprite):
    def __init__(self, coord, r):
        self.center = coord
        self.radius = r
        self.colour = RED

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.center, self.radius)

def get_content(index, code):
    file_input = open(files[index], 'r', encoding=code)
    strings = file_input.readlines()
    file_input.close()
    return strings

def output(result):
    strings = get_content(result, 'utf-8')
    for s in strings:
        print(s.split('\n')[0])