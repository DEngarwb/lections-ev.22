# типы данных в питоне:
# 1. NoneType => ничего пустота
# 2 Boolean -> правда\ложь true/false
# 3 числовые типы данных: 
#       integer(int())-> целое число
#       float() -> числа с плавающей точкой пример(-1.2,100,200)
#       complex() комлплексные числа(3+5i/j)
#       списковые типы данных(
#               list(список)(массив) -> [1,2,3, true,none]
#           )
#           truple( кортеж)-> (1,2,3,false)
#           range(1,3)->range(1,2)
# str() -> строки: 'hello world'
# set()-> множества
# dict -> словарь словарь содержит данные в виде ключа: значения -> {1: "one", 2: "two"}

#********************************************************************************************************
# Mutable(изменяемые типы данных)
#            list()
#            set()
#            dict()
# Immutable(неизменяемые типы данных)
#       NoneType
#       boolen
#       int(), float(), complex()
#       str()
#       range()
#       tuple()
#******************************************************************************************************
# '''стандартный вывод данных'''
# """в пайтоне для вывода данных в терминал используется функция print()"""
# print('pony')
# '''стандартный ввод данных через терминал используется функция input'''
# a = input('ведите число')

# print(a)
# #type() выводит тип данных
# print(type(a))

# b = int(input('ведите число №2: '))
# print(b)
# print(type(b))
# print(a,b,'salat')
# / <- деление
#******************************************************************************************************
# a =[12,14,30]
# print(min(a))
# print(max(a))

# a=2
# b=5
# c=7
# print(pow(a,b))
# print(pow(a,b,c))
# #==
# print(a ** b %c)
#******************************************************************************************************
# divmod(a,b) выводит 2 числа, первое - результат целочисленного деления "a" на 'b', а 2-остаток

# a=5
# b=2
# print(a//b)
#print(12//5)
#print(divmod(5,2))

#abs() - выводит абсолютное значение числа

#print (abs(-5))
#print (abs(5))
# import math
# a=5
# print(math.sqrt(a))

# a='hello'
# print(a)
# a=5
# print(a)


#!!!!!!!!!DZ!!!!!!!!!
#data=10500
#key=90
#res=data^key
#print(res)

# from random import uniform
# # import random
# # random.uniform()

# num1=uniform(0.1,1)
# num2=uniform(9.5,99.5)

# num1=round(num1,2)
# num2=round(num2, 2)

# print (num1,num2)

# res=num1*num2
# print(res)