# book169_10. Напишите прогу, в которой создается
# два списка одиннакового размера. На основе этих списков
# поочередной вставкой элементов из первого и второго списка
# формируется новый список.

from random import randint

l_1 = [randint(-20, -1) for i in range(4)]
l_2 = [randint(1, 20) for i in range(4)]
print(l_1)
print(l_2)
l_3 = []
for i in range(4):
    l_3.append(l_1[i])
    l_3.append(l_2[i])
print(l_3)
