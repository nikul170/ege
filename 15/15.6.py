# def f(x, y, a):
#     return (2 * x + 3 * y != 150) or (x < a) or (y < a)
#
#
# print(min(a for a in range(-100, 100) if all(f(x, y, a) for x in range(100) for y in range(100))))


# def d(x, a):
#     return x % a == 0
#
#
# def f(x, a):
#     return (not d(x, a)) or (not d(x, 5)) or d(x, 35)
#
#
# print(min(a for a in range(1, 200) if all(f(x, a) for x in range(1000))))


# def f(x, a):
#     return (x & 57 != 0) and (x & 38 != 0) or (x & 9 == 0) or (x & a == 0)
#
#
# print(min(a for a in range(1, 1000) if all(f(x, a) for x in range(10000))))


# p1, p2, q1, q2 = 3, 38, 21, 57
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return ((x in q) <= (x in p)) <= (x not in a)
#
#
# a = set([i / 10 for i in range(1 * 10, 60 * 10)])
# for x in [i / 10 for i in range(1 * 10, 60 * 10)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))


# def f(x, a):
#     return (x & a != 0) <= ((x & 36 == 0) <= (x & 6 != 0))
#
#
# print(max(a for a in range(-100, 100) if all(f(x, a) for x in range(1000))))


# def d(n, m):
# #     return n % m == 0
# #
# #
# # def f(x, a):
# #     return (d(x, 45) and (not d(x, 15))) <= (not d(x, a))
# #
# #
# # print(min(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# p1, p2, q1, q2 = 5, 30, 14, 23
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return ((x in p) == (x in q)) <= (x not in a)
#
#
# a = set([i / 10 for i in range(2 * 10, 35 * 10)])
# for x in [i / 10 for i in range(2 * 10, 35 * 10)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))


# def f(x, y, a):
#     return (x < 9) <= ((5 * y < x) <= (2 * x * y < a))
#
#
# print(min(a for a in range(-200, 200) if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100))))



# def f(x, a):
#     return (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0))
#
#
# print(max(a for a in range(-200, 200) if all(f(x, a) for x in range(1000))))



def f(x, y, a):
    return (x * y > a) or (x > y) or (8 > x)


print(max(a for a in range(1, 100) if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100))))



def f(x, y, a):
    return (3 * y - x > a) or (2 * x + 3 * y < 58) or (2 * y - x < -33)


print(max(a for a in range(-200, 0) if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100))))

