from functools import lru_cache


@lru_cache(None)
def f(n):
    answer = 1
    if n >= 1:
        answer += 2 + f(n - 1) + f(n - 3)
    return answer



print(f(40))
