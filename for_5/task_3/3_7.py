from itertools import permutations, product

answer = list()

for string in permutations('АБИКОЛУН'):
    string = ''.join(string)
    gl = product('АИОУ', repeat=2)
    sgl = product('БКЛН', repeat=2)
    if not any(''.join(element) in string for element in gl):
        if not any(''.join(element) in string for element in sgl):
            answer.append(string)

print(len(answer))
