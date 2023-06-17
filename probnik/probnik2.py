# print('x y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#                 f = ((x <= y) and (y <= z))
#                 if f == 1:
#                     print(x, y, z)

# from itertools import product
#
# k = 0
# for x in product('АБРТЫ', repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s.count('Ы') == 0 and 'АА' not in s:
#         print(s, k)


a = (9 ** 11) * (3 ** 20) - (3 ** 9) - 27

k = 0
while a > 0:
    if a % 3 == 2: k += 1
    a //= 3
print(k)