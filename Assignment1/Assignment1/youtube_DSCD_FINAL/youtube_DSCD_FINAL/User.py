import sys
import pika
import json

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Update subscription
def update_subscription(username, action, youtuber_name):
    message = {
        'user': username,
        'youtuber': youtuber_name,
        action: True
    }
    channel.basic_publish(exchange='',
                          routing_key='user_requests',
                          body=json.dumps(message))
    print("SUCCESS")

# Receive notifications
def receive_notifications(ch, method, properties, body):
    notification = json.loads(body)
    print(f"New Notification: {notification['youtuber']} uploaded {notification['videoName']}")

channel.queue_declare(queue='notifications')

# Start receiving notifications
channel.basic_consume(queue='notifications', on_message_callback=receive_notifications, auto_ack=True)

username = sys.argv[1]

# Send login message
update_subscription(username, 'login', None)

# If additional arguments are provided, process subscription updates
if len(sys.argv) > 2:
    action = 'subscribe' if sys.argv[2] == 's' else 'unsubscribe'
    youtuber_name = sys.argv[3]
    update_subscription(username, action, youtuber_name)

print(f"{username} is logged in and waiting for notifications...")
channel.start_consuming()
