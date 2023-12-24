for i in range(1000):
    n = int(str(bin(i))[2:][::-1], 2)
    if n == 13 and i < 100:
        print(i)