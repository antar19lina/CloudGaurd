"""
s3_upload.py - Upload reports to S3 bucket.
"""

import boto3
import os
from core.config import AWS_REGION, S3_BUCKET_NAME

def upload_to_s3(file_path: str) -> None:
    """
    Uploads the given file to the configured S3 bucket.
    """
    s3 = boto3.client("s3", region_name=AWS_REGION)
    file_name = os.path.basename(file_path)

    try:
        s3.upload_file(file_path, S3_BUCKET_NAME, file_name)
        print(f"[+] Uploaded {file_name} to S3 bucket: {S3_BUCKET_NAME}")
    except Exception as e:
        print(f"[ERROR] S3 upload failed: {e}")
        raise

if __name__ == "__main__":
    # Quick test run
    test_file = "reports/report.json"
    upload_to_s3(test_file)