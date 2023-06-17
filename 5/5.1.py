# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') % 2 == 0:
#         n += '1'
#         n = '10' + n[2:]
#     else:
#         n += '11'
#         n = '1' + n[2:]
#
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) >= 100:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n = n.replace('1', '2').replace('0', '1').replace('2', '0')
#     return N - int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) > 37:
#         print(N)
#         break
#     N += 2

# def f(N):
#     n = bin(N)[2:]
#     n = n.zfill(8)
#     n = n[:2] + n[-2:]
#     return int(n, 2)
#
#
# for N in range(0, 110):
#     if f(N) == 7:
#         print(N)


# def f(N):
#     n = bin(N)[2:]
#     x = len([1 for i in range(1, len(n), 2) if n[i] == '1'])
#     y = len([0 for i in range(0, len(n), 2) if n[i] == '0'])
#     return abs(x - y)
#
#
# N = 2
# while True:
#     if f(N) == 5:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') % 2 == 0:
#         n += '0'
#         n = '10' + n[2:]
#     else:
#         n += '1'
#         n = '11' + n[2:]
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) >= 16:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n = n.zfill(8)
#     n = n.replace('1', '2').replace('0', '1').replace('2', '0')
#     return int(n, 2) - N
#
#
# for i in range(0, 256):
#     if f(i) == 133:
#         print(i)


def f(N):
    n = bin(N)[2:]
    n = n.zfill(8)
    n = n.replace('1', '2').replace('0', '1').replace('2', '0')
    return int(n, 2) - N


for N in range(0, 256):
    if f(N) == 111:
        print(N)