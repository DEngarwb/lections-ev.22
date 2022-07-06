from views import list_of_products,retrieve_product,create_product,update_product,delete_product

def main():
    print('привет тебе доступны следующие функции: \n\tLIST-1\n\tRetrive2\n\tCreate3\n\tupdate-4\n\tDelete5')
choice = input('введите действие')
if choice =='1':
    print(list_of_products())
elif choice == '2':
    print(retrieve_product())
elif choice == '3':
    print(create_product())
elif choice == '4':
    print(update_product())
elif choice == '5':
    print(delete_product())
else:
    print('invalid choice!')
    main()
ask = input('хотите продолжить? (yes/no)')
if ask.lower() =='yes':
    main()
else:
    print('poka! poka!')
