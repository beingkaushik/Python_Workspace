#Methods of list
'''
1. append method
add the element at the end
'''
print("--------------------")
print("---1.append---")
list1 = []
list1.append(10)
print(list1)
list1.append(20)
list1.append(30)
print(list1)
print("--------------------")
print("---2.insert---")

list1.insert(3,33)
print(list1)


#insert method we can object in specified index'
list2 =[20,40,60,80]
list2.insert(-21,100)
print(list2)
print("--------------------")
'''
3. extend :
    ref.extend(collection)
'''
print("---3.extend---")
l3 = [11,22,33]
l4 = [44,55,66]
l3.extend(l4)
print(l3)
print("--------------------")
'''
4. pop :
    ref.pop()
'''
print("---4.pop---")

l4 = [10,20,30,40]
ele=l4.pop()
print(ele)#40
print(l4)
print("--------------------")
print("we can remove the particular value using its index using same method")
l5 = [11,22,33,44,55]
ele2 = l5.pop(2)
print(ele2)
print(l5)
print("--------------------")
'''
5.remove
    ref.remove(object)
    1st occurance of the object will be removed

'''
print("---5.remove---")
l6 = [20,30,20,40,20]
l6.remove(20)
print(l6)

l6.remove(20)
print(l6)
print("--------------------")

'''
6.clear
    ref.clear()
'''
print("---6.clear---")

print("6.clear")
l6.clear()
print(l6)
print("--------------------")

'''
7.sort()
'''
print("---7.sort---")
l7 = [4,2,-1,7,-7,11,3]
l7.sort()
print(l7)
l7.append("Ben")
print("--------------------")


'''
8.reverse()
'''
print("---8.reverse---")
l7.reverse()
print(l7)
print("--------------------")

'''
9.count
    ref.count(object)
'''
l7 = [22,31,22,98,22,10]
num = l7.count(200)
print(num)
print("--------------------")
'''
10.index
    ref.index(object)
'''

l10 = [20,40,30,20,40,30,30]
ind_1 = l10.index(30)
ind=l10.index(30,3)
print(ind)
l10 = [20,40,30,20,40,30,50,30,70,90]
ind = l10.index(30,6,9)
print(ind)
l1 = [10, 20]
l2 = [30, 40]

l1 += l2
print(l1)
print("--------------------")
