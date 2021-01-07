input = open('dic.txt', 'r', encoding = 'utf-8')
output = open('done_dic.txt', 'w')
k, c, = 0, 0
sp = input.readlines()
for s in sp:
    k += 1
    if '-' not in s and len(s) > 6:
        output.write(s)
        c += 1
input.close()
output.close()
print('Всего слов :', k)
print('Нормальных :', c)