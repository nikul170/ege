# for x in range(1, 51):
#     n = '6' * 48
#     while '66' in n:
#         n = n.replace('66', '1', 1)
#         n = n.replace('11', '2', 1)
#         n = n.replace('22', '6', 1)
#     if n == '21':
#         print(n)

# s = '2' * 50 + '3' * 50 + '1' * 50
# while ('21' in s) or ('31' in s) or ('23' in s):
#     if '21' in s:
#         s = s.replace('21', '12', 1)
#     if '31' in s:
#         s = s.replace('31', '13', 1)
#     if '23' in s:
#         s = s.replace('23', '32', 1)
# print(s[11], s[91], s[131])

# s = '>' + '1' * 20 + '3' * 40 + '2' * 15
#
# while ('>1' in s) or ('>2' in s) or ('>3' in s):
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>1', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>2', 1)
# s = s.replace('>', '')
# print(sum(map(int, s)))

# for x in range(100, 10000):
#     s = '1' * x
#     while ('333' in s) or ('111' in s):
#         s = s.replace('333', '11', 1)
#         s = s.replace('111', '3', 1)
#     print(x, s)


# s = '0' + '1' * 45
#
# while ('0' in s) or ('01' in s):
#     if '01' in s:
#         s = s.replace('01', '10', 1)
#     else:
#         s = s.replace('0', '111', 1)
# print(s.count('1'))

# for x in range(109, 10000):
#     s = '4' * x
#     while ('444' in s) or ('999' in s):
#         s = s.replace('444', '9', 1)
#         s = s.replace('999', '44', 1)
#     if s.count('4') == 1 and s.count('9') == 1:
#         print(x)


s = '0' + '1' * 11 + '3' * 5 + '1' + '2' * 43 + '2' * 2
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '2302', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '201', 1)
print(s.count('1'))
