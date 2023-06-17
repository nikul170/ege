# from itertools import product
#
# k = 0
# for x in product('ЛЕТО', repeat=4): #Перебираем абсолютно все значения из букв ЛЕТО длины 4, можно так product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО')
#     s = ''.join(x)  #преобразуем кортеж в строку
#     if s[0]  in 'ЛТ':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('КУМА', repeat=5):
#     s = ''.join(x)
#     if s[0] in 'КМ' and s[-1] in 'АУ':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ABC', 'ABC', 'ABC', 'ABC', 'ABCX'):
#     s = ''.join(x)
#     k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЭЮЯ', 'АБВГ', 'АБВГ', 'АБВГ', 'ЭЮЯ', ):
#     s = ''.join(x)
#     k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('НРОТ', repeat=6):
#     s = ''.join(x)
#     if s.count('О') == 1:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('КАНТ', repeat=6):
#     s = ''.join(x)
#     if s.count('К') == 2:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('АНИМЕ', repeat=6):
#     s = ''.join(x)
#     if s.count('Е') == 3:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЗЕРКАЛО', repeat=6):
#     s = ''.join(x)
#     if (s.count('К') == 1) and (s.count('А') == 3):
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЛЕТО', repeat=4):
#     s = ''.join(x)
#     if s.count('Е') >= 1:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('КАТЕР', repeat=5):
#     s = ''.join(x)
#     if s.count('Р') >= 2:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЖИРАФ', repeat=5):
#     s = ''.join(x)
#     if s.count('Ж') == 1 and s[0] != 'Ф' and s[-1] != 'Р':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for i in range(4,7):
#     for x in product('АНИМЕ', repeat=i):
#         k += 1

# for x in product('АНИМЕ', repeat=5):
#     k += 1
# for x in product('АНИМЕ', repeat=4):
#     k += 1
# for x in product('АНИМЕ', repeat=6):
#     k += 1
# print(k)

# from itertools import product
#
# k = 0
# c = 0
# for x in product('АИМРЯ', repeat=4):
#     c += 1
#     s = ''.join(x)
#     if c == 211:
#         print(s)

# from itertools import permutations
#
# k = 0
# for x in set(permutations('АССАСИН')):
#     k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# for x in set(permutations('КАЛИЙ')):
#     s = ''.join(x)
#     if s[0] != 'Й' and 'ИА' not in s:
#         k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# for x in set(permutations('ПЕСКАРЬ')):
#     s = ''.join(x)
#     # if s[0] != 'Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
#     if s[0] != 'Ь' and all(sub not in s for sub in ['ЬА', 'ЬЕ', 'ЬР']):
#         k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# w = ['ОУ', 'УО', 'КЛ', 'ЛК', 'КН', 'НК', 'ЛН', 'НЛ']
# for x in set(permutations('КОЛУН')):
#     if all(sub not in s for sub in w):
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('01234567', repeat=4):
#     s= ''.join(x)
#     if s[0] != '0' and s[-1] in '04':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('01234567', repeat=4):
#     s = ''.join(x)
#     if s[0] >= s[1] >= s[2] >= s[3]:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('01234567', repeat=5):
#     s = ''.join(x)
#     # if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
#     if all(s[i] != s[i + 1] for i in range(len(s) -1)):
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('АКРУ', repeat=5):
#     s = ''.join(x)
#     k += 1
#     if k == 150:
#         print(s)
#         break

# from itertools import product
#
# k = 0
# for x in product('АОУ', repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s=='УАУАУ':
#         print(k)
#         break

# from itertools import product
#
# k = 0
# for x in product('КРЕСЛО', repeat=4):
#     s = ''.join(x)
#     if s[0] in 'КРСЛ' and s[-1] in 'ЕО':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ'):
#     k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ПУЛЯ', repeat=6):
#     s = ''.join(x)
#     if s.count('У') == 2:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЛОДКА', repeat=4):
#     s = ''.join(x)
#     if s.count('О') >= 2:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('САЛО', repeat=6):
#     s = ''.join(x)
#     if s.count('О') <= 3:
#         k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# for x in set(permutations('ИГРОК')):
#     s = ''.join(x)
#     if s[0] != 'К' and 'РОК' not in s:
#         k += 1
# print(k)

# from itertools import permutations, product
#
# k = 0
# w = list(product('АОУИ', repeat=2)) + list(product('БКЛН', repeat=2))
# for x in set(permutations('АБИКОЛУН')):
#     s = ''.join(x)
#     if all(''.join(sub) not in s for sub in w):
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('AB123', repeat=8):
#     s = ''.join(x)
#     if (s.count('A') + s.count('B')) == 2:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('01234', repeat=6):
#     s = ''.join(x)
#     if s[0] not in '01' and s[-1] not in '34':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ВИШНЯ', repeat=6):
#     s = ''.join(x)
#     if s.count('В') <= 1 and  s[0] not in 'Ш' and s[-1] not in 'ИЯ':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ABCD', repeat=4):
#     s = ''.join(x)
#     if s[0] <= s[1] <= s[2] <= s[3]:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ГЕПАРД', repeat=5):
#     s = ''.join(x)
#     if s[0] not in 'А' and s[-1] not in 'Е' and s.count('Г') == 1:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('0123456789', repeat=3):
#     s = ''.join(x)
#     if s[0] != '0' and s[0] <= s[1] <= s[2]:
#         k+=1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ДЕЙКСТРА', repeat=6):
#     s = ''.join(x)
#     if any(sub in s for sub in ['ЙД', 'ЙК', 'ЙС', 'ЙТ', 'ЙР']):
#         print(s)
#         k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# for x in permutations('ВАЙФУ', r=4):
#     s = ''.join(x)
#     if s[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
#         k += 1
# print(k)

# from itertools import permutations
#
# k = 0
# for x in set(permutations('МИМИКРИЯ')):
#     k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЕЛМРУ', repeat=4):
#     k += 1
#     s = ''.join(x)
#     if s[0] == 'Л':
#         print(k)
#         break

# from itertools import product
#
# k = 0
# for x in product('АГИЛМОРТ', repeat=4):
#     k += 1
#     s = ''.join(x)
#     if s[2] == 'И' and s[3] == 'М':
#         print(k)

# from itertools import product
#
# k = 0
# for x in product('АИМРЯ', repeat=4):
#     k += 1
#     s = ''.join(x)
#     if s == 'АРИЯ':
#         print(k)

# from itertools import product
#
# k = 0
# for x in product('ШКОЛА', repeat=3):
#     s = ''.join(x)
#     if s.count('К') == 1:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ГАФНИЙ', repeat=4):
#     s = ''.join(x)
#     if s[0] != 'Й' and any(c in s for c in 'ИА'):
#         print(s)
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ИЙКНОТЕ', repeat=7):
#     s = ''.join(x)
#     if 'КОТ' in s:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('ЛЕТО', repeat=4):
#     s = ''.join(x)
#     if s[0] in 'ЛТ':
#         print(s)
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('КУМА', repeat=5):
#     s = ''.join(x)
#     if s[0] in 'МК' and s[-1] in 'УА':
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('СЛОН', repeat=5):
#     s = ''.join(x)
#     if 0 < s.count('О') <= 3:
#         k += 1
# print(k)

# from itertools import product
#
# k = 0
# for x in product('АГИЛМОРТ', repeat=4):
#     k += 1
#     s = ''.join(x)
#     if s[-2] == 'И' and s[-1] == 'М':
#         print(k, s)

from itertools import product

k = 0
for x in product('0123456789', repeat=7):
    s = ''. join(x)
    if int(s) % 5 == 0 and len(set(s)) == 7 and all((int(s[c]) % 2 == 1 and int(s[c + 1]) % 2 == 0) or (int(s[c]) % 2 == 0 and int(s[c + 1]) % 2 == 1) for c in range(len(s) - 1)):
        k += 1
        print(s)
print(k)