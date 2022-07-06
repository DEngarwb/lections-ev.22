# javascript object notation - JSON(единый формат зранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть) 

# <filename>.json

# {
#     "id":1,
#     "author": "celestia",
#     'posts' : []
# } # JSON

# задача научиться переводить JSON в python dict


#!!!

# JS object =={}
# PY dict =={}
# JSON = {}

# Процессы сериализации данных и их Дисериализация

# Сериализация(запись данных JSON) - перевод Python Dict в JSON формат(либо сохранить все в файл, либо сохраняем как текстовые данные)

# dump - этот метод записывает объект в python в  файл формате json
# dumps - метод записывает объект в python в строку формате json

# Десериализация(Чтения данных из JSON) - это процесс перевода из JSON в python dictionary 

# load - метод который считывает файл в формате JSON и переводит в объект python 
# loads - метод который считывает текст формате JSON и переводит в объект python 



######################################################################################################################################################################################################
# Дисериализация

# from urllib.request import urlopen
# import json
# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# generate_to_dict=json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))

# import json

# with open('downApi.json','r') as file:
#     data = file.read()
#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#процесс сериализации
import json

# dict_ = {
#     'name' : 'twilight',
#     'last_name': 'sparkle',
#     'status': True,
#     'wife' : None,
#     'children':False,
# }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file)


dict_ = {
    'name' : 'twilight',
    'last_name': 'sparkle',
    'status': True,
    'wife' : None,
    'children':False,
}
string = json.dumps(dict_)
print(string)
print(type(string))