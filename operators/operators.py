#операторы сравнения
#условные операторы
#логические операторы

#операторы сравнения:
#<,>, ==(равно), <=, >=, !=(не равно)
#trixie = 16
#starlight =15
# daringdo='Hello'
# print(ord('H'))
# kabaleron='Everypony'
# print(ord('E'))
# result = daringdo > kabaleron
# print(result)
#print(chr(1080))

#bool -- True(1) or False(0)


#условные операторы 
# if
#elif
#else

# if<condition>: 
#     ecли B if приходит True
#     <body if>
# elif (else if) <condition>:
#     <body>
# else:
#     <body>

# derpy = input('enter ponyname: ')

# if derpy == 'derpy':
#     print('derpy hooves')
# elif derpy == 'djpon-3':
#     print('vinyl scratch')
# else:
#     (print('rainbow dash better'))


# print('пони закончились')

#sign up

# pony = input('какого пони вы любите?: ')
# applejack = input('какая у неёё кьютимарка ')
# rainbowdash = input('напишите кьютимарку ещё раз ')

# if applejack != rainbowdash:
#     raise Exception('не совпадает имя пони')
# else:
#     print('ураа! вы отлично знаете пони-мир')

# age = input('напишите свой возраст ')
# #print(type(age))
# if age.isdigit():
#      age = int(age)
# else:
#      print('введите корректные данные')
#      raise Exception('value error!')
# if age < 18:
#     print(f'вам нельзя смотерть my little pony, посмотрите через {18-age} лет/годов')
# else:
#     print('вам можно смотерть my little pony')

#логические операторы
# 1 and -> логическое и
# 2 or -> логическое или
# 3 not -> логическое отрицание

# pony_age=20
# eg_age=18
# result= (pony_age == 20) and (eg_age == 18)
# print(result)
# result = pony_age > 18 or eg_age == 20
# print(result)

# result = not pony_age == 20
# print(result)

# is_user_google_user = True
# is_user_equestria_user = True
# is_user_age_greater_21=False
# user_accounts_bits = 8000

# if (is_user_google_user and is_user_equestria_user) and (is_user_age_greater_21 or user_accounts_bits > 5000):
#     print('вы можете войти')
# else:
#     print("вы не можете")
