# from itertools import product
#
# k = 0
# for a in product('ЛНРТ', repeat=5):
#     x = ''.join(a)
#     k += 1
#     if k == 150:
#         print(x)
#         break

# from itertools import product
# 
# k = 0
# for a in product('ВЛТУ', repeat=4):
#     x = ''.join(a)
#     k += 1
#     if k == 98:
#         print(x)

# from itertools import product
#
# k = 0
# for x in product('АОУ', repeat=5):
#     a = ''.join(x)
#     k += 1
#     if a[0] == 'У':
#         print(k, a)
#
# from itertools import product
#
# k = 0
# for x in product('АКРУ', repeat=5):
#     a = ''.join(x)
#     k += 1
#     if a[0] == 'К':
#         print(k, a)
#         break

# from itertools import product
#
# k = 0
# for x in product('КОР', repeat=5):
#     a = ''.join(x)
#     k += 1
#     if k == 182:
#         print(a)

# from itertools import product
#
# k = 0
# for x in product('АПРСУ', repeat=3):
#     a = ''.join(x)
#     k += 1
#     if a[0] == 'С':
#         print(k, a)

# from itertools import product
#
# k = 0
# for x in product('АМУХ', repeat=4):
#     a = ''.join(x)
#     k += 1
#     if a == 'ХУХХ':
#         print(k)

# from itertools import product
#
# k = 0
# for x in product('ПИР', repeat=5):
#     a = ''.join(x)
#     if a.count('П') == 1:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ABCDX', repeat=4):
#     a = ''.join(x)
#     if (a[0] == 'X' and 'X' not in a[1:]) or 'X' not in a:
#         k += 1
#         print(a)
# print(k)

from itertools import permutations

k = 0
for x in permutations('ОЛЬГА'):
    a = ''.join(x)
    if a[0] != 'Ь' and (('ОЬ' not in a) and ('АЬ' not in a)):
        k += 1
        print(a)
print(k)


