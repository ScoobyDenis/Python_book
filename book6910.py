# 10. Напишите программу, в которой описана функция,
# возвращающая результатом сумму нечетных чисел.
# Количество чисел передается аргументом функции.

def sum_odd_nums(a, b):
    count = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            count += i
    return count

a = int(input("От какого числа начинать счет: "))
b = int(input("До какого числа: "))
print(sum_odd_nums(a,b))
