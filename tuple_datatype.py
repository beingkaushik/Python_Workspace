print("---------empty tuple syntax-----------\n")
empty_tuple = ()
print(type(empty_tuple))#<class 'tuple'>
print("\n")
print("---------Another way of empty tuple syntax-----------\n")

empty_tuple_1 = tuple()
print(type(empty_tuple_1))#<class 'tuple'>


print("size of empty tuple",len(empty_tuple))
print("--------Tuple with elements inside------------\n")

tuple1 = (10,20,30,40)
print(tuple1)
print(len(tuple1))#len 4
print("---accessing the value using index----")
t = (10,20,30,40,50)
print(t[-2])
# Whenever  a single value is inside tuple, remember to have commma at the end
t2 = (60,)

dt = type(t2)
print(dt)

print("---Methods of Tuples (only 2)-----")
print("----1.count----")
l11 = (10,30,10,40,10)
num = l11.count(10)
print(num)
print("----2.index----")

ind = l11.index(40)
print(ind)

