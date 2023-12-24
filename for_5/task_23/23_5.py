with open('24_2498.txt', 'r') as file:
    string = file.readline()
    while 'XIXIX' in string:
        string = string.replace('XIXIX', 'XIX XIX')
    print(string.count('XIX'))
