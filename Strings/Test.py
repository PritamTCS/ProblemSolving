string = "Pritaammmmm"
my_dict = {}

for s in string:
    if s in my_dict.keys():
        my_dict[s] += 1
    else:
        my_dict[s] = 1


print(my_dict)


