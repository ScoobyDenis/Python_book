# 9. Напишите программу, в которой описана функция,
# возвращающая результатом второе по величине число в списке,
# переданном функции в качестве аргумента.

def pre_max(a):
    a = sorted(a, reverse=True)
    a.pop(0)
    return max(a)


l = list(map(int, input("Enter the numbers through space: ").split()))
print(pre_max(l))