#2. Дан список:['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
user_lst=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(user_lst)

length_of_list: int = len(user_lst)
id_name = id(user_lst)
for _ in range(length_of_list):
    elem = user_lst.pop(0)
    if  elem.isdigit() and elem.isalnum():
        user_lst.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        user_lst.append(f'"+{int(elem):02d}"')
    else:
        user_lst.append(elem)
print(' '.join(user_lst))

