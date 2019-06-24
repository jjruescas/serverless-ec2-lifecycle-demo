import boto3
import json

def lambda_handler(event, context):
    ec2client = boto3.client('ec2')
    ec2 = boto3.resource('ec2')

    instances = []

    response = ec2client.describe_instances()
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instanceId = instance["InstanceId"]
            
            ec2instance = ec2.Instance(instanceId)
            instancename = ''

            if ec2instance.tags:
                for tags in ec2instance.tags:
                    if tags["Key"] == 'Name':
                        instancename = tags["Value"]
            
            print(f"{instanceId} - {instancename}")
            instances.append(str(instanceId) + " - " + instancename)


    body = {
        "instances": str(instances)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

