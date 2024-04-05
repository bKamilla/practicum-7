from math import sqrt
a = int(input("Введите число:"))
b = sqrt(a)
while b % 1 != 0:
    a = int(input('не является полным квадратом'))
    print('')
    b = sqrt(a)
print('является полным квадратом')
