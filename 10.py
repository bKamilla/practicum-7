k = 0
b = -1
a = -1
a = float(input("Введите температуру:"))
while a != 0:
    if a < b:
        k += 1
    b = a
    a = float(input("Введите тепературу:"))
print(k)