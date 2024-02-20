import zmq
import threading

class MessageServer:
    def __init__(self, port=5555):
        self.port = port
        self.context = zmq.Context()
        self.groups = {}

    def start_server(self):
        socket = self.context.socket(zmq.REP)
        socket.bind(f"tcp://*:{self.port}")
        print(f"Message server started on port {self.port}.")

        while True:
            message = socket.recv_json()
            action = message['action']

            if action == 'register':
                self.register_group(message, socket)
            elif action == 'list':
                self.list_groups(socket)

    def register_group(self, message, socket):
        group_name = message['group_name']
        group_address = message['address']
        self.groups[group_name] = group_address
        response = {"status": "SUCCESS"}
        socket.send_json(response)
        print(f"JOIN REQUEST FROM {group_address} [IP: {group_name}]")

    def list_groups(self, socket):
     response = {
        "status": "SUCCESS",
        "groups": self.groups  
    }
     socket.send_json(response)
     print(f"GROUP LIST REQUEST")


if __name__ == "__main__":
    server = MessageServer()
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
