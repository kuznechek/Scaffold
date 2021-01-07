import random
import string

files = ['done_dic.txt', 'rep.txt', 'die.txt']

def get_content(index, code):
    file_input = open(files[index], 'r', encoding=code)
    sp = file_input.readlines()
    file_input.close()
    return sp

def output(result):
    strings = get_content(result, 'utf-8')
    for s in strings:
        print(s)

print('Добро пожаловать в игру "Виселица". Пожалуйста, выберите уровень:')
print('1 - Лёгкий - нет ограничений по ошибкам')
print('2 - Средний - вы можете умереть.')
print('3 - Сложный: действуйте на свой страх и риск!')
print('4 - Нереальный. Можно ошибиться только трижды.')
print('\nВведите выбранный уровень сложности в виде цифры и нажмите Enter.')
while 1:
    lvl = int(input())
    if lvl == 1:
        tries = 33
        print('Большое начинается с малого. Удачи!')
        break
    elif lvl == 2:
        tries = 12
        print('Хорошей игры.')
        break
    elif lvl == 3:
        tries = 6
        print('Удача любит смелых')
        break
    elif lvl == 4:
        tries = 3
        print('А фокус очень простой: не думайте о боли.')
        break
    else:
        print('Возьмите себя в руки! Тут всего четыре варианта.')

words = get_content(0, None)
word = random.choice(words).split('\n')[0]
letters = not_discovered = len(word)
s, used = list(), set()

for i in range(letters):
    s.append('_')
print('В загаданном слове', letters, 'букв')
print(' '.join(s))

while not_discovered > 0:
    letter = input()
    if letter in used:
        print('Вы уже проверяли эту букву!')
        continue

    used.add(letter)

    if letter in word:
        indexes = list()
        l = len(word)

        for i in range(l):
            if word[i] == letter:
                indexes.append(i)

        for ind in indexes:
            s[ind] = letter

        not_discovered -= len(indexes)
        print(' '.join(s))

        if not_discovered != 0:
            print('Осталось отгадать', not_discovered, 'букв')
        else:
            print('Поздравляю! Слово отгадано!')
            output(1)
    else:
        if tries > 1:
            print('Такой буквы нет в слове. Попробуйте другую!')
            tries -= 1
            print('Осталось попыток', tries)
        else:
            print('Вы будете повешены за шею, пока не умрёте.')
            print('А загаданное слово:', word)
            output(2)
            break