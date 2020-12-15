import boto3

sqs = boto3.resource('sqs')



name = input('Enter the name of the queue that will be created:')

queue = sqs.create_queue(QueueName=name, Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

