my_object = {
    'Name': 'Sasha',
    'City': 'Kazan',
}

other_dict = {}

# res = [(k: v) for k, v in my_object.items()]
res = [(k, v.upper()) for k, v in my_object.items()]

other_res = dict(res)

print(other_res)
