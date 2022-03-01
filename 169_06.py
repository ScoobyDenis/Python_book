# 169_06. Сортировка пузырьком

l = [15, 12, -2, 25, 9, 6, 7, 1]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)
