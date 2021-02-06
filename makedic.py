input = open('Словарь.txt', 'r', encoding = 'utf-8')
output = open('done_dic.txt', 'w')
k, c, = 0, 0
sp = input.readlines()
for s in sp:
    k += 1
    if '-' not in s and len(s) < 11:
        output.write(s.lower())
        c += 1
input.close()
output.close()
print('Всего слов :', k)
print('Нормальных :', c)




if letter in word:
    indexes = list()
    l = len(word)
    for i in range(l):
        if word[i] == letter:
            indexes.append(i)

    for ind in indexes:
        s[ind] = letter
    hidden_word = ''.join(s)
    write_word(hidden_word, all_sprites, a, b)
