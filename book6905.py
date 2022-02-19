# 5. Напишите программу, создающую список из чисел, которые при
# делении на 5 дают в остатке 3 (такие числа вычисляются
# по формуле 5к +3, где к = 0,1,2...). Отобразить этот список
# в прямом и обратном порядке.

def five_1(n):
    l = []
    for i in range(n+1):
        if i % 5 == 3:
            l.append(i)
    return l

def five_2(n):
    l_1 = []
    for i in range(n//5):
        l_1.append(5*i+3)
    return l_1


n = int(input())
print(five_1(n), sorted(five_1(n), reverse=True))
print(five_2(n), sorted(five_2(n), reverse=True))