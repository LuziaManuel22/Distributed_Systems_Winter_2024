import grpc
from concurrent import futures
import time
import shopping_pb2
import shopping_pb2_grpc

class Market(shopping_pb2_grpc.MarketServicer):
    def __init__(self):
        self.sellers = {}  # Dictionary to store registered sellers
        self.items = []    # List to store available items
        self.wishlist = {} # Dictionary to store buyers' wishlists

    def RegisterSeller(self, request, context):
        if request.address in self.sellers:
            return shopping_pb2.Response(message="FAILED: Seller already registered")
        self.sellers[request.address] = request.uuid
        print(f"Seller join request from {request.address}, uuid = {request.uuid}")
        return shopping_pb2.Response(message="SUCCESS")

    def SellItem(self, request, context):
        if request.seller_address not in self.sellers:
            return shopping_pb2.Response(message="FAILED: Seller not registered")
        item_id = len(self.items) + 1
        item = shopping_pb2.Item(
            id=item_id,
            name=request.name,
            category=request.category,
            quantity=request.quantity,
            description=request.description,
            price=request.price,
            seller_address=request.seller_address,
            rating=0.0
        )
        self.items.append(item)
        print(f"Sell Item request from {request.seller_address}, Item ID: {item_id}")
        return shopping_pb2.Response(message=f"SUCCESS: Item sold with ID {item_id}")

    def UpdateItem(self, request, context):
        if request.seller_address not in self.sellers:
            return shopping_pb2.Response(message="FAILED: Seller not registered")
        
        updated = False
        for item in self.items:
            if item.id == request.id:
                item.price = request.price
                item.quantity = request.quantity
                updated = True
                print(f"Update Item {request.id} request from {request.seller_address}")
                self.NotifyClient(item.id, request.price, request.quantity)
                break
        
        if updated:
            return shopping_pb2.Response(message="SUCCESS")
        else:
            return shopping_pb2.Response(message="FAILED: Item not found")

    def DeleteItem(self, request, context):
        if request.seller_address not in self.sellers:
            return shopping_pb2.Response(message="FAILED: Seller not registered")
        for item in self.items:
            if item.id == request.id:
                self.items.remove(item)
                print(f"Deleted Item ID: {request.id}")
                return shopping_pb2.Response(message="SUCCESS")
        return shopping_pb2.Response(message="FAILED: Item not found")

    def DisplaySellerItems(self, request, context):
        if request.address not in self.sellers:
            return shopping_pb2.ItemList(items=[])
        seller_items = [item for item in self.items if item.seller_address == request.address]
        print(f"Display Items request from {request.address}")
        return shopping_pb2.ItemList(items=seller_items)

    def SearchItem(self, request, context):
        filtered_items = [
            item for item in self.items 
            if (request.name == "" or item.name == request.name) 
            and (request.category == shopping_pb2.Category.ANY or item.category == request.category)
        ]
        
        category_name = shopping_pb2.Category.Name(request.category) if request.category != shopping_pb2.Category.ANY else "ANY"
        print(f"Search request for Item name: {request.name}, Category: {category_name}")
        return shopping_pb2.ItemList(items=filtered_items)

    def BuyItem(self, request, context):
        if request.item_id not in [item.id for item in self.items] or request.quantity > [item for item in self.items if item.id == request.item_id][0].quantity:
            return shopping_pb2.Response(message="FAILED: Item not found or not enough stock available")
        item = [item for item in self.items if item.id == request.item_id][0]
        item.quantity -= request.quantity
        print(f"Buy request {request.quantity} of item {item.id}, from {request.buyer_address}")
        return shopping_pb2.Response(message="SUCCESS")

    def AddToWishList(self, request, context):
        if request.buyer_address not in self.wishlist:
            self.wishlist[request.buyer_address] = set()
        self.wishlist[request.buyer_address].add(request.item_id)
        print(f"Wishlist request for item {request.item_id}, from {request.buyer_address}")
        return shopping_pb2.Response(message="SUCCESS")

    def RateItem(self, request, context):
        if request.item_id not in [item.id for item in self.items] or request.rating < 1 or request.rating > 5:
            return shopping_pb2.Response(message="FAILED: Item not found or invalid rating")
        print(f"{request.buyer_address} rated item {request.item_id} with {request.rating} stars.")
        return shopping_pb2.Response(message="SUCCESS")

    def NotifyClient(self, item_id, updated_price, updated_quantity):
        notifications_sent = 0
        for buyer_address, wishlist_items in self.wishlist.items():
            if item_id in wishlist_items:
                print(f"Notification to {buyer_address}: Item {item_id} has been updated. New price: {updated_price}, New quantity: {updated_quantity}.")
                notifications_sent += 1
        if notifications_sent == 0:
            print("No buyers to notify for the item update.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shopping_pb2_grpc.add_MarketServicer_to_server(Market(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Market server started...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
