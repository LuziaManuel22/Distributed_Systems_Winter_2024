import sys
import pika
import json

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Publish video
def publish_video(youtuber, video_name):
    channel.basic_publish(exchange='',
                          routing_key='youtuber_requests',
                          body=json.dumps({'youtuber': youtuber, 'videoName': video_name}))
    print("SUCCESS")

youtuber_name = sys.argv[1]
video_name = ' '.join(sys.argv[2:])

publish_video(youtuber_name, video_name)
