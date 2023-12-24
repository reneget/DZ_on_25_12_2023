answer = 0
with open('24_859.txt', 'r') as file:
    for string in file.readlines():
        if string.count('S') == string.count('X'):
            answer += 1
    print(answer)
