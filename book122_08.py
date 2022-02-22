# 122_08. Прога, в которой пользолватель вводит целое число
# от 1 до 7 включительно, а прога вводит еназвание дня недели
# соответсвующее этому числу.

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day = int(input("Enter the num of week's day: "))
try:
    print(days[day-1])
except:
    print("The week have only 7 days")
