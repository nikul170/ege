# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (not w) and z and (y <=x)
#                 if f == 1:
#                     print(x,y,z,w)

# from itertools import product
#
# k = 0
# for x in product('АЕВГД', repeat=6):
#     a = ''.join(x)
#     if a[0] == 'А' or a[0] == 'Е':
#         k += 1
# print(k)

# f = open('9.csv').readlines()
# k = 0
# for l in f:
#     a = sorted(list(map(int, l.split('	'))))
#     if ((a[0] + a[1]) == (a[2] + a[3]) or (a[0] + a[2]) == (a[1] + a[3]) or (a[0] + a[3]) == (a[1] + a[2])) and a[0] - a[3] < abs((a[1] + a[2]) - a[3]):
#         k += 1
# print(k)

# x = 2 ** 24 +2 ** 14 - 2 ** 5
# k = 0
# while x > 0:
#     if x % 2 == 1:
#         k += 1
#     x //= 2
# print(k)

# def f(x, a):
#     return (x % a == 0) <= ((x % a == 0) <= (x % 34 == 0) and (x % 51 == 0))
#
# for a in range(1, 10000):
#     if all(f(x,a) == 1 for x in range(1, 10000)):
#         print(a)


