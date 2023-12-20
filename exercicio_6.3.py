#faça um programa que percorra duas lista e gereum uma terceira sem elemento repetidos.
list1 = [12,5,8,6,4]
list2 = [5,8,7,12,5]
list3 = []

for n in list1:
    list3.append(n)
    print(n)

for n1 in list2:
    if n1 not in list3: 
        list3.append(n1)            

print(list1,list2,list3)
