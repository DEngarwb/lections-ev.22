print('⠀⠔⣲⣿⣿⣿⣷⣶⣤⣾⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⢀⢾⣿⣿⣿⣿⣿⣻⣽⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣼⣿⡿⠫⡿⠿⣿⣿⣿⣿⢧⠀⠀⢀⠀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⡰⠟⢫⣾⡏⣰⣟⠙⣿⣿⡿⣼⠀⢀⣾⣾⠟⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢸⣿⡇⢿⣯⣶⣿⢟⣵⣿⠀⢬⣏⣯⣾⠟⠁⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀\n⠀⠈⠿⣿⣿⣾⣿⣯⡥⣽⣿⣿⠀⡿⣭⢹⣥⡤⠀⣠⣶⣿⣿⣿⣿⣿⣷⡄⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⢱⢟⣿⠇⣸⡟⣕⢫⣷⣤⠾⠿⣿⣿⣿⣿⣿⣿⣿⡻⡀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⢠⢸⡏⣾⣿⣥⡷⠁⠀⢿⠀⠀⠈⢿⣿⣿⣿⣿⣿⣧⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠹⣿⣞⢸⣿⣿⣿⣇⢠⣶⡟⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠛⠻⣿⣸⣿⣥⡀⠀⠀⠈⣿⣿⣿⣿⣿⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⠀⠀⢹⣿⣿⣿⣧⠀⠀⠀⢹⣿⣿⣿⡟⢧⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠀⠀⠈⣿⣿⣿⣿⡄⠀⠀⠘⣿⣿⣿⣧⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡟⠀⠀⣸⣿⣿⣿⣿⡇⠀⠀⠀⠹⠈⠿⣿⢷⣄⡀\n⠀⠀⠀⠀⠀⠀⠀⠿⢿⣿⠿⠃⠀⠀⠛⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀')
#работа с файлами
# каретка - указатель


# open(<путь дo нашего файла>)
# file = open('/home/leon/Desktop/makers/unit.22/files.py') #абсолютный
# file = open('files.py') # относительный путь
# print(file)

#режимы для работы с файлами
# 1. r/r+(read)
# 2. w/w+(write)
# 3. a/a+(append)
# t, b, x

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))


# file = open('/home/leon/Desktop/makers/unit.22/text.txt')
# data = file.readlines()
# print(data)
# file.close()

# file = open('text.txt','w')
# file.write('Hello equestria! \n my name is twilight sparkle!\n princess!')


# file = open('text.txt','a')
# file.write('\nTwilight Sparkle Princess of Friendship')
# file.close()

# file=open('text1.txt')
# file.close()

# Контекст менеджер

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)

# print(file) #ошибка

#write writelines

# ls = ['Hello equestria', 'My name is celestia', 'I\'m 1000 years old']

# with open('text.txt', 'w') as f:
#     f.writelines(line +'\n'for line in ls)

# file.tell() --> возвращает индекс, где находится курсор(указатель)

# file.seek(<int>) ->перемещает каретку(указатель) на указанный int(index)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44


# from PIL import Image
# import pytesseract
# import re
# def get_imei_codes(list_images):
#     list_of_imei=[]
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s.\d+',string))
#         print(list_of_imei)
#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')
# list_images=['imei.jpg']
# get_imei_codes(list_images)

