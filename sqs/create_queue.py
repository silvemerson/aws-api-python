import boto3

sqs = boto3.resource('sqs')



name = input('Insira o nome da fila que será criada: ')

queue = sqs.create_queue(QueueName=name, Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

