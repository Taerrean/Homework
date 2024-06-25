n = int(input('Введите число из первой вставки: '))
num1 = n
num2 = n
result = ''
reverse = []
for i in range(1, num1+1):
    for j in range(1, num2 + 1):
        if str(i) + str(j) in reverse or i == j:
            continue
        if n % (i+j) == 0:
            result += str(i) + str(j)
            reverse.append(str(j) + str(i))
print(result)