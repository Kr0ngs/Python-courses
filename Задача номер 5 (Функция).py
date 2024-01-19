def merge_lists_to_dict(a, b):
    c = zip(a, b)
    d = dict(c)
    return d


fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

res = merge_lists_to_dict(fruits, quantities)
print(res)
print(type(res))

fruits = ['apple', 'banana', 'lime']
quantities = [255, 154, 111]

res1 = merge_lists_to_dict(fruits, quantities)
print(res1)
