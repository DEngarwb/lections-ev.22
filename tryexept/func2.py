# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # A, B, C, D, - параметры
#     '''returns sum of all parametrs'''
#     return a+b+c+d

# result = sum_of_args
# print(result)
# print(type(result))
# print(result(5,10,15,20))


#====================================================================================================

#позиционные и именнованные аргументы

# def printParams(a=None,b=None,c=None):
#     print(a, 'is stored in a')
#     print(b,'is stored in param b')
#     print(c, 'is stored in param c')
# printParams(1, c=3,b=5)



# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # A, B, C, D, - параметры
#     '''returns sum of all parametrs'''
#     return a+b+c+d
# print(sum_of_args(1,2,3,4)) #позиционные аргументы(arguments)
# print(sum_of_args(a=5,b=6, d=7, c=6))#именннованные аргументы (keyword arguments)
# print(sum_of_args(5,10,d=15,c=20))


#------------------------------------------------------------------------------------------------------------

#OПЕРАТОР *

# a = [1,2,3]
# b=[4,5,6]
# c=[*a,*b]
# print(c)
# print(*a, end='*\n')


#=========================================================================================================
# *args **kwargs в функциях

# def print_scores(student, *args):
#     print(f'Student name: {student}')
#     # print(args)
#     # print(type(args))
#     for x in args:
#         print(f'оценка',x)

# print_scores('silver stream', 100, 90, 80, 70, 88, 96)


# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         print(f'{pet}:{name}')
# print_pet_names('Fluttershy', dog='vaynona', kat='raritys cat', fish=['nemo',' dory', 'alex'], turtle='tank')

# def get_some_data(a,b, *args, **kwargs):
#     print(' параметры а и b: ', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('аргументы:', args)
#     print('именнованные аргументы: ', kwargs)

# get_some_data(1,2,3,4,5, lang='Python', name="Starlight Glimmer", car='pony')


#==============================================================================================================================


# from pickletools import string1


# def conc_two_string(str1, str2):
#     import random
#     res = random.randint(1,10)
#     return str1 + str2 + str(res)

# result = conc_two_string('hello', 'equestria')
# print(result)

#================================================================================================================================


# def generate_password(name, fam):
#     import random
#     random_num = random.randint(100000,999999)
#     return name + fam + '_' + str(random_num)
# def get_info():
#     name = input('введите имя')
#     fam= input('ведите фамилию')
#     return generate_password(name,fam)
# result = get_info()
# print(result)

#=====================================================================-------------------------------------------------------------------




# def generate_random_string(len_, lang):
#     import string as s
#     import random
#     random_str= ''.join(random.choice(s.ascii_lowercase + s.digits)for i in range(0, len_))
#     return random_str
# print(generate_random_string(15, 'eng'))

#--------------------------------------------------------------------------------------------------------------------------------------------





# def add(num1, num2): return num1+num2
# def subtract(num1, num2): return num1-num2
# def multiply(num1, num2): return num1 * num2
# def divide(num1,num2): 
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return " на 0 делить нельзя"    

# def main():
#     try:
#         num1 = float(input('введите 1 число'))
#         num2 = float(input('введите 2 число'))
#     except ValueError:
#         print('вы ввели неккоректные данные')
#         main()

#     operator = input('введите операцию(+,-,/,*): ')

#     result = None

#     if operator == "+": result = add(num1, num2)
#     elif operator == '-': result= subtract(num1, num2)
#     elif operator == '*': result = multiply(num1, num2)
#     elif operator == '/': result = divide(num1, num2)
#     else:
#         print('вы вели некорекнтый оператор')
#     print(f'результат: {result}')

#     question = input(' хотите продолжить\'?(Yes/NO)')
#     if question.lower() == 'yes' : 
#         main()
#     else:
#         print("спасибо за использование нашего калькулятора! пока")
# main()
