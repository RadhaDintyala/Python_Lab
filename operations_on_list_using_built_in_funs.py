list1=[1,2,3,4,5,6,7,8,9,10]

del list1[3]#deletion
print(list1)

list1.append(11)#append(addition at end)
print(list1)

list2=[12,13,14,15]
list1.extend(list2) #extend(addition of another list at end)
print(list1)

print(max(list1)) #returns maximum value in the list
print(min(list1)) #returns minimum value in the list

list3=list1.copy()
print(list3) #Copies the contents of list1 to list3