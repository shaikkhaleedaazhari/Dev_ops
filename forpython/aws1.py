import boto3

# Define variables
AMI_ID = "ami-085ad6ae776d8f09c"
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "Ec2_key"
MIN_COUNT = 1
MAX_COUNT = 1

def create_ec2_instance(ami_id, instance_type, key_name, min_count, max_count):
    try:
        print("Creating EC2 instance...")
        ec2_client = boto3.client("ec2")
        ec2_client.run_instances(
            ImageId=ami_id,
            MinCount=min_count,
            MaxCount=max_count,
            InstanceType=instance_type,
            KeyName=key_name
        )
        print("EC2 instance created successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Call the function with variables
create_ec2_instance(AMI_ID, INSTANCE_TYPE, KEY_NAME, MIN_COUNT, MAX_COUNT)