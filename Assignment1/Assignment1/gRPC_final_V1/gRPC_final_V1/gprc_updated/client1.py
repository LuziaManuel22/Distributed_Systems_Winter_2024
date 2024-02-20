# client1.py

import grpc
import shopping_pb2
import shopping_pb2_grpc

def search_item(stub):
    item_name = input("Enter item name to search (leave blank to display all items): ")
    category_input = input("Enter item category to search (ELECTRONICS, FASHION, BOOK, OTHERS, ANY): ")
    valid_categories = ["ELECTRONICS", "FASHION", "BOOK", "OTHERS", "ANY"]
    if category_input.upper() not in valid_categories:
        print("Invalid category. Please enter a valid category (ELECTRONICS, FASHION, BOOK, OTHERS, ANY).")
        return
    category_enum_value = shopping_pb2.Category.Value(category_input.upper()) if category_input.upper() != "ANY" else shopping_pb2.Category.ANY
    request = shopping_pb2.SearchRequest(name=item_name, category=category_enum_value)
    response = stub.SearchItem(request)
    print(f"Search request for Item name: {'<empty>' if not item_name else item_name}, Category: {category_input}.")
    if not response.items:
        print("No items found matching the criteria.")
        return
    for item in response.items:
        category_name = shopping_pb2.Category.Name(item.category)  # Convert enum value back to string name for display
        print(f"\n-\n\nItem ID: {item.id}, Price: ${item.price}, Name: {item.name}, Category: {category_name},\nDescription: {item.description}.\nQuantity Remaining: {item.quantity}\nRating: {item.rating} / 5  |  Seller: {item.seller_address}\n-")

def buy_item(stub):
    item_id = int(input("Enter item ID to buy: "))
    quantity = int(input("Enter quantity to buy: "))
    buyer_address = input("Enter buyer address (ip:port): ")
    request = shopping_pb2.BuyRequest(item_id=item_id, quantity=quantity, buyer_address=buyer_address)
    response = stub.BuyItem(request)
    print(response.message)

def add_to_wishlist(stub):
    item_id = int(input("Enter item ID to add to wishlist: "))
    buyer_address = input("Enter buyer address (ip:port): ")
    request = shopping_pb2.WishListRequest(item_id=item_id, buyer_address=buyer_address)
    response = stub.AddToWishList(request)
    print(response.message)

def rate_item(stub):
    item_id = int(input("Enter item ID to rate: "))
    rating = int(input("Enter rating (1-5): "))
    buyer_address = input("Enter buyer address (ip:port): ")
    request = shopping_pb2.RatingRequest(item_id=item_id, rating=rating, buyer_address=buyer_address)
    response = stub.RateItem(request)
    print(response.message)

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = shopping_pb2_grpc.MarketStub(channel)

    while True:
        print("\nClient 1 Menu:")
        print("1. Search Item")
        print("2. Buy Item")
        print("3. Add to Wishlist")
        print("4. Rate Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_item(stub)
        elif choice == "2":
            buy_item(stub)
        elif choice == "3":
            add_to_wishlist(stub)
        elif choice == "4":
            rate_item(stub)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()