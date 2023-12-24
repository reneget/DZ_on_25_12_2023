for i in range(1000, 10001):
    n = str(i)
    coples = (int(n[0]) * int(n[1]), int(n[2]) * int(n[3]))
    if str(min(coples)) + str(max(coples)) == '1214':
        print(i)
