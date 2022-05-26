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


# показать натуральные числа не больше N

def show_numbers(N):
    for i in range(1, N + 1):
        print(i, end=",")

show_numbers(100)
print()

# проверить является ли одно число квадратом другого

def is_square(a, b):
    if a * a == b or b * b == a:
          print('True')
    else:
         print('False')


is_square(2, 4)
is_square(3, 5)


# вывести числа которые делятся на 3, но не делятся на 5, до N

def division(N):
    for i in range(3, N + 1, 3):
        if i % 5 != 0:
           print(i, end=' ')


division(100)
#print('\nEnter a number:')

k = input()
print(k)

box = [1, 2, 3, 5]
box.append(7)
box.append(43)
box.append(35)
box.sort()
print(box)

# Подсчитать сумму цифр в вещественном числе.

x = 321
print(sum(map(int, str(x))))

# Написать программу получающую набор произведений чисел от 1 до N.
def get_factorial_list(n):
  list = []
  multi = 4
  for i in range(4, number + 1):
      multi *= i

  print(multi)





