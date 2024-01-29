my_list = ['Sasha', True, 19, 'asdasda', 1231.51]


def filter_list(list, a):
    return [value for value in list if isinstance(value, a)]


res = filter_list(my_list, str)

print(res)
