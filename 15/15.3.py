# p1, p2, q1, q2 = 3, 15, 14, 25
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return ((x in p) == (x in q)) <= (x not in a)
#
#
# a = set([i / 10 for i in range(0 * 10, 30 * 10)])
#
# for x in [i / 10 for i in range(0 * 10, 30 * 10)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))
#
# p1, p2, q1, q2 = 3, 15, 14, 25
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return ((x in p) == (x in q)) <= (x not in a)
#
#
# a = set([i / 10 for i in range(0 * 10, 30 * 10 + 1)])
# for x in [i / 10 for i in range(0 * 10, 30 * 10 + 1)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))


# p1, p2, q1, q2 = 130, 171, 150, 185
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return (x in p) <= (((x in q) and (x not in a)) <= (x not in p))
#
#
# a = set()
# for x in [i / 10 for i in range(100 * 10, 200 * 10 + 1)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))


# def f(x, a):
#     return (x not in a) <= (x not in [1, 12]) and (x not in [12, 13, 14, 15, 16])
#
#
# a = set()
# for x in range(0, 20):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))


# p1, p2, q1, q2 = 43, 49, 44, 53
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return ((x in a) <= (x in p)) or (x in q)
#
#
# a = set([i / 10 for i in range(40 * 10, 60 * 10 + 1)])
# for x in [i / 10 for i in range(40 * 10, 60 * 10 + 1)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))

#
# def f(x, a):
#     return (x not in [1, 2, 4, 8, 16]) and (x not in [3, 4, 9, 16]) or (x in a)
#
#
# a = set()
# for x in range(0, 20):
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))


# p1, p2, q1, q2 = 17, 54, 37, 83
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return (x in p) <= (((x in q) and (x not in a)) <= (x not in p))
#
#
# a = set()
# for x in [i / 10 for i in range(10 * 10, 90 * 10 + 1)]:
#     if not f(x, a):
#         a.add(x)
# print(54- 37)


# def f(x, a):
#     return (x in [3, 5, 7, 11, 12, 15]) <= (x in [5, 6, 12, 15]) or (x in a)
#
#
# a = set()
# for x in range(0, 25):
#     if not f(x, a):
#         a.add(x)
# print(3 * 7 * 11)


# p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# q = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#
#
# def f(x, a):
#     return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))
#
#
# a = set(range(0, 60))
# for x in range(0, 60):
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))