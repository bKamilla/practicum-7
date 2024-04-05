N, K, R = map(int, input("Введите длину в 1 день, изменение в %,минимум:").split())
n = 1
while N < R:
    N = N * (1 + (K / 100))
    n += 1
print(n)
