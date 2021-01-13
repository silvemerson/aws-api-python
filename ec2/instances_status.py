import boto3
import os
client = boto3.client('ec2', region_name= os.getenv('region'))

count_instances = 0

response = client.describe_instances()

for reservation in response ['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_name = instance['Tags'][0]['Value']
        instance_state_name = instance['State']['Name']
        print(instance_id,instance_name,instance_state_name)
        count_instances += 1

print()
print(f"Total instances: {count_instances}")
