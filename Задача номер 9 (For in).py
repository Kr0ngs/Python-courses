my_object = {
    'x': 10,
    'y': 'Sasha',
    'z': 12
}


def otvet(a):
    for key in a:
        print(a[key])
        if isinstance(a[key], int):
            print("Yes")
        elif isinstance(a[key], str):
            print('No')
        else:
            print('Error')


otvet(my_object)
