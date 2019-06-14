import json
import boto3

client = boto3.resource('ec2')

instance_type = 'm4.xlarge'
instance_tag = 'SLS-Demo'
ami_id = "ami-015954d5e5548d13b" #Amazon Linux 2 AMI in us-west-1

def lambda_handler(event, context):

    print("Launching EC2 Instance...")

    ec2_result = client.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1, 
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_tag
                    },
                ]
            },
        ]
        )

    instance_id = ec2_result[0].instance_id

    print(f"EC2 Instance Id: {instance_id}")

    instance = client.Instance(id=instance_id)

    print(f"Waiting for instance {instance_id} to reach running state...")

    instance.wait_until_running()

    print("DONE WAITING!! The instance is running now.")

    response = {
        "statusCode": 200,
        "instance": instance_id
    }

    return response