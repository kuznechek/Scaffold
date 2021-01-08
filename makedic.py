input = open('dic.txt', 'r', encoding = 'utf-8')
output = open('done_dic.txt', 'w')
k, c, = 0, 0
sp = input.readlines()
for s in sp:
    k += 1
    if '-' not in s and len(s) > 7 and len(s) < 11:
        output.write(s)
        c += 1
input.close()
output.close()
print('Всего слов :', k)
print('Нормальных :', c)







letter = input()
# if letter in used:
# print('Вы уже проверяли эту букву!')
# continue

# used.add(letter)

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


