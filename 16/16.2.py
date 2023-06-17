# import sys
# import threading
#
# sys.setrecursionlimit(99999)
#
# threading.stack_size(4096 * 4096 * 8)
#
# def thr():
#     def f(n):
#         if n <= 10: return n
#         if n >= 10000: return 1
#         if 10 < n < 10000 and n % 2 == 0: return n % 10 + f(n + 2)
#         if 10 < n < 10000 and n % 2 != 0: return f(n - 2) - (n - 1) % 10
#     print(f(4500) + f(5515))
#
#
# new_thread = threading.Thread(target=thr, args=[])
# new_thread.start()


# def f(n):
#     if n <= 3:
#         return 3
#     if n > 3 and n % 2 == 0:
#         return f(n // 2) + 5
#     if n > 3 and n % 2 != 0:
#         return f(n - 1) - f(n - 2)
#
# print(f(20))

# import functools
#
# @functools.lru_cache(None)
# def f(n):
#     if n == 0: return 1
#     if n == 1: return 3
#     if n > 1: return f(n - 1) - f(n - 2) + 3 * n
#
# print(f(40))


# def f(n):
#     if n <= 1: return 1
#     if n > 1 and n % 2 == 0: return 3 * n + f(n - 1)
#     if n > 1 and n % 2 != 0: return 2 * f(n - 3)
#
#
# print(f(30))


# def f(n):
#     if n <= 1: return 0
#     if n > 1 and n % 2 != 0: return f(n - 1) + 3 * n ** 2
#     if n > 1 and n % 2 == 0: return n / 2 + f(n - 1) + 2
#
#
# print(f(49))


# def f(n):
#     if n <= 2: return 1
#     if n > 2: return f(n - 1) + 2 * f(n - 2)
#
#
# print(f(17))


# def f(n):
#     if n == 1: return 1
#     if n > 1: return 5 * f(n - 1) + 3 * n
#
#
# print(f(4))

# import sys
# sys.setrecursionlimit(99999)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return (3 * n + 5) * f(n - 1)
#
# print(f(2073) / f(2070))



