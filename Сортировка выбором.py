from random import randint

N=7
a=[]
for i in range(N):
    a.append(randint(1,20))
print(a)

j=N-1#здесь j являеться счетчиком и индексом последнего элемента из расматриваемых в цикле for
while j>0:
    ind=0
    for i in range(1,j+1):
        if a[i]>a[ind]:
            ind=i#сохраняем индекс i большего элемента , чтобы не потерять его на следующей итерации и продолжить сравнивать оставшиеся элементы с ним
    b=a[ind]
    a[ind]=a[j]
    a[j]=b#самый большой эл. исследуемого отрезка списка , записывается в конец этого отрезка
    j-=1
print(a)
