# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def get_sum(elements):
    sum = 0
    for i in range(0, len(elements), 2):
        sum += elements[i]
    return sum


print(get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


def get_multi(elements):
    list = []
    for i in range(0, (len(elements) + 1) // 2):
        list.append(elements[i] * elements[len(elements) - 1 - i])
    return list

print(get_multi([2, 3, 4, 5, 6]))
print(get_multi([2, 3, 5, 6]))

# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_diff(elements):
    min = 1
    max = 0
    for i in range(0, len(elements)):
        if elements[i] % 1 < min and elements[i] % 1 != 0.0:
            min = elements[i] % 1
        if elements[i] % 1 > max:
            max = elements[i] % 1
    return max - min



print(get_diff([1.1, 1.2, 3.1, 5, 10.01]))




# Написать программу преобразования десятичного числа в двоичное

def dec_to_bin(number):
    str = ''
    while number > 0:
        if number % 2 == 0:
            str += '0'
        else:
            str += '1'
        number //= 2
    return str[::-1]


print(dec_to_bin(28))

