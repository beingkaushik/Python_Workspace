print("-------Methods of sets-------")
print("----1.add----")
s = set()
s.add(20)
s.add(10)
s.add(10)
print(s)

print("----2.update----")
s2={7,8,9}
s3={10,11,12}
s2.update(s3)
print(s2)

dance = [ "Amy","Ben","Chad"]
sing = ["Chad","Den"]
draw = ["Amy","Eric"]
dance.extend(sing)
dance.extend(draw)
print(dance)
set_of_students = set()
set_of_students.update(dance)
print(set_of_students)
print(len(set_of_students))

print("---3.pop---")
s4 = {11,22,33,44}
ele = s4.pop()
print(ele)
print(s4)

print("---4.remove---")
s5 = {7,9,8,4,5}
s5.remove(8)
print(s5)

print("\n---5.discard---")
s6 = {10,20,30,40}
s6.discard(30)#it removes object if its present otherwise its doesn't raise error
print(s6)
s6.discard(300)
print(s6)

print("\n---6.clear---")
s6.clear()
print(s6)

print("\n---7.issubset---")
s7 = {11,33}
s8 = {33,22,11}
bv = s8.issubset(s7)
print(bv)

print("\n---8.issuperset---")
print(s8.issuperset(s7))

print("\n---9.isdisjoint---")
s8 = {44}
print(s8.isdisjoint(s7))

print("\n---10.union----")
s06 = {90,80,70}
s07 = {70,60,50}
us = s06.union(s07)
print(us)

print("\n---11.intersection---")
cs = s06.intersection(s07)
print(cs)
print("\n---12.difference---")
ds = s06.difference(s07)
print(ds)

print("\n---13.symmetric_difference---")
sd = s06.symmetric_difference(s07)
print(sd)

