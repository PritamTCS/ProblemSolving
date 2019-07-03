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
