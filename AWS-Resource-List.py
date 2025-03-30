import sys
import subprocess
import os

def check_aws_cli():
    """Check if AWS CLI is installed."""
    try:
        subprocess.run(["aws", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("AWS CLI is not installed. Please install the AWS CLI and try again.")
        sys.exit(1)

def check_aws_configured():
    """Check if AWS CLI is configured."""
    if not os.path.exists(os.path.expanduser("~/.aws")):
        print("AWS CLI is not configured. Please configure the AWS CLI and try again.")
        sys.exit(1)

def list_resources(aws_region, aws_service):
    """List resources based on the AWS service."""
    services = {
        "ec2": f"aws ec2 describe-instances --region {aws_region}",
        "rds": f"aws rds describe-db-instances --region {aws_region}",
        "s3": f"aws s3api list-buckets --region {aws_region}",
        "cloudfront": f"aws cloudfront list-distributions --region {aws_region}",
        "vpc": f"aws ec2 describe-vpcs --region {aws_region}",
        "iam": f"aws iam list-users --region {aws_region}",
        "route53": f"aws route53 list-hosted-zones --region {aws_region}",
        "cloudwatch": f"aws cloudwatch describe-alarms --region {aws_region}",
        "cloudformation": f"aws cloudformation describe-stacks --region {aws_region}",
        "lambda": f"aws lambda list-functions --region {aws_region}",
        "sns": f"aws sns list-topics --region {aws_region}",
        "sqs": f"aws sqs list-queues --region {aws_region}",
        "dynamodb": f"aws dynamodb list-tables --region {aws_region}",
        "ebs": f"aws ec2 describe-volumes --region {aws_region}"
    }

    if aws_service not in services:
        print("Invalid service. Please enter a valid service.")
        sys.exit(1)

    print(f"Listing {aws_service.upper()} in {aws_region}")
    try:
        result = subprocess.run(services[aws_service], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error listing resources for {aws_service}: {e.stderr.decode()}")

def main():
    """Main function to run the script."""
    if len(sys.argv) != 3:
        print("Usage: python aws_resource_list.py <aws_region> <aws_service>")
        print("Example: python aws_resource_list.py us-east-1 ec2")
        sys.exit(1)

    aws_region = sys.argv[1]
    aws_service = sys.argv[2].lower()

    check_aws_cli()
    check_aws_configured()
    list_resources(aws_region, aws_service)

if __name__ == "__main__":
    main()