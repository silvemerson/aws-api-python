import boto3

sqs = boto3.resource('sqs')

fila = input('Insira o nome da fila que será enviado a mensagem: ')

queue = sqs.get_queue_by_name(QueueName=fila)

response = queue.send_message(MessageBody='mundo')

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))