# print('x y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#                 f = (y <= z) and (not(z and x))
#                 if f ==1:
#                     print(x, y, z)

# from itertools import product
#
# k = 0
# for x in product('ЩОГБА', repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s == 'ОБЩАГА':
#         print(s, k)

# for x in range(2, 100):
#     try:
#         if int('33', x + 4) - int('33', 4) == int('33', 10):
#             print(x)
#     except:
#         pass


# def f(x, a):
#     return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)
#
# for a in range(1, 1000):
#     if all(f(x, a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((x <= y) and (y <= z))
                if f == 1:
                    print(x, y, z, w)