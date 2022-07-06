from itertools import product
import json
import random

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)
def list_of_products():
    data = get_data()
    return data
def retrieve_product():
    data = get_data()
    id = int(input('введите айди продукта '))
    print('впишите цифру')
    product = list(filter(lambda x: x['id']==id, data))
    return product[0]

def get_id():
    with open('id.txt','r') as file:
      id = int(file.read())
        # print(type(id))
      id +=1

    with open('id.txt','w') as file:
        file.write(str(id))
    return id

def create_product():
    data=get_data()
    product = {
        'id':get_id(),
        'title':float(input("введите цену продукта")),
        'descriptuon': input('введите описание'),
        }
    data.append(product)
    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)
    result = {'msg':'created', 'product': product}
    return result

def update_product():
    data = get_data()
    flag = False
    id = int(input("введите айди продукта "))
    product = list(filter(lambda x : x['id'] == id, data))

    if not product:
        return{'msg': 'не правильное айди, продукта нет'}
    index = data.index(product[0])
    choice = input('что изменить? title-1, price-2, description-3: ')
    if choice == '1':
        data[index]['title'] = input('введите новое наззвание ')
        flag = True
    elif choice=='2':
        data[index]['price'] = float(input('введите новую цену'))
        flag = True
    elif choice == '3':
        data[index]['descriptuon'] = input('введите новое описание')
        flag = True
    else:
        print('вы ввели неправильный выбор')
    with open(FILE_PATH, 'w')as file:
        json.dump(data, file)
    
    if flag:
        return {'msg':'updated','product': data[index]}
    else:
        return{'msg': 'Not Updated'}

def delete_product():
    data = get_data()
    id = int(input('введите айди продукта'))
    product = list(filter(lambda x: x['id']==id,data))

    if not product:
        return{'msg':'Invalid id! product does not exist'}
    index = data.index(product[0])
    deleted = data.pop(index)
    json.dump(data, open(FILE_PATH, 'w'))
    return{'msg':'deleted', "product": deleted}

