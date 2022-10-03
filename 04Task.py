# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


while 1:
    n = int(input('Введите десятичное число\n'))
    if n != 0:
        print(binary(n))
    else:
        break
binary(n)
