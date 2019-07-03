from collections import OrderedDict

def FirstNonRepeatChar(str):
    my_dict = OrderedDict()
    for char in str:
        if char in my_dict.keys():
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    for key, value in my_dict.items():
        if value == 1:
            return key


if __name__ == "__main__":
    str = "GeeksforGeeks"
    print(FirstNonRepeatChar(str))