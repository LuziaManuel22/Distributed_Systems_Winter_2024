import datetime
import zmq
import threading
import json
import time

class Group:
    def __init__(self, group_name, message_server_address):
        self.group_name = group_name
        self.message_server_address = message_server_address
        self.context = zmq.Context()
        self.users = {}
        self.messages = []

    def register_with_server(self):
        socket = self.context.socket(zmq.REQ)
        socket.connect(self.message_server_address)
        socket.send_json({"action": "register", "group_name": self.group_name, "address": f"tcp://localhost:{self.group_name}"})
        response = socket.recv_json()
        print(response["status"])

    def start_group(self):
        socket = self.context.socket(zmq.REP)
        socket.bind(f"tcp://*:{self.group_name}")
        print(f"Group {self.group_name} started on tcp://localhost:{self.group_name}.")

        while True:
            message = socket.recv_json()
            action = message['action']
            user_uuid = message['user_uuid']
            threading.Thread(target=self.handle_action, args=(action, message, socket, user_uuid)).start()

    def handle_action(self, action, message, socket, user_uuid):
        if action == 'join':
            self.handle_join(message, socket, user_uuid)
        elif action == 'leave':
            self.handle_leave(message, socket, user_uuid)
        elif action == 'send':
            self.handle_send(message, socket, user_uuid)
        elif action == 'get':
            self.handle_get(message, socket)

    def handle_join(self, message, socket, user_uuid):
        self.users[user_uuid] = time.time()
        socket.send_json({"status": "SUCCESS"})
        print(f"JOIN REQUEST FROM {user_uuid}")

    def handle_leave(self, message, socket, user_uuid):
        if user_uuid in self.users:
            del self.users[user_uuid]
            socket.send_json({"status": "SUCCESS"})
        else:
            socket.send_json({"status": "FAILED"})
        print(f"LEAVE REQUEST FROM {user_uuid}")

    def handle_send(self, message, socket, user_uuid):
        if user_uuid in self.users:
            timestamp = time.time()
            self.messages.append({"timestamp": timestamp, "message": message['message']})
            socket.send_json({"status": "SUCCESS"})
            print(f"MESSAGE SEND FROM {user_uuid}")
        else:
            socket.send_json({"status": "FAILED"})

    def handle_get(self, message, socket):
        user_uuid = message.get('user_uuid')
        timestamp_str = message.get('timestamp', None)
        print(f"MESSAGE REQUEST FROM {user_uuid}")

        if user_uuid not in self.users:
            socket.send_json({"status": "FAILED", "reason": "User not found"})
            return

        try:
            timestamp = datetime.datetime.strptime(timestamp_str, "%H:%M:%S") if timestamp_str else None
        except ValueError:
            socket.send_json({"status": "FAILED", "reason": "Invalid timestamp format"})
            return

        relevant_messages = self.filter_messages(timestamp)
        socket.send_json({"status": "SUCCESS", "messages": relevant_messages})

    def filter_messages(self, timestamp):
        if timestamp:
            return [msg for msg in self.messages if datetime.datetime.strptime(msg['timestamp'], "%H:%M:%S") >= timestamp]
        else:
            return self.messages

if __name__ == "__main__":
    group_port = input("Enter the group port number: ")
    message_server_address = "tcp://localhost:5555" 

    group = Group(group_port, message_server_address)
    group.register_with_server()

    # Start a thread for the group to handle incoming requests
    group_thread = threading.Thread(target=group.start_group)
    group_thread.start()
