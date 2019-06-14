import json
import boto3

client = boto3.resource('ec2')

instance_tag = 'SLS-Demo'

def lambda_handler(event, context):

    terminate_result = client.instances.filter(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [instance_tag]
            },
        ]
    ).terminate()

    print(terminate_result)

    print(f"Terminating Instance...")

    return terminate_result;