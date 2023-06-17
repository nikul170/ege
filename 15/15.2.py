# def d(n ,m):
#     return  n % m == 0
#
#
# def f(x, a):
#     return (not d(x, a)) <= (d(x, 6) <= (not d(x, 9)))
#
#
# print(max(A for A in range(1, 100) if all(f(x, A) for x in range(1, 1000))))

# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return (d(x, a) and d(x, 24) and (not d(x, 16))) <= (not d(x, a))
#
#
# print(min(A for A in range(1, 100) if all(f(x, A) for x in range(1, 1000))))


# def f(x, y, a):
#     return ((x < a) <= (x ** 2 <= 169)) and ((y ** 2 < 16) <= (y <= a))
#
#
# print(len([a for a in range(-100, 100) if all(f(x, y, a) for x in range(1000) for y in range(1000))]))


# def f(x, a):
#     return (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))
#
#
# print(max(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return (a < 50) and ((not d(x, a)) <= (d(x, 10) <= (not d(x, 12))))
#
#
# print(max(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# def f(x, a):
#     return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))
#
#
# print(min(a for a in range(1, 1000) if all(f(x, a) for x in range(1, 1000))))

# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return (d(x, 34) and (not d(x, 51))) <= ((not d(x, a)) or d(x, 51))
#
#
# print(min(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# def f(x, y, a):
#     return (x * y > a) and (x > y) and (x < 8)
#
#
# print(min(a for a in range(-100, 100) if all((not f(x, y, a)) for x in range(1, 1000) for y in range(1, 1000))))

# def f(x, a):
#     return (x & 33 == 0) <= ((x & 45 != 0) <= (x & a != 0))
#
#
# print(min(a for a in range(100) if all(f(x, a) for x in range(1000))))


# def f(x, a):
#     return (x & 30 != 4) or ((x & 35 == 1) <= (x & a == 0))
#
#
# print(max(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))

# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return d(90, a) and ((not d(x, a)) <= (d(x, 15) <= (not d(x, 20))))
#
#
# print(max(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# def f(x, a):
#     return (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0))
#
#
# print(max(a for a in range(-200, 200) if all(f(x,a) for x in range(1000))))


# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return d(70, a) and (d(x, 28) <= ((not d(x, a)) <= (not d(x, 21))))
#
#
# print(max(a for a in range(1, 100) if all(f(x, a) for x in range(1, 1000))))


# def f(x, a):
#     return (x & a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))
#
#
# print(max(a for a in range(1000) if all(f(x,a) for x in range(1000))))

