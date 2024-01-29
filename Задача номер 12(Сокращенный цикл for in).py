print("Определить кол-во имен, в которых кол-во букв больше 5")
name_list = ['Aleksandr', 'Nikita', 'Ivan', 'Lesha',]

res = [v for v in name_list if len(v) > 5]

print("Cписок имен:", name_list)
print("Cписок имен, у которово кол-во букв в имени больше 5:", res)
other_res = len(res)

print("Кол-во имен:", other_res)
