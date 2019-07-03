string = "Pritaammmmm"
my_dict = {}

for s in string:
    if s in my_dict.keys():
        my_dict[s] += 1
    else:
        my_dict[s] = 1


print(my_dict)


from collections import OrderedDict

my_dict1 = OrderedDict()

my_dict1['a1'] = "Test1"
my_dict1['a2'] = "Test2"

print(my_dict1)

arr = [1, 2, 5, 1, 7, 2, 4, 2]
# mp = { i: 0 for i in arr}
# print(mp.keys())

mp = {}

for i in arr:
    if i in mp.keys():
        mp[i] += 1
    else:
        mp[i] = 1
print(mp)
print(mp.keys())



