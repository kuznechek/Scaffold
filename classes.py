import pygame
import random
import os
import string

game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, 'Assets')

files = ['done_dic.txt', 'rep.txt', 'die.txt']
decs = ['Dunder.png', 'Title.png', 'FineFin.png', 'Bg.png']
screamers = ['Scream1.png', 'Scream2.png', 'Scream3.png']

indexes = list()

# Задаем цвета
WHITE = (240, 240, 240)
BLACK = (0, 0, 15)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (130, 155, 205, 255)

WIDTH = 1280
HEIGHT = 720
FPS = 15

a = 100
b = HEIGHT/2 - 100

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
        self.kill()

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
        for obj in group:
            if obj.name in self.game and obj.name in self.full:
                obj.kill_me()
        for obj in self.game:
            block = draw_block(obj, a, b)
            group.add(block)
            a += 70

def draw_block(letter, x, y):
    letter = letter.upper()
    image = pygame.image.load(os.path.join(assets_folder, letter+'.png'))
    block = Rectangle(letter, image, x, y)
    return block

def draw_decs(n, x, y, fd):
    image = pygame.image.load(os.path.join(assets_folder, fd[n]))
    block = Rectangle('dec',image, x, y)
    return block

def draw_alphabet():
    w0 = WIDTH / 20
    w, k, h = w0, 80, HEIGHT / 1.7
    alphabet_full = get_full_alphabet()
    alphabet, d = set(), 0
    for j in range(2):
        for i in range(11):
            alphabet.add(draw_block(alphabet_full[i+d], w, h))
            w += k
        w, h, d = w0, h+100, d+11
    for i in range(23, 33):
        alphabet.add(draw_block(alphabet_full[i], w, h))
        w += k
    return alphabet

def get_full_alphabet():
    x, y = 1040, 1072
    alphabet = list()
    for i in range(x, x + 6):
        alphabet.append(chr(i))
    alphabet.append('Ё')
    for i in range(x + 6, y):
        alphabet.append(chr(i))
    return alphabet

def get_content(index, code):
    file_input = open(files[index], 'r', encoding=code)
    strings = file_input.readlines()
    file_input.close()
    return strings

def output(result):
    strings = get_content(result, 'utf-8')
    for s in strings:
        print(s.split('\n')[0])