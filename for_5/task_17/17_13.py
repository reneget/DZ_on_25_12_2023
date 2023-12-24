answer = []


def f(n):
    if n <= 18:
        return 3 + n
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n - 1) + n ** 2 + 5


for i in range(1, 1001):
    if all(int(element) % 2 == 0 for element in str(f(i))):
        answer.append(i)
print(len(answer))
