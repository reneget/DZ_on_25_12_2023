answer = []


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n/2)
    if n > 0 and n % 2 != 0:
        return f(n - 1) + 1


for i in range(1, 501):
    if f(i) == 8:
        answer.append(i)
print(len(answer))
