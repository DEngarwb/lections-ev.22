# types = (str, int, float, list, tuple)

# for value in types:
#     print(value, True if "__iter__" in dir(value) else False)


# ponyname_list = ['dj-pon3', 'sunset', 'rainbow dash', 'octavia', 'bon bon']

# # for name in ponyname_list:
# #     if name == 'sunset':
# #         continue
# #     print(f"hello {name}!")

# ponyname_list.insert(len(ponyname_list) // 2, 'starlight')

# for name in ponyname_list:
#     if name == 'starlight':
#         break
#     print(f"hi {name}!")


# a = bool(23)
# while a:

#    if input('enter your message: ') in "pony, zebra, hipogriff".split():
#        print('you are banned')
#        break



#input(email) 2) show emails 
#tesst@test.com test@mail.ru Testgmail.com

#CRUD - create read update delete





# DB_EMAILS = []

# while True:
#     print("1) Input Email 2) show db_emails 3) delete email 4) stop 5) change email")
#     choices = int(input('enter chooice'))
#     if choices == 1:
#         email = input('enter email: ')
#         if email.endswith("@gmail.com"):
#             if email in DB_EMAILS:
#                 print('email уже существует')
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         print('invalid email')
#     elif choices == 2:
#         print(DB_EMAILS)
#     elif choices == 3:
#         email = input("enter email : ")
#         if email in DB_EMAILS:
#             # index = DB_EMAILS.index(email)
#             # DB_EMAILS.pop(index)
#             DB_EMAILS.remove(email)
#         else:
#             print(f"{email} не существует!!!")
#     elif choices == 4:
#         break
#     elif choices == 5:
#         old_email = input('enter email: ')
#         if old_email in DB_EMAILS:
#             new_email= input("enter new email: ")
#         if email.endswith("@gmail.com"):
#             DB_EMAILS.remove(old_email)
#             DB_EMAILS.append(new_email)
#     else:
#         ('!!!error!!!')


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

