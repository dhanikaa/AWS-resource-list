# AWS Resource Listing Script

## Description
This script automates the process of listing resources in an AWS account for a specified service and region using the AWS Command Line Interface (CLI). It simplifies the task of auditing and managing your AWS resources by providing a quick overview of the specified service's resources.

## Supported AWS Services
The script supports the following AWS services:
1. **EC2** - Elastic Compute Cloud instances.
2. **RDS** - Relational Database Service instances.
3. **S3** - Simple Storage Service buckets.
4. **CloudFront** - Content Delivery Network distributions.
5. **VPC** - Virtual Private Cloud configurations.
6. **IAM** - Identity and Access Management users and roles.
7. **Route53** - DNS and domain management.
8. **CloudWatch** - Monitoring and logging services.
9. **CloudFormation** - Infrastructure as Code stacks.
10. **Lambda** - Serverless function services.
11. **SNS** - Simple Notification Service topics.
12. **SQS** - Simple Queue Service queues.
13. **DynamoDB** - NoSQL database tables.
14. **EBS** - Elastic Block Store volumes.

## Prerequisites
- **AWS CLI**: The AWS CLI must be installed and configured on your system.
- **AWS Configuration**: Ensure the AWS CLI is configured with appropriate credentials and default settings.

### Installing AWS CLI
If you haven't installed the AWS CLI, you can do so by following these instructions:

```bash
# On macOS
brew install awscli

# On Linux
sudo apt-get update
sudo apt-get install awscli

# On Windows
Download the installer from the [AWS CLI installation page](https://aws.amazon.com/cli/).
```

## Usage
1. Clone the repository or download the script.
2. Open your terminal and navigate to the directory containing the script.
3. Make the script executable (if it's not already):

   ```bash
   chmod +x aws_resource_listing.sh
   ```

4. Run the script with the desired service and region:

   ```bash
   ./aws_resource_listing.sh <service> <region>
   ```

   Replace `<service>` with the desired AWS service (e.g., `ec2`, `rds`, etc.) and `<region>` with the AWS region (e.g., `us-west-2`, `us-east-1`, etc.).

## Example
To list all EC2 instances in the `us-west-2` region, you would run:

```bash
./aws_resource_listing.sh ec2 us-west-2
```

## How It Works
The script leverages the AWS CLI commands to query specific services based on the user inputs for service type and AWS region. Upon execution, the script will:
1. Check if the required AWS CLI is installed and configured.
2. Parse command-line arguments for the service and region.
3. Execute the appropriate AWS CLI command to list the resources for the specified service.
4. Output the results in a user-friendly format.

