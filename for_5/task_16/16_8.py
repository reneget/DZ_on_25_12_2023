for i in range(1000):
    n = str(bin(i*2))[2:]
    if n.count('1') % 2 == 0:
        n += '1'
    else:
        n += '0'
    if n.count('1') % 2 == 0:
        n += '1'
    else:
        n += '0'
    if int(n, 2) > 1017:
        print(i - 1)
