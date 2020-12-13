import boto3

client = boto3.client('ec2', region_name='us-east-1')


try:
        id_instaces = input ("Insira o ID da sua instância: ")

        response = client.start_instances(
        InstanceIds=[id_instaces]
        )

        print(response)


except:

        print('ID não encontrado, tente novamente')