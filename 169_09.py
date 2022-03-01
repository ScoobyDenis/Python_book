# book169_09. Напишите прогу, в которой создается
#  числовой список. Список заполянется случайными
# числами. Затем между каждой парой элементов
# этого списка вставляется новый элемент, равный
# сумме значений соседних элементов.

from random import randint

l = [randint(0,10) for i in range(4)]
print('original list:', l)
k = 0

for i in range(len(l)-1):
    num = l[k] + l[k+1]
    l.insert(k+1, num)
    k+= 2

print('new:', l)

