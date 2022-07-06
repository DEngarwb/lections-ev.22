#list(список, массив) - изменяемый последовательный тип данных, который из себя представляет коллекцию каких либо объектов.

#pony_list = [1, 'string', False, None, [1,2,3]]
#print(pony_list)
#print(type(pony_list))

#1. -> list(<iterable>)
# pony_list = list('hello equestria!')
# print(pony_list)

# princcess=['selestia', 'luna', 'cadance', 'twilight']
# print(princcess)
# print(type(princcess))
# pony_list = list()
# print(pony_list)
# print(type(pony_list))

#2. range() -> возвращает последовательность элементов(числа)

# rainbowdash = list(range(1, 100, 2))
# print(rainbowdash)

#3. -> []


# pony_list = [1,23,4,45,5]
# print(pony_list)
# print(type(pony_list))



#print(dir(list))
#append(element) - добавляет элемент в конец списка

# djpo3=[1,2,3]
# print(djpo3)
# djpo3.append(5)
# djpo3.append([1,2,3])
# print(djpo3)



#extend(element[iturable]) -> расширяет список добовляя element в конец
# pony=[1,2,3]
# pony.extend([1,2,3])
# print(pony)

#insert(<index>,<element>) -> добавляет элемент по указанному индексу index

# ponylist = ['string', 2, 3, False]
# ponylist.insert(1,[1,2,3, None])
# ponylist.insert(2,1)
# print(ponylist)
# print(ponylist[5])
# print(ponylist[1][3])
# print(ponylist[2:5])
# print(len(ponylist))


# index(element, [start], [end]) - возвращает индекс элемента

# ls = [1,2,33,3,4,5,5,7,2, 'pony']
# print(ls.index(5, 6))
# if 'pony' in ls: 
#     print(f"'pony' is in list: {ls.index('pony')}")
#     if 'pony' in ls:
#         print("'pony'is in list:", ls.index('hello'))

#count(element) -> возвращает кол-во вхождений element в списке
# ls = [1,2,3,4,5,5,5,5,5,1]
# result = ls.count(5)
# print(result)

#remove(element)- удаляет element , но если такого нет то выводит ошибку

# pop([index]) - удаляет и возвращает элемент по index, но если index не указан то удаляет последний элемент



# ponylist = [5, 1 , 2 ,3 ,4 ,5]
# # ponylist.remove(5)
# # ponylist.remove(5)
# # ponylist.remove(5)
# deleted = ponylist.pop(0)
# d = ponylist.remove(4)
# print(ponylist)
# print(deleted)
# print(d)

# sort([reverse=True/False], [key=<>]) -> сортирует список. Если в аргументах передан reverse=True то список будет отсортирован в убывающем порядке

# ls = [5, 0, -2, -101, 102, 23, 1]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls = ['hello', 'octavia', 'djpon3', 'starlight']
# ls.sort(reverse=True, key=len)
# print(ls)


# ls = [1, 'h', 3]
# ls[1] = 2
# print(ls)
# del ls[-1]
# print ls

