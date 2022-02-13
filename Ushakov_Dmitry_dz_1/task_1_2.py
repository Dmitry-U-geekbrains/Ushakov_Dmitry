# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
lst = []
sum_number1 = 0
sum_number2 = 0
for i in range(1, 1001):
    if i % 2 != 0:
        lst.append(i ** 3)
for idx in range(len(lst)):
    num_sum = 0
    j = lst[idx]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum_number1 += lst[idx]
    lst[idx] += 17
    num_sum = 0
    j = lst[idx]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        sum_number2 += lst[idx]
print(sum_number1)
print(sum_number2)
