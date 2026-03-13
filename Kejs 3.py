n = int(input("Введите количество элементов массива: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))

max_index = a.index(max(a))
min_index = a.index(min(a))

left = min(max_index, min_index)
right = max(max_index, min_index)

sum_negative = 0
for i in range(left + 1, right):
    if a[i] < 0:
        sum_negative += a[i]

print("Сумма отрицательных элементов между максимальным и минимальным:", sum_negative)
