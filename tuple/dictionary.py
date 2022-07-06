#dict() - словарь -> упорядочное коллекция элементов (3.7 -> ordered) каждый элемент в  словаре содержиться в паре ключ: значения 

#ключи должны быть уникальными и быть неизменяемым типом данных( str, int, tuple, etc) тогда как начениями могут выступать любые типы данных

# thisdict = {
#     'brand' : 'MLP',
#     'pony' : 'rainbow dash',
#     'year' : 2010
# }
# print(thisdict)
# print(type(thisdict))


#Hash tables, ассоциативный массив, dictionary, object(js) == dictionary 

# a = {1,2,3} #set
# some_tuple = 1,2,3
# print(type(some_tuple))
# print(some_tuple)

# some_dict = {}
# print(type(some_dict))
# key_values = {'key': 'value', 'key1':'value1'}
# print(type(key_values))

# dict_created_with_function = dict()
# print(type(dict_created_with_function))

# ponydict = dict((('key', 'value'), ('key2', 'value2')))
# print(ponydict)
# print(type(ponydict))


#--------------------------------------------------------




# user_info = {
#     'first_name': 'apple',
#     "last_name" : 'jack',
#     "age" : '20',
#     'email':'applejack@gmail.com',
#     'role' : 'farmer',
#     'list' : [1,2,3],
#     #'first_name' : 'pinkie pie'
# }
# print(user_info['first_name'])
# print(user_info.get('age'))
# print(dir(user_info))

# print(user_info.items())
# for items in user_info.items():
#     print(items)

# print(user_info.keys())
# user_info['height'] = 24
# user_info['age'] = 30
# print(user_info.keys())
# print(user_info)

# for value in user_info.values():
#     print(value)

#pop() - удаляет элеент по определенному ключу
#popitem() - удаляет последнюю пару в словаре

# print(user_info)

# # user_info.pop('list')
# # user_info.pop('email')
# user_info.pop('list')
# user_info.popitem()
# user_info.popitem()

# print(user_info)

# setdefault(key, [default_value]) = работает так же как и метод get(), но если такого ключа не существует то он создаст новую пару значений
#1 cпособ применнения получения значений
# dict_ ={'name': 'rainbow', 'age' :21}
# result = dict_.setdefault('age')
# print(result)
#2 способ добавление пары
# dict_ ={'name': 'rainbow', 'age' :21}
# result = dict_.setdefault('adress', 'ponivile')
# print(dict_)

# print(user_info)
# user_info.update({'name': 'lyra'})
# user_info.update({'height': 185})
# print(user_info)


# print(user_info)
# user_info['first_name'] = 'bonbon'
# user_info['height'] = 185
# print(user_info)

#---------------------------------------
# roles = {
#     0: 'admin',
#     1: 'moderator',
#     2: 'vendor',
#     3: 'customer',
#     4: 'guest'
# }

# users = [
#     {
#         'id' :0 ,
#         'name' : 'derpy',
#         'role' : roles[0]

#     },
#     {
#         'id' : 1,
#         'name' : 'pinkiepie',
#         'role' : roles[3]
#     },
#     {
#         'id' :2 ,
#         'name' : 'djpon-3',
#         'role' : roles[4]
#     }

# ]

# product = {
#     'id': 1,
#     'title' : 'plush pony starlight glimmer',
#     'discription' : 'best plush pony',
#     'price' : 1000
# }

# print(users)
# print(product)

# user_id = int(input('введите ваше айди'))

# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('введите новое описание продукта')
# else:
#     raise Exception(' у вас недостаточно прав')
# print(product)