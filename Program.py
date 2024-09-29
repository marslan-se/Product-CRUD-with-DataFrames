from Functions import *

file_name = "product_data.csv"

def menu():
    print("1. Show All Products")
    print("2. Add New Product")
    print("3. Delete a Product")
    print("4. Update Product Rating")
    print("5. Exit")

    option = input("Enter Option to Continue: ")
    return option

while True:
    choice = menu()

    if choice == '1':
        print(list_products(file_name))
    elif choice == '2':
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        desc = input("Enter Product Description: ")
        price = input("Enter Product Price: ")
        image = input("Enter Product Image: ")
        rating = input("Enter Product Rating: ")
        print(add_product(file_name, [pid, name, desc, price, image, rating]))
    elif choice == '3':
        print(list_products(file_name))
        pid = input("Enter Product ID to delete: ")
        print(delete_product(file_name, pid))
    elif choice == '4':
        print(list_products(file_name))
        pid = input("Enter Product ID you want to update: ")
        rating = input("Enter Product Rating: ")
        print(update_product_rating(file_name, pid, rating))
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")