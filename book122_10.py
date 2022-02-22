# 122_10. Прога для решения уравнения Ax = B - A - 1.
# Параметры А и В вводятся пользователем. Уравнение
# имеет решение x = (B-1)/A-1, если А != 0. Предложите
# разные варианты программы, в том числе с обработкой исключений.
#  При А = 0, а В = 1 - решением явл любое число. а при А = 0,
# В != 1 - решений у уравнения нет.

A, B = map(int, input("Enter two nums: ").split())
if A == 0 and B == 1:
    print("Solution is any number")
elif A == 0 and B != 1:
    print("The equation have not a solutions")
else:
    print(f"The solution is {(B-1)/A-1}")

