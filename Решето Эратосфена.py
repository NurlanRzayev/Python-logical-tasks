n = int(input())

a = []
for i in range(n + 1):
    a.append(i)

a[1] = 0 # обнуляется первое не простое число
i = 2
while i <= n:
    if a[i] != 0: # если значение ячейки не было обнулено, то в этой ячейки содержится простое число
        j = i + i # значения элементов списка совпадают с их индексами, первое кратное для простого числа будет в два раза больше его
        while j <= n: # в этом цикле обнуляются все составные числа с делителем i
            a[j] = 0
            j = j + i
    i += 1

a = set(a)
a.remove(0)
print(a)
