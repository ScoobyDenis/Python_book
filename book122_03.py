# 122_03. напишите программу, которая на основе списка
# из натуральных чисел формирует целое число. Пример:
# [1,23, 45] = 12345

l = list(map(int, input("enter digits separated by spaces: ").split()))
for i in l:
    print(int(i), end="")