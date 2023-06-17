# from itertools import *
#
# def u(x, y, z, w):
#     return (w == y) or (((not x) <= z) and ((not z) <= y))
#
#
# for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
#     t = (
#         (x1, 1, 1, x2, 0),
#         (x3, x4, 1, x5, 0),
#         (1, x6, x7, x8, 0),
#          )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)



# def f(N):
#     n = bin(N)[2:]
#     flag = False
#
#     print(n)
#     # return N - int(n, 2)
#
#
# print(f(11))