import boto3
import os

sqs = boto3.resource('sqs', region_name= os.getenv('region'))

fila = input('Enter the name of the queue that will be sent the message: ')

queue = sqs.get_queue_by_name(QueueName=fila)

response = queue.send_message(MessageBody='mundo')

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))