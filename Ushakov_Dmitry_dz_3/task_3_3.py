# 3.Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
def thesaurus(*args):
    out_dict = {}
    for name in args:
        if out_dict.get(name[0]):
            out_dict[name[0]].append(name)
        else:
            out_dict[name[0]] = [name]
    return out_dict


print("Иван", "Мария", "Петр", "Дмитрий", "Ольга", "Илья")
