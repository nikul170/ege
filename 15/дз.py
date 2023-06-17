# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return ((d(x, a) and d(x, 37)) <= d(x, 3737)) and (a < 1000)
#
#
# print(max(a for a in range(1, 1000) if all(f(x, a) for x in range(1, 100000))))


# def f(x, y, a):
#     return (25 * x + 8 * y != 10000) or ((a > x) and (a > y))
#
#
# print(min(a for a in range(-100, 2000) if all(f(x, y, a) for x in range(1000) for y in range(1000))))


# a1, a2, p1, p2 = 30, 50, 10, 80
# a = [i / 10 for i in range(a1 * 10, a2 * 10 + 1)]
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
#
#
# def f(x, a):
#     return (x in q) <= ((x in a) and (x not in p))
#
#
# q = set()
# for x in [i / 10 for i in range(0, 100 * 10)]:
#     if not f(x, q):
#         q.add(x)
# print(sorted(q))


# def f(x, a):
#     return (x & a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))
#
#
# print(max(a for a in range(1000) if all(f(x, a) for x in range(1000))))

#
# def d(n, m):
#     return n % m == 0
#
#
# def c(s, d):
#     return s + d >= 0
#
#
# def f(x, a):
#     return (x + a >= 160) or (d(x, 7) <= (not c(x, -17)))
#
#
# print(min(a for a in range(-200, 200) if all(f(x, a) for x in range(1, 1000))))


# def f(x, a):
#     return (x & 49 != 0) <= ((x & 41 == 0) <= (x & a != 0))
#
#
# print(min(a for a in range(1000) if all(f(x,a) for x in range(1000))))


# def f(x, y, a):
#     return (y + 2 * x != 48) or (a < x) or (a < y)
#
#
# print(max(a for a in range(100) if all(f(x, y, a) for x in range(1000) for y in range(1000))))


p1, p2, q1, q2 = 10, 20, 35, 45
p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]


def f(x, a):
    return ((not(x in p)) <= (x in q)) and (x not in a)


a = set()
for x in [i / 10 for i in range(5 * 10, 60 * 10)]:
    if f(x, a):
        a.add(x)
print(sorted(a))







