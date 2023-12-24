with open('24_2500.txt', 'r') as file:
    string = file.readline()
    summary = 0
    for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        summary += string.count(f'K{i}GE')
    print(summary)
