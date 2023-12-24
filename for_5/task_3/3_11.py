from itertools import product

answer = list()

for string in product('ВИШНЯ', repeat=6):
    if string.count('В') < 2 and string[0] != 'Ш' and string[-1] not in 'ИЯ':
        answer.append(string)

print(len(answer))