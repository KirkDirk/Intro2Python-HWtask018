# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

def checklist1(li, a):
    matches = 0
    for j in range(len(li)):
        if li[j] == a: matches +=1
    if matches>1: return False
    else: return True

list1 = [1, 3, 4, 5, 8, 5, 4, 7, 20]
list2 = []
for i in list1:
    if checklist1(list1, i): list2.append(i)
print(list2)