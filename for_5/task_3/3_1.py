from itertools import product

answer = list()

for string in product('КРЕСЛО', repeat=4):
    if string[0] in 'КРСЛ' and string[-1] in 'ЕО':
        answer.append(string)

print(len(answer))
