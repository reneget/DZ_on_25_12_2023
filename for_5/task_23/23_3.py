with open('24_314.txt', 'r') as file:
    string = file.readline()
    print(string.count('OCK') - string.count('STOCK'))
