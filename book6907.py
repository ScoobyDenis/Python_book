# 7. Напишите программу, в которой вычисляется факториал числа.
# Факториал - это произведение всех чисел от единицы до этого числа.

def factorial(n):
    count = 1
    for i in range(1, n+1):
        count *=i

    return count

n = abs(int(input("Enter integer: ")))
print(factorial(n))


