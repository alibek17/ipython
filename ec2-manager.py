import boto3
import argparse
import awsboto3
parser = argparse.ArgumentParser(description='Script to manage EC2 instances.')

arguments = parser.add_argument_group('Arguments')
arguments.add_argument('-n', '--name', help='Image name to be used for the instance', required=False)
arguments.add_argument('-l', '--list', help='List running instances', action='store_true', required=False)
arguments.add_argument('-k', '--key', help='Key name', required=False)
arguments.add_argument('-t', '--type', help='Instance type', required=False)
arguments.add_argument('-d', '--delete', nargs='+', help='ID of the instance to delete', required=False)
arguments.add_argument('-s', '--snap', nargs='+', help='ID of the volumes to take a snapshot', required=False)

args = parser.parse_args()

images = {'amznlinux':'ami-0bbc25e23a7640b9b', 'centos':'ami-0ff760d16d9497662'}

def main():

    if (args.list):
        awsboto3.getInstances()
        exit()

    if(args.delete):
        awsboto3.deleteInstance(args.delete)
        exit()

    if(args.snap):
        awsboto3.createSnapshot(args.snap)
        exit()

    if(args.name):
        if (args.name in images.keys()):
            key = args.key if args.key else 'almac'
            instancetype = args.type if args.type else 't2.nano'
            awsboto3.createInstance(images[args.name], 1, 1, instancetype, key)
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
