import boto3
import os

sqs = boto3.resource('sqs', region_name= os.getenv('region'))


try:
        response = client.purge_queue(
             QueueUrl= input('Insert the queue to be purge: ')
        )

        print('Done successfully')

except client.exceptions.QueueDoesNotExist as error :
        print(error)

except client.exceptions.PurgeQueueInProgress as error :
        print(error)







