import boto3

client = boto3.client('sqs', region_name='us-east-1')


try:
        response = client.purge_queue(
             QueueUrl= input('Insert the queue to be purge: ')
        )

        print('Done successfully')

except client.exceptions.QueueDoesNotExist as error :
        print(error)

except client.exceptions.PurgeQueueInProgress as error :
        print(error)







