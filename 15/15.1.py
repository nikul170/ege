'''
Делимость
'''
# def f(x, a):
#     return ((x % a == 0) and (x % 36 != 0)) <= (x % 12 != 0)
#
# for a in range(1, 10001):
#     if all(f(x,a) == 1 for x in range(1, 1000)):
#         print(a)
#         break

'''
Поразрядная конъюнкция
'''

# def f(x,a):
#     return (x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))
#
# for a in range(1, 1000):
#     if all(f(x, a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

'''
Числовая примая
'''

# def f(x, y, a):
#     return (x < a) and (y < a) and ( x * y > 1200)
#
# for a in range(1,1000):
#     if all(f(x, y, a) == 0 for x in range(1, 100) for y in range(1, 100)):
#         print(a)

'''
Множества
'''

# p = {1,3,5,7,9,11}
# q = {3,6,9,12}
# a = set()
#
# def f(x):
#     return (x in p) <= (x not in q) or (x in a)
#
# for x in range(1, 1001):
#     if f(x) == 0:
#         a.add(x)
# print(a)

'''
Отрезки
'''

# def f(x, a1, a2):
#     return ((a1 <= x <= a2) <= (430 <= x <= 490) or (440 <= x <= 530))
#
#
# m = 0
# for a1 in range(400, 600):
#     for a2 in range(a1 + 1, 600):
#         if all(f(x,a1,a2) == 1 for x in range(400, 600)):
#             m = max(m, a2 - a1)
# print(m)

# def f(x,a):
#     return (((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0))
#
# for a in range(1, 1000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

# def f(x,a):
#     return (((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0))
#
#
# for a in range(1, 10000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

# def f(x,a):
#     return (((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0)))
#
#
# for a in range(1, 100000):
#     if all(f(x,a) == 1 for x in range(1, 10000)):
#         print(a)
#         break

# def f(x, a):
#     return (((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a))
#
# for a in range(1, 10000):
#     if all(f(x,a) == 1 for x in range(1,10001)):
#         print(a)
#         break

# def f(x,a):
#     return (((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0)))
#
#
# for a in range(1, 1000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

# def f(x,a):
#     return ((a % 7 == 0) and ((240 % x == 0)) <= ((a % x != 0) <= (780 % x != 0)))
#
#
# for a in range(1, 1000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

# def f(x,a):
#     return (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0)) or ((x & a != 0) and (x & 39 == 0))
#
#
# for a in range(1, 10000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)

# def f(x,a):
#     return ((x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0)))
#
# for a in range(1, 10000):
#     if all(f(x,a) == 1 for x in range(1, 10001)):
#         print(a)
#         break

# p = set(range(11, 2 ** 8 + 1))
# q = set(range(0, 2 ** 8, 10))
# a = set()
# def f(x):
#     return ((x not in a) <= ((x in p) or (x not in q)))
#
# for x in range(1, 1000):
#     if f(x) == 1:
#         a.add(x)
# print(a)

# def f(x,y, a):
#     return ((x * y > a) and (x > y) and (x < 8))
#
# for a in range(1, 1000):
#     if all(f(x,y,a) == 0 for x in range(1, 100) for y in range(1, 100)):
#         print(a)
#

# def f(x,y, a):
#     return ((x > 39) or ( y > 26) or (2 * x + 4 * y < a))
#
# for a in range(1, 1000):
#     if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
#         print(a)
#         break
#
# def f(x, y, a):
#     return ((2 * x + y != 70) or (x < y) or (a < x))
#
# for a in range(1, 1000):
#     if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
#         print(a)

# def f(x, y, a):
#     return ((x ** 2 - 10 * x + 16 > 0) or (y ** 2 - 10 * y + 21 > 0) or (x * y < 2 * a))
#
# for a in range(1, 1000):
#     if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
#         print(a)
#         break


# a = set()
# def f(x):
#     return (((x in {1,3,5,7,9,11}) <= (x not in {3,6,9,12})) or x in a)
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         a.add(x)
# print(a)

# a = set()
#
# def f(x):
#     return (not((x not in a) and (x in {3,6,9,12})) or not(x in {1,2,3,4,5,6}))
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         a.add(x)
# print(a)

# p = set(range(2, 21, 2))
# q = set(range(5, 51, 5))
# a = set(range(1, 1000))
# def f(x):
#     return (((x in a) <= (x in p)) and ((x in q) <= (x not in a)))
#
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         a.remove(x)
# print(a)

# p = set(range(2, 21, 2))
# q = set(range(3, 31, 3))
# r = set(range(12, 61, 12))
# a = set()
#
# def f(x):
#     return ((x not in a) <= (((x in p) and (x in q)) <= (x in r)))
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         a.add(x)
# print(a)


# def f(x, a1, a2):
#     return (170 <= x <= 580) <= ((not(290 <= x <= 800) and not(a1 <= x <= a2)) <= (not(170 <= x <= 580)))
#
# m = 10 ** 8
# for a1 in range(150, 900):
#     for a2 in range(a1 + 1, 900):
#         if all(f(x, a1, a2) == 1 for x in range(150, 900)):
#             m = min(m, a2 - a1)
# print(m / 10)

# def f(x, a1, a2):
#     return (((170 <= x <= 540)) <= (((370 <= x <= 830) and (not(a1 <= x <= 2))) <= (not(170 <= x <= 540))))
#
# m = 10 ** 8
# for a1 in range(160, 840):
#     for a2 in range(a1 + 1, 840):
#         if all(f(x, a1, a2) == 1 for x in range(160, 840)):
#             m = min(m, a2 - a1)
# print(m)

def f(x, a1, a2):
    return (((180 <= x <= 520) <= (a1 <= x <= a2)) and (not(160 <= x <= 410) or (a1 <= x <= a2)))


m = 10 ** 8
for a1 in range(130, 550):
    for a2 in range(a1 + 1, 550):
        if all(f(x, a1, a2) == 1 for x in range(130, 550)):
            m = min(m, a2 - a1)
print(m / 10)
