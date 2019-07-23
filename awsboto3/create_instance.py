import boto3
def createInstance(ami, mincount, maxcount, instancetype='t2.nano', keyname='almac'):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=ami,
        InstanceType=instancetype,
        MaxCount=mincount,
        MinCount=maxcount,
        KeyName = keyname,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                #'VirtualName': 'string',
                'Ebs': {
                    'DeleteOnTermination': True,
                    #'Iops': 123,
                    #'SnapshotId': 'string',
                    #'VolumeSize': 123,
                    'VolumeType': 'gp2'  #'standard'|'io1'|'gp2'|'sc1'|'st1',
                    #'Encrypted': True|False,
                    #'KmsKeyId': 'string'
                },
                #'NoDevice': 'string'
            },
        ],
        #DryRun=True
    )
    return instance