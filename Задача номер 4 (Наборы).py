two_set = {155, 122, 144, 591, 336, 1054}

two_set.add(121)

other_set = {122, 155, 180, 161}

all_set = two_set.intersection(other_set)

res = list(all_set)

print(res)
print(type(res))
