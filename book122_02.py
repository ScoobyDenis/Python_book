# 122-2. Напишите программу, в которой пользователь вводит целое
# число, а прога кажду цифру меняет "на дополнение до 9"

def reverse_num(num):
    l = []
    for i in num:
        l.append(abs(int(i)-9))
    return l
num = input("Введите целое число ")

print(*reverse_num(num), sep="")