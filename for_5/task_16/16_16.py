for i in range(100, 1001):
    n = str(i)
    coples = (int(n[0]) ** 2 + int(n[1]) ** 2, int(n[1]) ** 2 + int(n[2]) ** 2)
    if str(max(coples)) + str(min(coples)) == '9010':
        print(i)
