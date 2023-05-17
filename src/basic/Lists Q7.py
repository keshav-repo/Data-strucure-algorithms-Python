list1=[1,1,2,3,4,4,4,5,6]
list2=[]
for i in list1:
    if list1.count(i)>1:
        list2.append(i)
        list2set=set(list2)
print(list2set)
