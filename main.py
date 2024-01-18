my_cars = ['BMW', 'Chevrolet']
copied_cars = list(my_cars)
copied_cars.append('Audi')

print(copied_cars)
# ['BMW', 'Chevrolet', 'Audi']
print(my_cars)
# ['BMW', 'Chevrolet']
print(id(my_cars) == id(copied_cars))
# False
