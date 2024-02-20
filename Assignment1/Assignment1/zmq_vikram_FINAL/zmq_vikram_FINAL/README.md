
# Project Name
GROUP MESSAGING APPLICATION

## Overview

This project provides a comprehensive messaging platform that supports user management, direct messaging, and group interactions. It consists of several key components:

- **User Management**: Implemented in `user1.py` and `user2.py`, these modules handle user profiles, allows users to join a group, send message ,leave a group ,get all the messages from group.

- **Messaging Server**: Defined in `message_server.py`, this core component manages message transmission, storage, and retrieval between users.

- **Group Features**: The `group.py` module facilitates group creation, membership management, and group-based messaging.

## Installation

### Python 3 Installation on Linux/Ubuntu

1. Update the package index:
   ```
   sudo apt update
   ```
2. Install Python 3:
   ```
   sudo apt install python3
   ```

### Installing zmq

After installing Python, you need to install `zmq` (ZeroMQ), a high-performance asynchronous messaging library, which is required for this project's messaging functionalities.

- Install `zmq` using pip:
   ```
   pip3 install pyzmq
   ```

## Usage

Here's how to get started with the project:

### Starting the Messaging Server

Run the messaging server using:
```
python3 message_server.py
```

### Managing Users

To create or manage users, execute: {when executed allows user to enter the desired choice - asks user to enter the port number of Group to interact and performs the desired Operations according to provided choices}

```
python3 user1.py  
python3 user2.py
```

### Handling Groups

For group management, use: {Asks to provide Port number as input}
```
python3 group.py
```

## Contributing

Contributions to the project are welcome! Here's how you can contribute:

## License

This project is licensed under the MIT License - see the LICENSE file for details.