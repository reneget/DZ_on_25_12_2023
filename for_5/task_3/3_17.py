from itertools import permutations

answer = set()

for string in permutations('МИМИКРИЯ'):
    answer.add(string)

print(len(answer))
