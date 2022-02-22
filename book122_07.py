# 122_07. Прога, в которой пользователь вводит три целых числа,
# а прога проверяет , являются ли эти числа членами арифметической
# последовательности(каждый новый член получается путем прибавления
# к нему определенного фиксированного числа).

a, b, c = map(int, input("Enter three nums: ").split())
x = b-a
y = c-b
if x == y:
    print("This is arithmetic sequence")
else:
    print("It is not arithmetic sequence")