#!/bin/bash
# Launches EC2 with IAM role for S3 access
# Beginner-friendly, recruiter-ready version

# -------------------------------
# Configurable Variables
# -------------------------------
INSTANCE_TYPE="t2.micro"
AMI_ID="ami-0c02fb55956c7d316"   # Amazon Linux 2 AMI (update if region differs)
KEY_NAME="your-key-pair"         # Must exist in AWS EC2 console
SECURITY_GROUP="pentest-sg"      # Pre-created security group
IAM_ROLE_NAME="PentestRole"      # IAM role with iam_policy.json attached

# -------------------------------
# Launch EC2 Instance
# -------------------------------
echo "[+] Launching EC2 instance..."
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id $AMI_ID \
  --count 1 \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-groups $SECURITY_GROUP \
  --iam-instance-profile Name=$IAM_ROLE_NAME \
  --query 'Instances[0].InstanceId' \
  --output text)

echo "[+] Waiting for instance to be running..."
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# -------------------------------
# Get Public IP
# -------------------------------
PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text)

echo "[+] Instance launched: $INSTANCE_ID"
echo "[+] Public IP: $PUBLIC_IP"

# -------------------------------
# Connect via SSH and Setup Docker
# -------------------------------
echo "[+] Connecting via SSH to configure Docker..."
ssh -o StrictHostKeyChecking=no -i ~/.ssh/$KEY_NAME.pem ec2-user@$PUBLIC_IP << EOF
  sudo yum update -y
  sudo amazon-linux-extras install docker -y
  sudo service docker start
  sudo usermod -a -G docker ec2-user
  echo "[+] Docker installed and started."
  # Placeholder: run your Docker image here
EOF