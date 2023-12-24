for i in range(1000):
    n = str(bin(i))[2:]
    if i % 2 == 0:
        n += '01'
    else:
        n += '10'
    if int(n, 2) > 81:
        print(int(n, 2))
        