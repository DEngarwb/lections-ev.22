#методы строк
#dir()-#функция вытаскивает метолы типов данных
#print(dir(str))
#'<соединитель>'.join(<массив который нужно соединить>)-соединяет массив из строк по соединителю в одну строку

#ls=['rainbow dash', 'pinkie pie', 'applejack','rarity']
#joined='!'.join(ls)
#print(joined)

#split(разделитель)-> дробит строку по разделителю и возвращает тип дагнных list.

#text= 'Celestia, Luna, Twilight, Cadance'
#splited=text.split('. ')
#print(splited)
#joined=', '.join(splited)
#print(joined)

#replace(<old value>,<new value>, [count]) меняет в строке old Ha new value, ecли указать count то заменит count pa3

# text= 'ha ha ha ha'
# result=text.replace('ha','pinkamena',)
# print(result)
# print(text)


#strip() -> убирает пробельные символы в начале и конце 
#rstrip()-с конца
#lstrip()-с начала

#text=input('ведите ФИО: ')
#result=text.rstrip()
#print(text.strip())
#print(result)
#print(text)


#count('symbol')-> считает кол-во вхожденний symbols в строку

# text='hello everypony! I\'m from equestria!'
# result = text.count('l')
# print(result)

#index('<value>'[start],[end]) -> выводит индекс-значение value в нашей строке

# text = 'hello equestria! this is octavia!'
# result=text.index('!',16)
# print(result)
# print(len(text))
# print(text.find('i'))
