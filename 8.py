n = int(input("Введите последнее число:"))
k = 0
while n > 2:
    n = n/2
    k += 1
if n == 1:
    print(k)
elif n == 2:
    print(k+1)
else:
    print(k+1)