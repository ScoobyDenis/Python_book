# 3. Напишите программу, в которой расстояние, указанное
# в милях, переводится в км. одна миля равна примерно
# 1.6 км. Расстояние в милях вводится пользователем с клавиатуры.

def conv_mile_to_km(x):
    return x*1.6

print(conv_mile_to_km(int(input("Enter mile for convertation "))))