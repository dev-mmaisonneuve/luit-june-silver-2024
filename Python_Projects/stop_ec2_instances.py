import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get a list of all running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # Extract instance IDs from the response
    instances_to_stop = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

    if not instances_to_stop:
        print("No running instances found.")
    else:
        # Stop the instances
        print(f"Stopping instances: {instances_to_stop}")
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print("Instances are stopping...")