import boto3

client = boto3.client('sqs', region_name='us-east-1')


try:

        response = client.purge_queue(
             QueueUrl= input('Insira a fila que será feito o purge: ')
        )

        print("Purge feito com sucesso")

except:
        print('Fila não encontrada')







