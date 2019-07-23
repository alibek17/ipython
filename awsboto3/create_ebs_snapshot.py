import boto3
def createSnapshot(volume_ids):
    ec2 = boto3.resource('ec2')
    for volume_id in volume_ids:
        volume = ec2.Volume(volume_id)
        snapshot = volume.create_snapshot(
            Description='string',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            #DryRun=True|False
        )