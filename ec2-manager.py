import boto3
import argparse

def getInstances():
    ec2 = boto3.client('ec2')
    for item in ec2.describe_instances()['Reservations']:
        if(item['Instances'][0]['State']['Name'] == 'running'):
            print(item['Instances'][0]['State']['Name'], end='   ')
            print('ID =', item['Instances'][0]['InstanceId'], end='   ')
            print('IP =',item['Instances'][0]['PublicIpAddress'], end='   ')
            print('AMI =',item['Instances'][0]['ImageId'], end='   ')
            print('SubnetID =',item['Instances'][0]['SubnetId'])
        else:
            print(item['Instances'][0]['State']['Name'], end='   ')
            print('ID =', item['Instances'][0]['InstanceId'])

def createInstance(ami, mincount, maxcount, instancetype='t2.nano', keyname='almac'):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId=images[ami],
        InstanceType=instancetype,
        MaxCount=mincount,
        MinCount=maxcount,
        KeyName = keyname,
        #DryRun=True
    )
    return instance

def deleteInstance(instances):
    ec2 = boto3.client('ec2')
    response = ec2.terminate_instances(
        InstanceIds=instances,
        #DryRun=True|False
    )
    return response

parser = argparse.ArgumentParser(description='Script to manage EC2 instances.')

arguments = parser.add_argument_group('Arguments')
arguments.add_argument('-n', '--name', help='Image name to be used for the instance', required=False)
arguments.add_argument('-l', '--list', help='List running instances', action='store_true', required=False)
arguments.add_argument('-k', '--key', help='Key name', required=False)
arguments.add_argument('-t', '--type', help='Instance type', required=False)
arguments.add_argument('-d', '--delete', nargs='+', help='ID of the instance to delete', required=False)
args = parser.parse_args()

images = {'amznlinux':'ami-0bbc25e23a7640b9b', 'centos':'ami-0ff760d16d9497662'}

def main():
    
    if (args.list):
        getInstances()
        exit()

    if(args.delete):
        deleteInstance(args.delete)
        exit()

    if(args.name):
        if (args.name in images.keys()):
            key = args.key if args.key else 'almac'
            instancetype = args.type if args.type else 't2.nano'
            createInstance(args.name, 1, 1, instancetype, key)
            exit()
        else:
            print('Image name is not supported.')
            exit()
    else:
        print("Script requires at least one argument")
        print(parser.print_help())
        exit()

if __name__ == "__main__" :
    main()
