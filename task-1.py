# Задача 34
text = input().split()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
count = list()
for i in text:
    c = 0
    for j in i:
        if j in volwes:
            c += 1
    count.append(c)
if len(set(count)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')