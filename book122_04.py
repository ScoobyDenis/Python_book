# 122_04. Напишите программу, в которой сравниваются на предмет
# равнества два числовых списка. Два списка равны, если они
# одинакового размера и у них совпадают соответсвующие элементы.

a = list(map(int, input("Enter digit separated by spaces: ").split()))
b = list(map(int, input("Enter digit separated by spaces: ").split()))
if len(a) != len(b):
    print("Lists is not identical")
else:
    if sorted(a) == sorted(b):
        print("Perfect, it is identical!")


