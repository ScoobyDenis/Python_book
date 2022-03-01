# book169_08. Напишите прогу, в которой создается числовой
# список. Список заполняется случайными числами. Затем
# элементы с четными индексами сортируются в порядке возрастания,
# а элементы с нечетными индексами сортируются в порядке убывания.

from bubble import bubble_sort
from random import randint


l = [randint(0,100) for i in range(10)]
print(f'original list {l}')
chet_l = [l[i] for i in range(len(l)) if i%2==0]
nechet_l = [l[i] for i in range(len(l)) if i%2!=0]
print(f'even index {chet_l}')
print('Sorted: ', bubble_sort(chet_l))
print(f'odd index {nechet_l}')
print('Sorted:', bubble_sort(nechet_l))