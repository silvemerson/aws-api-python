sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='fila_de_testes')

response = queue.send_message(MessageBody='mundo')

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'
