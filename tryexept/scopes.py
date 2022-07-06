#области видимости и пространство имен

# Built-in(встроенная) - print,len,max,int

# Global(глобальная)

# Enclosed(не локальная, nonlocal) 
# local(локальная область видимости)

# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element = 'q'
# print_list([1,2,3,4,5,])
# print(element)

# a =10 #global
# print #built-in
# def hello(): # global
#     a = 'hello equestria'#local
#     print(a, 'local inside at func')
# hello()
# print(a,'global')



# x = 'global'
# print(x) #1 global

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x)#3 local
#     print(x)#2 enclosed
#     local()
#     print(x)#4 enclosed

# enclosed()
# print(x)#5 global



# def func():
#     print(a)

# a = 'str'
# func()


# def func():
#     print(a)
#     a=5
# a='str'
# func()


# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()

# func()

# var = 100 #global variable
# def increment():
#     var = var+1 #Try to update a global variable(using increment -> var+=1)
# increment()

# global -> позволяет менять значение глобальной переменной находсь в локальной области видимости

#nonlocal -> позволяет менять значение локальной переменной находясь в локальной области видимости

# var = 100
# def increment():
#     global var
#     var +=1
# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)

# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num +=1
#         return num
#     return incrementer

# c = counter()
# print(c) #<function counter.<locals>.incrementer at 0x7f74c43e40d0>
# print(c())#1
# print(c())#2
# c = counter()
# print(c())#3

# print(len(dir(__builtins__)))

# print(abs(-15)) # стандартный вызов встроенной функции
# abs =15 #переопределение встроенного имени abs в глобальной области
# del abs
# print(abs(-15))

#===============================================================================================================================================

# a =[[1,2,3],[3,3,5]]
# # fluttershy=sum(a)
# # rainbowdash=sum(b)
# # print(max(rainbowdash,fluttershy))

# res = max([sum(x) for x in a ])
# print(res)

#==================================================================================================================================================

# djpon=[13, 15, 38]
# octavia=[5, 15, 58]
# def compareScores(d,o):
#     score_d= 0
#     score_o=0
#     for i in range(0, len(d)):
#         if d[i] > o[i]:
#             score_d +=1
#         elif o[i] > d[i]:
#             score_o += 1
#         else:
#             pass
#     return{'djpon': score_d, 'octavia': score_o}
# print(compareScores(djpon,octavia))
# print(compareScores([54,20,10], [10,35, 15]))

str_= 'Princess Mi Amore Cadenza'
dcit_={key:str_.count(key) for key in str_}
print(dcit_)