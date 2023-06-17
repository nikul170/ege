# def f(s, c, m):
#     if 51 <= s: return c % 2 == m % 2
#     if c == m: return 0
#     h = []
#     if s + 1 < 60: h.append(f(s + 1, c + 1, m))
#     if s + 2 < 60: h.append(f(s + 2, c + 1, m))
#     if s * 2 < 60: h.append(f(s * 2, c + 1, m))
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 51):
#     for m in range(1, 7):
#         if f(s, 0, m):
#             if m == 3:
#                 print(s)
#             break


def f(a, b, c, m):
    if a + b == 13: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a + 2, b, c + 1, m), f(a, b + 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 10):
    for m in range(1, 7):
        if f(3, s, 0, m):
            if m == 1:
                print(s)
            break


# def f(a, b, c, m):
#     if a + b >= 49: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 3, b, c + 1, m), f(a, b * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 44):
#     for m in range(1, 7):
#         if f(5, s, 0, m):
#             if m == 4:
#                 print(s)
#             break


# def f(a, b, c, m):
#     if a + b >= 200: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a + 6, b, c + 1, m), f(a ** 2, b, c + 1, m), f(a, b + 6, c + 1, m), f(a, b ** 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else any(h)
#
#
# for s in range(1, 195):
#     for m in range(1, 7):
#         if f(3, s, 0, m):
#             if m == 2:
#                 print(s)
#             break



