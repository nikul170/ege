# s = '8' * 70
#
# while ('2222' in s) or ('8888' in s):
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
#
# print(s)

# s = '2' + '5' * 81
#
# while '25' in s or '355' in s or '4555' in s:
#     if '25' in s:
#         s = s.replace('25', '4', 1)
#     if '355' in s:
#         s = s.replace('355', '2', 1)
#     if '4555' in s:
#         s = s.replace('4555', '3', 1)
#
# print(s)

# def f(x):
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return False
#     return True
#
#
# for n in range(0, 50):
#     s = '>' + '0' * 39 + '1' * n + '2' * 39
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s: s = s.replace('>1', '22>', 1)
#         if '>2' in s: s = s.replace('>2', '2>', 1)
#         if '>0' in s: s = s.replace('>0', '1>', 1)
#     s = s.replace('>', '')
#     s = sum(map(int, s))
#     if f(s):
#         print(n)
#         break

# s = '4' * 204

# while '4444' in s or '777' in s:
#     if '4444' in s: s = s.replace('4444', '77', 1)
#     else: s = s.replace('777', '4', 1)
# print(s)

# s = 'X' * 107
#
# while 'XXX' in s or 'ZYX' in s or "ZXX" in s:
#     s = s.replace('XXX', 'ZZ', 1)
#     s = s.replace('ZYX', 'X', 1)
#     s = s.replace('ZXX', 'Y', 1)
# print(s)

# s = '1' + '8' * 80
#
# while '18' in s or '288' in s or '3888' in s:
#     if '18' in s: s = s.replace('18', '2', 1)
#     if '288' in s: s = s.replace('288', '3', 1)
#     if '3888' in s: s = s.replace('3888', '1', 1)
# print(s)

# s = '5' * 54 + '7'
#
# while '722' in s or '557' in s:
#     if '722' in s: s = s.replace('722', '57', 1)
#     else: s = s.replace('557', '72', 1)
#
# print(s)

# s = '1' + '9' * 98
#
# while '19' in s or '299' in s or '3999' in s:
#     s = s.replace('19', '2', 1)
#     s = s.replace('299', '3', 1)
#     s = s.replace('3999', '1', 1)
# print(s)

# s = '>' + '2' * 18 + '3' * 35 + '1' * 28
#
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s: s = s.replace('>1', '22>', 1)
#     if '>2' in s: s = s.replace('>2', '2>1', 1)
#     if '>3' in s: s = s.replace('>3', '1>2', 1)
# s = s.replace('>', '')
# print(sum(map(int, s)))

s = '1' + '0' * 80

while '10' in s or '1' in s:
    if '10' in s: s = s.replace('10', '001', 1)
    elif '1' in s: s = s.replace('1', '000', 1)
print(len(s))

# s = '1' * 84
#
# while '11111' in s:
#     s = s.replace('222', '1', 1)
#     s = s.replace('111', '2', 1)
# print(s)

# s = '1' * 99
#
# while '111' in s:
#     s = s.replace('11', '2', 1)
#     s = s.replace('22', '1', 1)
# print(s)

s = '1' * 99

while '111' in s:
    if '222' in s:
        s = s.replace('222', '1', 1)
    else: s = s.replace('111', '2', 1)
print(s)