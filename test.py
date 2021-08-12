# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу
# 6. Получить список ключей словаря

dict_one = {'key1': 'value1', 'key2': 'value2'}
print(dict_one)
dict_one['key3'] = 22
print(dict_one)
dict_one[('one', 'two', 'three')] = [1, 'four', "five"]
print(dict_one)
get_el_by_key = dict_one.get('key2')
print(get_el_by_key)
del_el_by_key = dict_one.pop('key3')
print(dict_one)
keys = dict_one.keys()
print(keys)

#Do some changes for another branch
