import time
import zmq
import uuid
import zmq
import uuid
import json

class User:
    def __init__(self, message_server_address="tcp://localhost:5555"):
        self.message_server_address = message_server_address
        self.context = zmq.Context()
        self.uuid = str(uuid.uuid4())
        self.groups = {}

    def get_group_list(self):
        socket = self.context.socket(zmq.REQ)
        socket.connect(self.message_server_address)
        socket.send_json({"action": "list"})
        response = socket.recv_json()
        if response['status'] == "SUCCESS":
            self.groups = response['groups']
            print("Available groups:")
            for name, address in self.groups.items():
                print(f"{name} - {address}")
        else:
            print("Failed to get group list.")

    def join_group(self, group_name):
        if group_name in self.groups:
            group_address = self.groups[group_name]
            socket = self.context.socket(zmq.REQ)
            socket.connect(group_address)
            socket.send_json({"action": "join", "user_uuid": self.uuid})
            response = socket.recv_json()
            if response['status'] == "SUCCESS":
                print("SUCCESS joining group")
            else:
                print("Failed to join group.")
        else:
            print("Group not found.")

    def leave_group(self, group_name):
        if group_name in self.groups:
            group_address = self.groups[group_name]
            socket = self.context.socket(zmq.REQ)
            socket.connect(group_address)
            socket.send_json({"action": "leave", "user_uuid": self.uuid})
            response = socket.recv_json()
            if response['status'] == "SUCCESS":
                print("SUCCESS leaving group")
            else:
                print("Failed to leave group.")
        else:
            print("Group not found.")

    def send_message(self, group_name, message):
        if group_name in self.groups:
            group_address = self.groups[group_name]
            socket = self.context.socket(zmq.REQ)
            socket.connect(group_address)
            socket.send_json({"action": "send", "user_uuid": self.uuid, "message": message})
            response = socket.recv_json()
            if response['status'] == "SUCCESS":
                print("SUCCESS sending message")
            else:
                print("FAILED to send message.")
        else:
            print("Group not found.")

    def get_messages(self, group_name):
     if group_name not in self.groups:
        print("Group not found.")
        return

     group_address = self.groups[group_name]
     timestamp = input("Enter the timestamp to get messages from (HH:MM:SS, leave blank for all messages): ")

     socket = self.context.socket(zmq.REQ)
     socket.connect(group_address)
     request_data = {"action": "get", "user_uuid": self.uuid, "timestamp": timestamp if timestamp else ""}

     socket.send_json(request_data)
     response = socket.recv_json()

     print(f"MESSAGE REQUEST FROM {self.uuid}")
     if response['status'] == "SUCCESS":
        for msg in response['messages']:
            # Format the timestamp as HH:MM:SS
            formatted_timestamp = time.strftime('%H:%M:%S', time.localtime(msg['timestamp']))
            print(f"{formatted_timestamp} - {msg['message']}")
     else:
        print(f"Failed to get messages: {response.get('reason', '')}")

def user_menu():
    user = User() 

    while True:
        print("\nUser Menu:")
        print("1. Get Group List")
        print("2. Join Group")
        print("3. Leave Group")
        print("4. Send Message")
        print("5. Get Messages")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.get_group_list()
        elif choice == "2":
            group_name = input("Enter the group port to join: ")
            user.join_group(group_name)
        elif choice == "3":
            group_name = input("Enter the group port to leave: ")
            user.leave_group(group_name)
        elif choice == "4":
            group_name = input("Enter the group port to send a message: ")
            message = input("Enter the message: ")
            user.send_message(group_name, message)
        elif choice == "5":
            group_name = input("Enter the group port to get messages from: ")
            user.get_messages(group_name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_menu()