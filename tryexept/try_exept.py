# обработка исключений
# операторы try...except

# ошибки -> связанные с кодом
SyntaxError
IndentationError
TabError

# исключения -> invalid values

ZeroDivisionError
ArithmeticError
NameError
IndexError
KeyError
ValueError
ImportError
BaseException #прородитель всех ошибок

# try...except

# try:
#     <body try>
# except:
#     <body except>

# num1 = int(input('введите число: '))
# print(num1)
# print('важная строчка кода')

# try:
#     num1 = int(input('введите число: '))
#     print(num1)
# except:
#     print('вы ввели неккоректные данные')
# print('важная строчка кода')

# 1. import sys
# list_=[1,2,3,4,5]
# index = int(input("введите индекс: "))
# try:
#     res = list_[index]
#     print(res)
# except IndexError:
#     import  sys
#     print(f'ooops, we catched{sys.exc_info()[0]} error!')

# 2. Exception as e
# list_=[1,2,3,4,5]
# index = int(input("введите индекс: "))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'ooooops, we catched {e.__class__} error')


# list_=[1,2,3,4,5]

# try:
#     index = int(input("введите индекс: "))
#     res = list_[index]
#     print(res)
# except (IndexError, ValueError):
#     print( "вы ввели неккоректный индекс или символ")

# list_=[1,2,3,4,5]

# try:
#     index = int(input("введите индекс: "))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print( "IndexError")
# except ValueError:
#     print( "ValueError")



# else в try...except
# finally в try...except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body># сработает если в операторе try не случилась ошибка

# finally:
#     <body> # сработает при любом исходе


# try:
#     num1 = int(input('enter: '))
#     num2 = int(input('enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print(" на ноль делить нельзя")
# except ValueError:
#     print("invalid symbols")
# else:
#     print(result) 
# finally:
#     print("код закончился")













