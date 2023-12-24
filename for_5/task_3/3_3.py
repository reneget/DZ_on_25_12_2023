from itertools import product

answer = list()

for string in product('ПУЛЯ', repeat=6):
    if string.count('У') == 2:
        answer.append(string)

print(len(answer))
