import boto3
def getInstances():
    ec2 = boto3.client('ec2')
    for item in ec2.describe_instances()['Reservations']:
        if(item['Instances'][0]['State']['Name'] == 'running'):
            print(item['Instances'][0]['State']['Name'], end='  ')
            print('ID =', item['Instances'][0]['InstanceId'], end='  ')
            print('IP =',item['Instances'][0]['PublicIpAddress'], end='  ')
            print('AMI =',item['Instances'][0]['ImageId'], end='  ')
            print('SubnetID =',item['Instances'][0]['SubnetId'], end='  ')
            print("Volumes {", end=' ')
            for v in item['Instances'][0]['BlockDeviceMappings']:
                print(v['Ebs']['VolumeId'], end=' ')
            print('}')
        else:
            print(item['Instances'][0]['State']['Name'], end='   ')
            print('ID =', item['Instances'][0]['InstanceId'])