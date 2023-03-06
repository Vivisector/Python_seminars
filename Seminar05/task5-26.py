#task26
# А возвести в степень B
a = int(input("основание степени: "))
b = int(input("показатель стпени: "))
def mpow(a,b):
    if b == 0:
        return 1
    return a * mpow(a, b-1)

print(mpow(a, b))
