from typing import List, Dict
from time import sleep

from Models.product import Product
from utils.helper import format_float_str_coin

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==============================')
    print('========== Welcome ===========')
    print('=========Pedro Shop===========')
    print('==============================')

    print('Select an option below: ')
    print('1 - Register Product')
    print('2 - List Product')
    print('3 - Buy Product')
    print('4 - View Shopping Cart')
    print('5 - Close Order')
    print('6 - Exit System')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_shopping_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Check back often!!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()


def register_product() -> None:
    print('Product Registration')
    print('===================')

    name: str = input('Inform the product name: ')
    price: float = float(input('Inform the price of the product: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product {product.name} has been successfully registered!')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Product Listing')
        print('--------------------')
        for product in products:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print('There are no registered products yet!')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Enter the code of the product you want to add to the cart:')
        print('-------------------------------------------------------------')
        print('-----------------Available Products------------------------')
        for product in products:
            print(product)
            print('---------------------------------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if Product:
            if len(cart) > 0:
                have_in_cart: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'The product {product.name} now have {quant +1} units in the cart.')
                        have_in_cart = True
                        sleep(2)
                        menu()
                if not have_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product has been added to the cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} has been added to the cart')
                sleep(2)
                menu()
        else:
            print(f'The product with code {code} was not found.')
            sleep(2)
            menu()
    else:
        print('There are no products to sell yet.')
    sleep(2)
    menu()


def view_shopping_cart() -> None:
    if len(cart) > 0:
        print('Cart products:')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('-----------------------')
                sleep(2)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Cart Products:')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
                print('------------------')
        print(f'Your invoice is {format_float_str_coin(total_value)}')
        print('Check back often!')
        cart.clear()
        sleep(5)
    else:
        print('There are no products in the cart yet!')
    sleep(2)
    menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()