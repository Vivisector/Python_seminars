# Задача 2: Найдите сумму цифр трехзначного числа
# n = 123
n = int(input('введите число: '))
sum = 0  # test commits changes
while n > 0:
    sum = sum + n % 10
    n = n // 10

print(sum)
