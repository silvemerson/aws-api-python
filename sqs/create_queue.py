import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName='fila_de_testes', Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))
