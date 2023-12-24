for i in range(1000):
    n = str(bin(i))[2:]
    if n.count('1') % 2 == 0:
        n = f'10{n[2:]}0'
    else:
        n = f'11{n[2:]}1'
    if int(n, 2) < 35:
        print(i)
