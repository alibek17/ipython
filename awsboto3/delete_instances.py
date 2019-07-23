import boto3
def deleteInstance(instances):
    ec2 = boto3.client('ec2')
    response = ec2.terminate_instances(
        InstanceIds=instances,
        #DryRun=True|False
    )
    return response