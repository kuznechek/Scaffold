import pygame
import random
import os

game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, 'Assets')

files = ['done_dic.txt', 'rep.txt', 'die.txt']
decorations = ['Dunder.png', 'Title.png', 'FineFin.png']

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
b = HEIGHT/2

def write_word(w, alls, a, b):
    for k in w:
        block = draw_block(k, a, b)
        alls.add(block)
        a += 70

def get_content(index, code):
    file_input = open(files[index], 'r', encoding=code)
    strings = file_input.readlines()
    file_input.close()
    return strings

def output(result):
    strings = get_content(result, 'utf-8')
    for s in strings:
        print(s.split('\n')[0])


def draw_block(letter, x, y):
    letter = letter.upper()
    image = pygame.image.load(os.path.join(assets_folder, letter+'.png'))
    block = Rectangle(image, x, y)
    return block

def draw_decs(n, x, y):
    image = pygame.image.load(os.path.join(assets_folder, decorations[n]))
    block = Rectangle(image, x, y)
    return block



class Rectangle(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
