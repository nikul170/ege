# q1, q2 = 29, 47
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return ((not d(x, 3)) and x not in [48, 52, 56]) <= ((abs(x - 50) <= 7) <= (x in q)) or (x & a == 0)
#
#
# print(min(a for a in range(1, 100) if all(f(x, a) for x in range(1, 100))))


# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return d(a, 5) and ((not d(2020, a)) <= (d(x, 1718) <= d(2023, a)))
#
#
# k = 0
# for a in range(1, 300):
#     if all(f(x, a) for x in range(1718, 4000)):
#         k += 1
# print


# ДЕЛ(A, 5) ∧ (¬ДЕЛ(2020, A) → (ДЕЛ(x, 1718) → ДЕЛ(2023, A)))

