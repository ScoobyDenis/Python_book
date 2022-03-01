# 169_07. Напишите прогу с функцией, которая для
# списка, переданного аргументом, возвращает список
# из двух элементов: значение наибольшего элемента
# в списке и индекс этого элемента в списке(если таких
# элементов несколько, то индекс первого из таких
# элементов)

def max_min(l):
    big = max(l)
    small = min(l)
    ind_big = l.index(big)
    ind_small = l.index(small)
    print(f'max digit - {big}, its index - {ind_big}')
    print(f'min_digit - {small}, its index - {ind_small}')

my_list = [0, -5, 15, -25, 525, 19, 14, -25]
max_min(my_list)
