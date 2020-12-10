import boto3

client = boto3.client('sqs', region_name='us-east-1')

response = client.purge_queue(
        QueueUrl= input('Insira a fila que será feito o purge: ')
)
