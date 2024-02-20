
# YouTube Clone Project

## Overview

This project aims to replicate basic functionalities of YouTube, providing a platform for content sharing and viewing. It consists of several key components:

- **YoutubeServer**: Manages server-side operations.
- **Youtuber**: Facilitates content creators' interactions with the platform, including video uploads and channel management.
- **User**: Allows users to interact with the platform by creating profiles, subscribing to channels, and viewing videos.

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
3. Verify the installation:
   ```
   python3 --version
   ```

### RabbitMQ Installation

RabbitMQ is used for message queuing between different components of the application.

1. Add the RabbitMQ repository to your system:
   ```
   echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
   ```
2. Update the package index:
   ```
   sudo apt-get update
   ```
3. Install RabbitMQ server:
   ```
   sudo apt-get install rabbitmq-server
   ```
4. Enable and start the RabbitMQ service:
   ```
   sudo systemctl enable rabbitmq-server
   sudo systemctl start rabbitmq-server
   ```
5. (Optional) To manage RabbitMQ through its web interface, enable the management plugin:
   ```
   sudo rabbitmq-plugins enable rabbitmq_management
   ```
## Usage

### Starting the Server

- To start the YouTube server, run:
  ```
  python3 YoutubeServer.py
  ```

### Youtuber Operations

This file represents the Youtuber service. It takes two command line arguments: the YouTuber's name and the video they want to publish.

- **Methods**:
  - **publishVideo(youtuber, videoName)**: Sends the video to the YoutubeServer. The server adds a new YouTuber if the name appears for the first time; otherwise, it adds the video to the existing YouTuber. Prints “SUCCESS” message when the video is received by the YoutubeServer.

- **Example**:
  ```
  # Run the Youtuber service to publish a video
  python3 Youtuber.py TomScott "After ten years, it's time to stop weekly videos."
  ```

### User Operations

This file represents the User service. It can take either 1 or 3 command line arguments. The first argument is the name of the user. If the user wants to subscribe or unsubscribe, the second argument is 's' or 'u', respectively, and the third argument is the name of the YouTuber. (Second and third arguments are optional)

- **Methods**:
  - **updateSubscription**: Sends the subscription/unsubscription request to the YouTubeServer.
  - **receiveNotifications**: Receives any notifications for the user's subscriptions and starts receiving real-time notifications for videos uploaded while the user is logged in. Prints notifications in the format: “New Notification: <YouTuberName> uploaded <videoName>”.

- **Examples**:
  ```
  # Run the User service to log in, subscribe to a YouTuber, and receive notifications
  python3 User.py username s TomScott

  # Run the User service to log in, unsubscribe from a YouTuber, and receive notifications
  python3 User.py username u TomScott

  # Run the User service to log in and receive notifications
  python3 User.py username
  ```

## Contributing

Contributions to the project are welcome! Here's how you can contribute:

## License

This project is licensed under the MIT License - see the LICENSE file for details.