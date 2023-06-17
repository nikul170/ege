# import collections
#
# a = open('24.txt').readline()
# c = []
# for i in range(len(a) - 1):
#     if a[i] == 'A':
#         c.append(a[i + 1])
# print(collections.Counter(c).most_common())


# a = open('24.txt').readline().split('A')
# m = -float('inf')
# for i in range(len(a) - 1):
#     m = max(m, len(a[i]) + len(a[i + 1]) + 1)
# print(m)

import collections

# a = open('24.txt').readlines()
# m = min(i.count('N') for i in a)
# for i in a:
#     if i.count('N') == m:
#         c = i
#         break
# ma = max(c.count(i) for i in c)
# for i in c:
#     if c.count(i) == ma:
#         print(i)


# a = open('24.txt').readline()
#
# count = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] in 'ABEF' and a[i + 1] in 'ABEF':
#         count += 1
#         m = max(m, count)
#     else:
#         count = 1
# print(m)

# a = open('24.txt').readline()
# count = 0
# m = -float('inf')
# for i in range(len(a) - 5):
#     if a[i:i + 5: 2] == 'AAA':
#         count += 1
# print(count)


# a = open('24.txt').readlines()
# count = 0
# for x in a:
#     if x.count('E') > x.count('A'):
#         count += 1
# print(count)

# a = open('24.txt').readline()
# mi = min(a.count(i) for i in set(a))
# ma = max(a.count(i) for i in set(a))
# print(ma - mi)

# count = 0
# for i in range(100, 200):
#     count += 1
# print(count)







