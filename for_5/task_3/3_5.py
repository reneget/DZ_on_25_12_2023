from itertools import product

answer = list()

for string in product('САЛО', repeat=6):
    if 4 > string.count('О') > 0:
        answer.append(string)

print(len(answer))