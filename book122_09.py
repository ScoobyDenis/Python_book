# 122_09. Прога, в которой пользователь вводит два
# действительных числа, а прога проверяет , какие из чисел
# больше. Используйте тернарный оператор и обработку исключительных
# ситуаций.


try:
    a, b = map(int, input("Enter two digits sep by spaces: ").split())
    print(a if a > b else b)
except ValueError:
    print("need enter nums")
except SyntaxError:
    print("only digits")