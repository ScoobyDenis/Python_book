# 2.Напишите программу, в которой пользователь должен
# ввести текущий год и год своего рождения. программа
# вычисляет возраст пользователя и выводит
# соответствующее сообщение.

def age(a,b):
    return a - b

year = int(input("What year is it now? "))
year_old = int(input('How old are you? '))
print("You were born in", age(year, year_old))
