from itertools import product

answer = list()

for string in product('01234', repeat=6):
    if string[0] in '234' and string[-1] not in '34':
        answer.append(string)

print(len(answer))