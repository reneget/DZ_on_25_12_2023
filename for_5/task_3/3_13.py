from itertools import product

answer = list()

for string in product('ГЕПАРД', repeat=5):
    if string.count('Г') == 1 and string[0] != 'А' and string[-1] != 'Е':
        answer.append(string)

print(len(answer))