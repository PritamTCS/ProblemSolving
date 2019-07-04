from collections import OrderedDict
string = "Pritaammmmm"
my_dict = {}

for s in string:
    if s in my_dict.keys():
        my_dict[s] += 1
    else:
        my_dict[s] = 1


# print(my_dict)


my_dict1 = OrderedDict()

my_dict1['a1'] = "Test1"
my_dict1['a2'] = "Test2"

# print(my_dict1)

arr = [1, 2, 5, 1, 7, 2, 4, 2]
# mp = { i: 0 for i in arr}
# print(mp.keys())

mp = {}

for i in arr:
    if i in mp.keys():
        mp[i] += 1
    else:
        mp[i] = 1
# print(mp)
# print(mp.keys())

lst = [2, 5, 2, 8, 5, 6, 8, 8]
dict1 = {}

for k in lst:
    if k in dict1.keys():
        dict1[k] += 1
    else:
        dict1[k] = 1
print(dict1)
lst_sort = sorted(dict1.values())
print(lst_sort)
# for k, v in dict1.items():
#     for i in lst_sort:
#         if i == v:
#             for j in range(i):
#                 print(k)

# for k, v in dict1.items():
#     if v in lst_sort:
#         for i in range(v):
#             print(k)

# for i in lst_sort:
#     for k, v in dict1.items():
#         if i == v:
#             for j in range(i):
#                 print(k)

for i in lst_sort:
    for k, v in dict1.items():
        if v == i:
            for j in range(i):
                print(k)
