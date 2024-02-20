import pika
import json

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queues
channel.queue_declare(queue='user_requests')
channel.queue_declare(queue='youtuber_requests')
channel.queue_declare(queue='notifications')

# A data structure to hold YouTuber and video information
youtubers = {}

# A data structure to hold user subscriptions
user_subscriptions = {}

# Process user requests
def consume_user_requests(ch, method, properties, body):
    request = json.loads(body)
    username = request['user']
    
    # Login user
    if 'login' in request:
        print(f"{username} logged in")
        # Send all pending notifications to the user
        if username in user_subscriptions:
            for youtuber, videos in user_subscriptions[username].items():
                for video in videos:
                    print(f"New Notification: {youtuber} uploaded {video}")
            user_subscriptions[username] = {y: [] for y in user_subscriptions[username]}

    # Subscription update
    elif 'subscribe' in request or 'unsubscribe' in request:
        action = 'subscribed' if 'subscribe' in request else 'unsubscribed'
        youtuber = request['youtuber']
        print(f"{username} {action} to {youtuber}")
        if action == 'subscribed':
            if username not in user_subscriptions:
                user_subscriptions[username] = {}
            if youtuber not in user_subscriptions[username]:
                user_subscriptions[username][youtuber] = []
        else:
            if youtuber in user_subscriptions.get(username, {}):
                del user_subscriptions[username][youtuber]

# Process youtuber requests
def consume_youtuber_requests(ch, method, properties, body):
    request = json.loads(body)
    youtuber = request['youtuber']
    video_name = request['videoName']
    
    print(f"{youtuber} uploaded {video_name}")
    # Update youtubers data structure
    if youtuber not in youtubers:
        youtubers[youtuber] = []
    youtubers[youtuber].append(video_name)
    
    # Notify subscribed users
    for user, subscriptions in user_subscriptions.items():
        if youtuber in subscriptions:
            channel.basic_publish(exchange='',
                                  routing_key='notifications',
                                  body=json.dumps({'user': user, 'youtuber': youtuber, 'videoName': video_name}))
            user_subscriptions[user][youtuber].append(video_name)

# Start consuming messages
channel.basic_consume(queue='user_requests', on_message_callback=consume_user_requests, auto_ack=True)
channel.basic_consume(queue='youtuber_requests', on_message_callback=consume_youtuber_requests, auto_ack=True)

print('YouTubeServer is running and waiting for messages...')
channel.start_consuming()
