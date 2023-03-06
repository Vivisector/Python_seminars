#task28
# вернуть сумму неотрицательных чисел через плюс 1
a = int(input("первое слагаемое: "))
b = int(input("второе слагаемое: "))

def m_sum(a, b):
    if b == 0:
        return a
    return m_sum(a+1, b-1)

# циклическое сложение (запрещенное)
# def m_sum_f(a,b):
#     for i in range(b):
#         a = a+1
#     return a

print(m_sum(a, b))