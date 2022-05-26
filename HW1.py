# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


def get_elements(N):
    list = []
    element = 1

    for i in range(0, N):
        list.append(element)
        element = element * -3

    return list
print(get_elements(100))


# Подсчитать сумму цифр в вещественном числе.

x = 321.543

def digits_sum(x):
    s = str(x)
    sum = 0
    for i in s:
        sum += int(i if i != '.' else '0')
    return sum


print(digits_sum(x))



# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
s = "vavavabcdvav"
t = "vav"
n = 0

for j in range(len(s) - len(t) + 1):
    flag = True
    for i in range(len(t)):
        if s[j + i] != t[i]:
            flag = False
    if flag:
        n += 1

print(n)

# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def get_list_of_products(number):
    list_of_products = []
    multiplication = 1
    for i in range(1, number):
        multiplication *= i
        list_of_products.append(multiplication)
    return list_of_products


print(get_list_of_products(98))








