# x = 3284
# while x > 0:
#     print(x % 2)
#     x //= 2
#
# print(bin(25)[2:])
# print(oct(25)[2:])
# print(hex(25)[2:])
#
# x = 2 ** 18 * 6 ** 234 + 101
# s = ''
# print(bin(x)[2:].count('0'))
# while x > 0:
#     s = str(x % 2) + s
#     x //= 2
# print(s.count('0'))

# x = 17 ** 5 + 85 ** 8 - 10
#
# k = 0
# while x>0:
#     if x % 17 ==16:
#         k += 1
#     x //= 17
# print(k)

# x = 8 ** 2 + 49 ** 4 - 21
#
# k = 0
# while x > 0:
#     if x % 14 == 0 or x % 10:
#         k += 1
#     x //= 14
# print(k)

# for i in range(1, 1000):
#     x = 81 ** 20 - 9 ** i + 50
#     k = 0
#     while x > 0:
#         k += x % 9
#         x //= 9
#     if k == 138:
#         print(i)
#         break

# for i in range(1, 1000):
#     x = 64**12 - 8**14 + i
#     k7 = 0
#     k1 = 0
#     while x > 0:
#         if x % 8 == 7: k7 += 1
#         if x % 8 == 1: k1 += 1
#         x //= 8
#     if k7 == 12 and k1 == 1:
#         print(i)

# for n in range(2, 1000):
#     try:
#         if int('123', n) == int('93', n + 2):
#             print(n)
#     except:
#         ...

# for n in range(1,100):
#     if 56 % n == 1 and 45 % n == 1:
#         print(n)

# for n in range(1,100):
#     if 338 % n == 2 and n ** 2 <= 338 < n ** 3:
#         print(n)

# for n in range(1, 50):
#     if n % 8 == 3:
#         print(n)

# for x in range(1, 50):
#     if x % 9 == 7:
#         print(x)

# for x in range(100):
#     if x % 16 == 12:
#         print(x)

# for x in range(10, 100):
#     if x % 16 == 10 and x % 5 == 3:
#         print(x)

# for n in range(345):
#     if 27 <= n < 81 and 49 <= n <= 343 and n % 64 == 15:
#         print(n)

# x = 64 ** 30 + 2 ** 300 - 4
#
# k = 0
# while x > 0:
#     if x % 8 == 7:
#         k += 1
#     x //= 8
# print(k)
#
# x = 3 * 16 ** 8 - 4 ** 5 + 3
#
# k = 0
# while x > 0:
#     if x % 4 == 3:
#         k += 1
#     x //= 4
# print(k)

# x = 2 * 27 ** 7 + 3 ** 10 - 9
#
# k = 0
# while x > 0:
#     if x % 3 == 0:
#         k += 1
#     x //= 3
# print(k)

# x = 51 * 7 ** 12 - 7 ** 3 - 22
#
# k = 0
# while x > 0:
#     k += x % 7
#     x //= 7
# print(k)

# for i in range(0, 1000):
#     x = 125 ** 200 - 5 ** i + 74
#     k = 0
#     while x > 0:
#         if x % 5 == 4:
#             k += 1
#         x //= 5
#     if k == 100:
#         print(i)


# for i in range(10000):
#     x = 4 ** 2015 + 2 ** i - 2 ** 2015 + 15
#     if bin(x).count('1') == 500:
#         print(i)
#
# for i in range(10000):
#     x = 4 ** 1014 - 2 ** i + 12
#     if bin(x)[2:].count('0') == 2000:
#         print(i)

# for i in range(1000):
#     x = 36 ** 17 - 6 ** i + 71
#     k = 0
#     while x > 0:
#         k += x % 6
#         x //= 6
#     if k == 61:
#         print(i)


# x = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
# k = 0
# while x > 0:
#     if x % 12 == 11:
#         k += 1
#     x //= 12
# print(k)

# x = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
#
# k5 = 0
# k0 = 0
# while x > 0:
#     if x % 6 == 5:
#         k5 += 1
#     if x % 6 == 0:
#         k0 += 1
#     x //= 6
# print(k5 - k0)

# for i in range(4, 100):
#     try:
#         if int('33', i + 4) - int('33', 4) == int('33', 10):
#             print(i)
#     except:
#         pass

# for i in range(4, 1000):
#     try:
#         if int('21', i) * int('13', i) == int('313', i):
#             print(i)
#     except:
#         pass

# for i in range(21, 30):
#     if i % 9 == 4:
#         print(i)

# for x in range(41):
#     if x % 16 == 11:
#         print(x)

# for n in range(1, 1000):
#     if 68 % n == 2 and n ** 3 <= 68 < n ** 4:
#         print(n)


# for x in range(1000):
#     if 6 <= x < 36 and 25 <= x < 125 and x % 11 == 1:
#         print(x)

# for x in range(1000):
#     if 7 <= x < 49 and 36 <= x < 36 * 6 and x % 13 == 3:
#         print(x)

k = 0
for x in range(10000):
    if 16 <= x < 625 and x % 16 == 12:
        k += 1
print(k)