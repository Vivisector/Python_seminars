# task30
# a = 7  # первый элемент
# n = 2  # шаг
# d = 25  # число элементов
a = int(input('введите начальный элемент последовательности: '))
n = int(input('введите приращение: '))
d = int(input('введите длину последовательности: '))
li = [a]
for i in range(d-1):
    a = a + n
    li.append(a)
print(*li)