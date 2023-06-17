# a = open('24.txt').readline()
#
# k = 0
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if a[i] + a[i + 1] != 'ad' and a[i] + a[i + 1] != 'da':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
#
# print(m)


# a = open('24.txt').readlines()
#
# k = 0
# for x in a:
#     if x.count('A') > x.count('E'):
#         k += 1
# print(k)

# a = open('24.txt').readline()
#
# l = []
# k = 0
#
#
# for i in range(len(a) - 2):
#     if a[i] == a[i + 2]:
#         l.append(a[i + 1])
#
#
# m = max(l.count(a) for a in set(l))
#
# for j in set(l):
#     if l.count(j) == m:
#         print(j)


# a = open('24.txt').readlines()
# l = min(x.count('G') for x in a)
#
# for i in a:
#     if i.count('G') == l:
#         m = max(i.count(x) for x in set(i))
#         for x in set(i):
#             if i.count(x) == m:
#                 print(x)
#         break


# a = open('24.txt').readline()
#
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1] != 'PR') and (a[i] + a[i + 1] != 'RP'):
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# a = open('24.txt').readline()
#
# k = 1
# m = -float('inf')
# l = 0
#
# for x in range(len(a) - 1):
#     for y in range(x + 1, len(a) - 1):
#         if a[y] == 'D' or a[x] == 'D':
#             if a[y] == a[x]:
#                 break
#             l += 1
#         if l <= 2:
#             k += 1
#             m = max(m, k)
#         elif l > 2:
#             k = 1
#             l = 0
#             break
#
#
# print(m)


# z = open('24.txt').readline()
# a = z
# m = -float('inf')
# s = a.split('DBAC')
# i = 0
# for x in s:
#     a = a.replace(x, '0', 1)
#     if x[0] == 'D':
#         a += 'D'
#     print(a)
#     break
#     elif x[:2] == 'DB': a += 'DB'
#     elif x[:3] == 'DBA': a += 'DBA'
# a = a.split('0')
# print(max(len(x) for x in a))








# a = open('24.txt').readline()
# 
# m = -float('inf')
# k = 0
# 
# i = 0
# while i < len(a) - 2:
#     if (a[i] == a[i + 1]) and (a[i + 1] == a[i + 2]):
#         k = 0
#         i += 1
#     else:
#         k += 1
#         m = max(m, k)
#         i += 1
# 
# print(m)


# a = open('24.txt').readline()
# c = ['D', 'B', 'A', 'C']
# index = 0
# string = 'DBAC'
#
# while string in a:
#     string += c[index]
#     index += 1
#     if index == len(c):
#         index = 0
# while string not in a:
#     string = string[:-1]
# print(len(string))


# a = open('24.txt').readline()
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1] != 'ad') and (a[i] + a[i + 1] != 'da'):
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)

# a = open('24.txt').readlines()
# k = 0
#
# for x in a:
#     if x.count('A') > x.count('E'):
#         k += 1
# print(k)


# a = open('24.txt').readline()
# k = 0
# c = dict()
#
# for x in set(a):
#     c[x] = 0
#
# for i in range(1, len(a) - 1):
#     if a[i - 1] == a[i + 1]:
#         c[a[i]] += 1
#
# m = max(i for i in c.values())
# for x in c.keys():
#     if c[x] == m:
#         print(x)
#         break


# a = open('24.txt').readlines()
# m = float('inf')
# index = 0
# for x in a:
#     m = min(m, x.count('G'))
# for x in a:
#     if x.count('G') == m:
#         index = x
#         break
#
# m = max(index.count(i) for i in set(index))
# d = set()
# for x in index:
#     if index.count(x) == m:
#         d.add(x)
# print(d)


# a = open('24.txt').readline()
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1] != 'PR') and (a[i] + a[i + 1] != 'RP'):
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# a = open('24.txt').readline()
# k = 1
# # a = 'ABCDDBDAD'
# c = 0
# m = -float('inf')
# i = 0
# while i < len(a):
#     if a[i] == 'D':
#         c += 1
#         if c == 2:
#             index_d = i
#     if c == 3:
#         k -= 1
#         m = max(m, k)
#         # i = index_d - 1
#         c = 0
#         k = 1
#     k += 1
#     i += 1
# print(m)


# a = open('24.txt').readline()
# k = 2
# m = -float('inf')
#
# for i in range(len(a) - 2):
#     if not (a[i] == a[i + 1] == a[i + 2]):
#         k += 1
#         m = max(m, k)
#     else:
#         k = 2
# print(m)


# a = open('24.txt').readline()
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         k += 1
#     else:
#         k -= 1
#         m = max(m, k)
#         k = 0
# print(m)




