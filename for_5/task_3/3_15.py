from itertools import permutations

answer = list()

for string in permutations('ДЕЙКСТРА', 6):
    string = ''.join(string)
    if string.count('Й') == 1 and ('ЙЕ' not in string and 'ЙА' not in string) and string[-1] != 'Й':
        answer.append(string)

print(len(answer))