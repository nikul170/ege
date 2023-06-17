# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) > 807:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) > 601:
#         print(oct(N)[2:])
#         break
#     N += 1

#
# def f(N):
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) > 77:
#         print(N)
#         break
#     N += 1


# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') > n.count('0'):
#         n += '1'
#     else:
#         n += '0'
#     return int(n, 2)


# N = 1
# m = float('inf')
# while True:
#     if f(N) > 100 and f(N) < m:
#         m = f(N)
#         print(m)
#     N += 1


# def f(N):
#     n = int(bin(N)[2:][-1::-1])
#     return int(str(n), 2)
#
#
# for N in range(1, 101):
#     if f(N) == 9:
#         print(N)


# def f(N):
#     n = bin(2 * N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) > 1017:
#         print(N)
#         break
#     N += 1


# def f(N):
#     N -= N % 4
#     n = bin(N)[2:]
#     n += str(n.count('1') % 2)
#     n += str(n.count('1') % 2)
#     return int(n, 2)
#
#
# m = float('inf')
# N = 1
#
# while True:
#     if f(N) > 100 and f(N) < m:
#         m = f(N)
#         print(m)
#     N += 1

#
# def f(N):
#     n = bin(N)[2:]
#     if N % 2 == 0:
#         n = '1' + n + '0'
#     else:
#         n = '11' + n + '00'
#     return int(n, 2)
#
#
# N = 1
# m = float('inf')
# while True:
#     if sum(map(int, str(f(N)))) > 17 and f(N) < m:
#         m = f(N)
#         print(bin(sum(map(int, str(m))))[2:], m)
#     N += 1

# R
def f(N):
    n = bin(N)[2:]
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n += '1'
    if n.count('1') % 2 == 0:
        n = n + '0'
    else:
        n += '1'

    return int(n, 2)

# N
N = 1
count = 0
while True:
    if 64 <= f(N) < 72:
        count += 1
        print(count)
    N += 1



print(f(12))




