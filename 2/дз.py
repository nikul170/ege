# from itertools import *
#
#
# def u(x, y, z, w):
#     return (w <= y) and ((x <= z) == (y <= x))
#
#
# for x1, x2, x3, x4 in product([0,1], repeat=4):
#     t = (
#         (x1, 1, x2, 0, 1),
#         (0, x3, 1, x4, 1),
#         (0, 1, 0, 1, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x == (not y)) <= (z == (y or w))
#
#
# for x1, x2, x3, x4, x5 in product([0,1], repeat=5):
#     t = (
#         (0, x1, 0, x2, 0),
#         (0, 0, x3, 0, 0),
#         (0, x4, x5, 0, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return w and (x == (z <= y))
#
#
# t = (
#     (0, 1, 1, 0, 1),
#     (0, 1, 0, 1, 1),
#     (1, 1, 0, 1, 1),
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and (not y)) or (y == z) or w
#
#
# for x1, x2, x3, x4 in product([0,1], repeat=4):
#     t = (
#         (x1, x2, x3, 1, 0),
#         (1, 0, 0, 0, 0),
#         (1, 1, 0, x4, 0),
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (y <= (x or z)) and (z <= y)
#
#
# t = (
#     (1, 0, 0, 0, 0),
#     (1, 1, 0, 0, 0),
#     (1, 1, 0, 1, 0),
#     (0, 1, 1, 0, 0),
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and (y or (not z)) and w) == (x <= ((not y) and z))
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (x1, 1, x2, x3, 1),
#         (1, 1, x4, x5, 1),
#         (1, 1, 1, x6, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


from itertools import *


def u(a, b, c):
    return a == (b or c) == b


for x1, x2, x3, x4 in product([0, 1], repeat=4):
    t = (
        (x1, 0, 0, 1),
        (0, x2, x3, 1),
        (0, x4, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('abc', r=3):
            if all(u(**dict(zip(p, r))) == r[-1] for r in t):
                print(*p)



# from itertools import *
#
#
# def u(x, y, z, w):
#     return ((not x) or y or (not z)) and (x or (not y)) or (not w)
#
#
#
# t = (
#     (0, 0, 1, 1, 0),
#     (0, 1, 1, 1, 0),
#     (1, 1, 1, 0, 0),
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)
