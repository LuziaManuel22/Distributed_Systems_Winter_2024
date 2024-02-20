
# Using gRPC to implement an Online Shopping Platform

## I. Project Details

The project consists of a shopping platform composed of three main components: Market, Seller, and Buyer. Each of these components resides on a different virtual machine and communicates with each other through gRPC. This Platform is intended to facilitate product purchase and sale transactions, in a similar way to the infrastructure established by large companies such as Amazon. To enable this efficient interaction between the platform's various components, gRPC (gRPC Remote Procedure Calls) is used, a remote procedure calling system developed by Google.

gRPC plays a crucial role in communication between the different components of the platform, allowing the centralized marketplace, sellers, and buyers to interact in an agile and reliable manner. Through remote procedures defined in protobuf files, clients can send requests to the central server and receive corresponding responses, all in a transparent and scalable way.

## II. Project Files

- **shopping.proto**: This file defines the gRPC services and messages used in communication between the different components of the platform. It specifies the RPC methods offered by the market, such as registering sellers, adding items for sale, searching for items, etc.

- **market.py**: This file implements the market server, which offers the services defined in the shopping.proto file. It maintains a list of registered sellers, items for sale, and buyer wishes. The server runs on a specific port and manages all interactions between sellers and buyers.

- **seller1.py and seller2.py**: These files implement clients for the sellers. They interact with the market server to perform operations related to item sales. They allow sellers to register, add new items, update information on existing items, delete items, and view their items for sale.

- **client1.py and client2.py**: These files implement clients for the buyers. They interact with the market server to perform operations related to item purchase. They allow buyers to search for items, buy items, add items to their wish list, and rate purchased items.

## III. How to Run

To execute the project, follow the steps below:

Make sure you have - **Python** installed on your system.
Install project dependencies by running - **pip install grpcio grpcio-tools**.
Run the market server using the command - **python3 market.py**.
Run the clients for sellers and buyers as needed, using the commands - **python3 seller1.py, python3 seller2.py, python3 client1.py, and python3 client2.py**.

## IV. Contribution

Contributions to this project are welcome. If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request

