# def f(a, b, c, m):
#     if a + b <= 32: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(a - 1, b, c + 1, m), f(a, b - 1, c + 1, m), f((a + 1) // 2, b, c + 1, m), f(a, (b + 1 ) // 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1,100):
#     for m in range(1, 5):
#         if f(10, s, 0, m):
#             if m == 2:
#                 print(s, m)
#             break

# def f(s, c, m):
#     if 43 <= s <= 72: return c % 2 == m % 2
#     if s > 72: return c % 2 != m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else any(h)
#
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2:
#                 print(s, m)
#             break


# def f(s, c, m, n):
#     if s >= 43: return m % 2 == c % 2
#     if m == c: return 0
#     h = []
#     if n != "+1": h += [f(s + 1, c + 1, m, "+1")]
#     if n != "+2": h += [f(s + 2, c + 1, m, "+2")]
#     if n != "*2": h += [f(s * 2, c + 1, m, "*2")]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m, ''):
#             if m == 2:
#                 print(s, m)
#                 break


# def f(a, b, c, m):
#     if a + b <= 20: return c % 2 == m % 2
#     if m == c: return 0
#     h = [f(a - 1, b, c + 1, m), f(a, b - 1, c + 1, m), f((a + 1) // 2, b, c + 1, m), f(a, (b + 1) // 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(11, 100):
#     for m in range(1, 5):
#         if f(10, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break


def f(s, c , m):
    if 36 <= s <= 60: return c % 2 == m % 2
    if s > 60: return c % 2 != m % 2
    if c == m: return 0
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 36):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break

# def f(s, c, m, n):
#     if s >= 62: return c % 2 == m % 2
#     if c == m: return 0
#     h = []
#     if n != "+1": h += [f(s + 1, c + 1, m, '+1')]
#     if n != "+2": h += [f(s + 2, c + 1, m, '+2')]
#     if n != "*3": h += [f(s * 3, c + 1, m, '*3')]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 62):
#     for m in range(1, 5):
#         if f(s, 0, m, ""):
#             if m == 4:
#                 print(s, m)
#             break


