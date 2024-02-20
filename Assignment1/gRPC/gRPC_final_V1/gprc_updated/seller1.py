# seller1.py

import grpc
import uuid
import shopping_pb2
import shopping_pb2_grpc

def register_seller(stub):
    address = input("Enter seller address (ip:port): ")
    # Generate UUID for seller
    seller_uuid = str(uuid.uuid1())  # Correção: chamar uuid.uuid1() para gerar o UUID
    request = shopping_pb2.SellerInfo(address=address, uuid=seller_uuid)
    response = stub.RegisterSeller(request)
    print(response.message)

def sell_item(stub):
    name = input("Enter item name: ")
    category_str = input("Enter item category (ELECTRONICS, FASHION, BOOK, etc.): ").upper()
    category_map = {
        "ELECTRONICS": shopping_pb2.ELECTRONICS,
        "FASHION": shopping_pb2.FASHION,
        "BOOK": shopping_pb2.BOOK,
        "OTHERS": shopping_pb2.OTHERS
    }
    category = category_map.get(category_str)
    if category is None:
        print(f"Invalid category. Valid categories are: {list(category_map.keys())}")
        return

    quantity = int(input("Enter item quantity: "))
    description = input("Enter item description: ")
    price = float(input("Enter item price: "))
    seller_address = input("Enter seller address (ip:port): ")
    seller_uuid = input("Enter seller UUID: ")
    request = shopping_pb2.ItemInfo(
        name=name,
        category=category,  
        quantity=quantity,
        description=description,
        price=price,
        seller_address=seller_address,
        seller_uuid=seller_uuid
    )
    response = stub.SellItem(request)
    print(response.message)


def update_item(stub):
    item_id = int(input("Enter item ID to update: "))
    price = float(input("Enter new price: "))
    quantity = int(input("Enter new quantity: "))
    seller_address = input("Enter seller address (ip:port): ")
    seller_uuid = input("Enter seller UUID: ")
    request = shopping_pb2.ItemInfo(id=item_id, price=price, quantity=quantity, seller_address=seller_address, seller_uuid=seller_uuid)
    response = stub.UpdateItem(request)
    print(response.message)

def delete_item(stub):
    item_id = int(input("Enter item ID to delete: "))
    seller_address = input("Enter seller address (ip:port): ")
    seller_uuid = input("Enter seller UUID: ")
    request = shopping_pb2.ItemID(id=item_id, seller_address=seller_address)
    response = stub.DeleteItem(request)
    print(response.message)

def display_items(stub):
    address = input("Enter seller address (ip:port): ")
    # You can optionally provide UUID as well if required
    request = shopping_pb2.SellerInfo(address=address)
    response = stub.DisplaySellerItems(request)
    for item in response.items:
        print(f"Item ID: {item.id}, Price: ${item.price}, Name: {item.name}, Category: {item.category}, Description: {item.description}, Quantity Remaining: {item.quantity}, Seller: {item.seller_address}, Rating: {item.rating}")

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = shopping_pb2_grpc.MarketStub(channel)

    while True:
        print("\nSeller 1 Menu:")
        print("1. Register as Seller")
        print("2. Sell Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Display Items")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_seller(stub)
        elif choice == "2":
            sell_item(stub)
        elif choice == "3":
            update_item(stub)
        elif choice == "4":
            delete_item(stub)
        elif choice == "5":
            display_items(stub)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
