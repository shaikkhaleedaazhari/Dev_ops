import boto3
def create_ec2_instance():
    try:
        print("creating ec2 instance")
        resource_ec2=boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId= "ami-085ad6ae776d8f09c",
            MinCount= 1,
            MaxCount =1,
            InstanceType= "t2.micro",
            keyname = "Ec2 Exp"
        )
        
    except Exception as e:
        print(e)
create_ec2_instance()