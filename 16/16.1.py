# import sys, functools
# sys.setrecursionlimit(9999999)


# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 0:
#         return f(n - 1) + n - 1
#     if n > 2 and n % 2 != 0:
#         return f(n - 2) + 2 * n - 2
#
#
# print(f(34))

# @functools.lru_cache(None)
# def fact(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
#
#
# def f(n):
#     if n >= 10000:
#         return fact(n)
#     elif n < 10000 and n % 2 == 0:
#         return f(n + 1) * f(n + 2)
#     elif n < 10000 and n % 2 != 0:
#         return (n + 2) / f(n + 2)
#

# print(f(10))


# def f(n):
#     if n < 4:
#         return n - 1
#     if n > 3 and n % 3 == 0:
#         return n + 2 * f(n - 1)
#     if n > 3 and n % 3 != 0:
#         return f(n - 2) + f(n - 3)
#
#
# print(f(25))


# def f(n):
#     if n < 0:
#         return -n
#     if n % 2 == 0:
#         return 2 * n + 1 + f(n - 3)
#     if n % 2 != 0:
#         return 4 * n + 2 * f(n - 4)
#
#
# print(f(33))



# def f(n):
#     if n == 1:
#         return 3
#     if n > 1:
#         return 2 * f(n - 1) - n + 1
#
#
# print(f(21))



# def f(n):
#     if n > 16:
#         return n - 3
#     if n <= 16:
#         return 2 * f(n + 1) + 2 * n + 3
#
#
# print(f(2))

# def g(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) - 2 * g(n - 1)
#
#
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + 3 * g(n - 1)
#
#
# print(f(18))
# print(sum(list(map(int, str(f(18))))))

# import sys, functools
# sys.setrecursionlimit(999999)
#
# @functools.lru_cache(None)
# def f(n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return 2 * f(1 - n) + 3 * f(n - 1) + 2
#     if n < 0:
#         return -f(-n)
#
#
# print(sum(list(map(int, str(f(50))))))

# def g(n):
#     if n <= 2:
#         return n
#     if n > 2:
#         return f(n - 1) - g(n - 2)
#
#
#
# def f(n):
#     if n <= 2:
#         return n
#     if n > 2:
#         return g(n) + f(n - 2)
#
#
# print(g(15))

# import functools
#
#
# @functools.lru_cache(None)
# def f(n):
#     if n <= 3:
#         return n + 3
#     if n > 3 and f(n - 1) % 2 == 0:
#         return f(n - 2) + n
#     if n > 3 and f(n - 1) % 2 != 0:
#         return f(n - 2) + 2 * n
#
#
# summ = 0
# for i in range(40, 51):
#     summ += f(i)
#     print(summ)
# print(summ)



# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n > 1 and n % 2 == 0:
#         return f(n - 1) - f(n - 2) + 3 * n
#     if n > 1 and n % 2 != 0:
#         return f(n - 2) - f(n - 3) + 2 * n
#
#
# print(f(40))

import sys, functools
sys.setrecursionlimit(99999999)

@functools.lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 6 == 0:
        return n / 6 + f(n / 6 + 2)
    if n < 10000 and n % 6 != 0:
        return n + f(n + 2)
print(f(264) - f(7))
