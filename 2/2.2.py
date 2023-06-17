# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((not x) and y and (not z) or x and (not y)) and (not w)
#                 if f == 1:
#                     print(x, y, z, w)

# from itertools import *

# def u(x, y, z, w):
#     return ((not x) and y and (not z) or x and (not y)) and (not w)
#
#
# t = (
#     (0, 0, 0, 1, 1),
#     (1, 0, 0, 0, 1),
#     (1, 1, 0, 0, 1),
# )
#
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)

# from itertools import *
#
# def u(x, y, z, w):
#     return (x or (y and (not z))) and (not w)
#
#
# t = (
#     (1, 0, 0, 0, 1),
#     (0, 0, 1, 0, 1),
#     (0, 1, 0, 1, 0)
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and (not y)) or (y == z) or (not w)
#                 if f == 0:
#                     print(x, y, z, w)


# from itertools import *
#
# def u(x, y, z, w):
#     return (x and (not y)) or (y == z) or (not w)
#
# for x1, x2, x3, x4 in product([0, 1], repeat=4):
#     t = (
#         (0, x1, x2, 0, 0),
#         (0, 1, 0, 1, 0),
#         (x3, 1, 0, x4, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and z) or ((w <= x) == (z <= y))
#                 if f == 0:
#                     print(x, y, z, w)

# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and z) or ((w <= x) == (z <= y))
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (x1, x2, x3, 1, 0),
#         (x4, x5, 1, 1, 0),
#         (x6, 1, 1, 1, 0),
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x or y and (not z)) and (not w)
#                 if f == 0:
#                     print(x, y, z, w)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x or y and (not z)) and (not w)
#
#
# t = (
#     (1, 0, 0, 0, 0),
#     (0, 0, 1, 0, 0),
#     (0, 1, 0, 1, 1)
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (((not y) <= w) <= (x <= z)) <= (x <= w)
#                 if f == 0:
#                     print(x, y, z, w)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (((not y) <= w) <= (x <= z)) <= (x <= w)
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (0, 0, 0, x1, 0),
#         (0, 0, x2, x3, 0),
#         (0, x4, x5, x6, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and (not y)) or (y == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and (not y)) or (y == z) or w
#
#
# for x1, x2, x3, x4, x5, x6, x7, x8 in product([0, 1], repeat=8):
#     t = (
#         (x1, x2, x3, 1, 0),
#         (1, x4, x5, x6, 0),
#         (1, 1, x7, x8, 0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (w <= y) and ((x <= z) == (y <= x))
#                 if f == 1:
#                     print(x, y, z, w)


# from itertools import *
#
#
# def u(x, y, z, w):
#     return (w <= y) and ((x <= z) == (y <= x))
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


