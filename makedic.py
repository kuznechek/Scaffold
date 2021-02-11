import string

input = open('Словарь.txt', 'r', encoding = 'utf-8')
output = open('done_dic.txt', 'w')
k, c, = 0, 0
sp = input.readlines()
for w in sp:
    k += 1
    w = w.upper().split()[0]
    if len(w) < 11 and len(w) > 2:
        w = w.replace('E', 'Е')
        w = w.replace('Y', 'У')
        output.write(w + "\n")
        print(w, len(w))
        c += 1
input.close()
output.close()
print('Всего слов :', k)
print('Нормальных :', c)