# 8. Числа Фибонначи. 1,1, 2, 3, 5, 8, 13.... Количество
# чисел вводится с клавиатуры.

def fibannachi(n):
    fib =[1,1]
    for i in range(n):
        fib.append(fib[i] + fib[i+1])
    return fib

n = int(input())

print(*fibannachi(n))