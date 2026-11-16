print("\n------------Methods of Dict-----------")
print("\n---1.setdefault---\n")
d1 = {}
d1.setdefault(2,20.4)
d1.setdefault(3)
print(d1)

d2 = {1:10,2:20}
d3 = {3:30,4:40}
print("\n---2.update---\n")

d3.update(d2)
print(d3)

print("\n---3.get---\n")
d4 = {3:33,4:44}
print(d4.get(4))
print(d4.get(8))

print("\n----4.pop---\n")
d5 = {9:99,8:88,7:77}
print(d5.pop(8))
print(d5)

print("\n----5.popitem---\n")
d6 = {19:99,18:88,17:77}
print(d6.popitem())
print(d6)

print("\n----6.clear---\n")
d6.clear()
print(d6)
print("\n----7.keys---\n")
d7 = {4:5,6:7,8:9}
print(d7.keys())
print("\n----8.Values---\n")
print(d7.values())
print("\n----9.items---\n")
print(d7.items())


