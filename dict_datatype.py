print("---------------Dictionary---------------")


print("\n----Syntax to create empty dictionary----")
empty_dict = dict()
print(type(empty_dict))


print("\n----Syntax to create  dictionary with elements----")
dict_items = {10:100,20:400,30:900}
print(dict_items)

print("\n----------Synatax to Access a value in a dict --------")
print(dict_items[20])


print("\n--------Syntax to create/modify a value in a dict--------")
dict_items[20] = 500
print(dict_items)

dict_items[21] = 700
print(dict_items)
