import boto3

# Defining variables
ami_id = "ami-085ad6ae776d8f09c"
instance_type = "t2.micro"
key_name = "Ec2_key"
min_count = 1
max_count = 1

# Creating a list with all variables
ec2p = [ami_id, instance_type, key_name, min_count, max_count]

def create_ec2_instance(ec2p):
    try:
        print("Creating EC2 instance...")
        ec2_client = boto3.client("ec2")
        ec2_client.run_instances(
            ImageId=ec2p[0],
            InstanceType=ec2p[1],
            KeyName=ec2p[2],
            MinCount=ec2p[3],
            MaxCount=ec2p[4]
        )
        print("EC2 instance created successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Calling function with the list
create_ec2_instance(ec2p)
