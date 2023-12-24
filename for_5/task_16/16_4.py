for i in range(1000):
    n = str(bin(i))[2:] + str(bin(i))[2:][-1]
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n += '0'
    else:
        n += '1'
    if int(n, 2) > 144:
        print(int(n, 2))
