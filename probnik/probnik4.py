# print('b d c a')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 f = not(b <= a) and (c <= d) or a and b and c and (not d)
#                 if f == 1:
#                     print(b, d, c, a)

# from itertools import product
#
# k = 0
# for x in product('ЛОДКА', repeat=4):
#     a = ''.join(x)
#     if a.count('О') >= 2:
#         # print(a)
#         k += 1
# print(k)

f = open('9.csv').readlines()

k = 0
for line in f:
    a = sorted(list(map(int, line.split('	'))))
    if (a[0] + a[1] > a[2]):
        k += 1
        print(a)
print(k)
# k = 0
# for i in range(100, 1000):
#     k += 1
# print(k)