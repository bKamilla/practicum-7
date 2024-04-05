string = input("Введите строку:")
result = ""
i = 2
while i < len(string):
    result += string[i]
    i += 3
print(result)