
print('⠀⠔⣲⣿⣿⣿⣷⣶⣤⣾⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢀⢾⣿⣿⣿⣿⣿⣻⣽⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣼⣿⡿⠫⡿⠿⣿⣿⣿⣿⢧⠀⠀⢀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⡰⠟⢫⣾⡏⣰⣟⠙⣿⣿⡿⣼⠀⢀⣾⣾⠟⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢸⣿⡇⢿⣯⣶⣿⢟⣵⣿⠀⢬⣏⣯⣾⠟⠁⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀\n⠀⠈⠿⣿⣿⣾⣿⣯⡥⣽⣿⣿⠀⡿⣭⢹⣥⡤⠀⣠⣶⣿⣿⣿⣿⣿⣷⡄⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⢱⢟⣿⠇⣸⡟⣕⢫⣷⣤⠾⠿⣿⣿⣿⣿⣿⣿⣿⡻⡀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⢠⢸⡏⣾⣿⣥⡷⠁⠀⢿⠀⠀⠈⢿⣿⣿⣿⣿⣿⣧⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠹⣿⣞⢸⣿⣿⣿⣇⢠⣶⡟⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠛⠻⣿⣸⣿⣥⡀⠀⠀⠈⣿⣿⣿⣿⣿⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⠀⠀⢹⣿⣿⣿⣧⠀⠀⠀⢹⣿⣿⣿⡟⢧⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠀⠀⠈⣿⣿⣿⣿⡄⠀⠀⠘⣿⣿⣿⣧⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡟⠀⠀⣸⣿⣿⣿⣿⡇⠀⠀⠀⠹⠈⠿⣿⢷⣄⡀\n⠀⠀⠀⠀⠀⠀⠀⠿⢿⣿⠿⠃⠀⠀⠛⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀')
#встроенные функции
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() etc.

# map()
# filter()
# lambda
# enumerate()

# Аноонимные функции - lambda λ (такие же функции только без названия)
# lambda функции могут принимать сколько угодно значений, но всегда возвращают только одно выражение

# def sum_args(a,b):
#     result = a+b
#     return result

# def sum_args1(a,b): return a+b

# print(sum_args(1,2))
# print(sum_args1(1,2))

# sum_arg = lambda a,b: a + b
# print(sum_arg(1,2))



# x  = lambda a,b,c: a+b+c
# print(5+6+7)

# def myFunc(n):
#     return lambda a: a*n
# mydoubler = myFunc(2)
# mytripler = myFunc(3)
# print(mydoubler(11))
# print(mydoubler(22))
# print(mytripler(11))
# print(mytripler(22))

# ls = ['def','Pony','selestia', '', ' ']
# new_list = sorted(ls, key = len)
# print(new_list)


#___________________________________________________________________________________________________________________________________________________________




# map(function, Iterable) -> применяет функцию к каждому элементу последовательности и возвращает mapobject(итератор) с результатами

# с  помощью map можно выполнять преобразования элементов(перевести все строки в верхний регистр)


# list_of_words = ['one','two','three','dict', ]

# result = list(map(str.upper, list_of_words))
# result2 = list(map(len, list_of_words))
# print(result)
# print(result2)

# ls = ['1','2','3','4',]
# result = list(map(int,ls))
# print(result)

# names = ['Derpy','Rainbowdash', 'Rarity','Bonbon','Lyra']
# result = list(map(lambda x: f'hello mr/mrs {x}', names))

# print(result)

# nums = [1,2,3,4,5]
# mums2= [100,200,300,400,500]

# result = list(map(lambda x,y: x*y, nums, mums2))
# print(result)

# dict_ = {1:2,3:4,5:6}
# result = dict(map(lambda items:(items[0],str(items[1])), dict_.items()))
# print(result)


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))






# filter (function, Iterable) - применяет  ко всем элементам Iterable функцию которую мы передаем и возвращает filterobject(итератор) с теми объектами для которых функция вернула True.


# list_of_str = ['one','two','list','','100', '1','50', "Djpon3"]
# result = filter(str.isdigit, list_of_str)
# print(list(result))

# ls = [10,11,102,213,314,515]
# result = list(filter(lambda x: x %2 !=0, ls))
# print(result)

# list_of_words = ['Pony','one','two','list','makers','ev.22','kot']
# result=list(filter(lambda x: len(x) >=4, list_of_words))
# print(result)

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""''''''''''''''''''''''''''''''""""""""""""""""""""""""""""''''''"""""'''''""""''''""""''''"""''''"""''''""""''''"""''''""""''''""""''''''''
#enumerate(iturable) -
# ls = ['str1', 'str2','str3']
# # i=0 
# # for x in ls:
# #     print(f'element: {x}, index {i}')
# #     i+=1

# for i, x in enumerate(ls):
#     print(f'element:{x}, index {i}')

# new_list = list(enumerate(ls))
# print(new_list)

#==+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# zip(interables) - соединяет каждый элемент интерируемых элементов между собой в тип данных tupleи возвращает 

# list1= [1,2,3]
# list2 = [100,200,300]
# result = list(zip(list1,list2))
# print(result)

# a = [1,2]
# b = [10,20,30,40]
# c = [100,200,300]
# result = list(zip(a,b,c))
# print(result)

#zip для создания словарей
# d_keys = ['hostname','location','vendor', 'model','IOS',"ip"]
# d_values = ['london_r1', '21 New blobe', 'cisco', '4451', '15.4', '10.255.0.1']

# dict_r1 = dict(zip(d_keys,d_values))
# print(dict_r1)

# d_keys = ['hostname','location','vendor', 'model','IOS',"ip"]
# data = {
#     'r1': ['london_r1', '21 New blobe', 'cisco', '4451', '15.4', '10.255.0.1'],
#     'r2' : ['london_r2', '21 New blobe', 'cisco', '4451', '15.4', '10.255.0.1'],
#     'sw1' : ['equestria', '21 rainbowdash', 'derpy', '1138','13.04','10.244.0.2']
# }

# pony_data={}
# for key in data.keys(): 
#     pony_data[key] = dict(zip(d_keys, data[key]))
# print(pony_data)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# all и any
# all -> возвращвает True, если все элементы обьекта истина(или он пустой)

# ls = [[1,2],1,'stroka',True]
# print(all(ls))

# ip= '10.255.0.0.1'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает True,если хотя бы один элемент истинный

# ls = [0,0,'',False,1]
# print(any(ls))

# def ignore_command(command):
#     '''
#     функция проверяет есть ли в  команде слово из списка ignore. True-если есть, False-нет
#     '''
#     ignore=['rm -rf','alias', 'reset', ]
#     for word in ignore:
#         if word in command:
#             return True
#     return False
# # print(ignore_command('sudo root user'))
# command = 'rm -rf'
# if ignore_command(command):
#     raise Exception('invalid command')
# print('vse ok')

# ignore=['rm -rf','alias', 'reset', ]
# command = 'rm -rf'
# if any([word in command for word in ignore]):
#     raise Exception('invalid command')
# print('vse norm')
import os
from random import choices
from string import ascii_letters, digits
from itertools import repeat

q_pass = int(input('введите количество паролей: '))

print({
    f(choices(ascii_letters, k=10), choices(digits, k=5))
    for f in repeat(lambda x, y:''.join(set((x+y))) ,q_pass)
    })