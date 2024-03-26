import math

def square():
    aInt = input("сторона: ")
    a = float(aInt)  # Преобразуем вещественное число
    if a.is_integer():  # Проверяем, является ли число целым
        s = a * a
        print(s)
    else:
        a = math.ceil(a)  # Округляем вверх
        s = a * a
        print(s)

square()