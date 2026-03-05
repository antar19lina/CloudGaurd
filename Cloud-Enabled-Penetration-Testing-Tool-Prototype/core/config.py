"""
config.py - Centralized settings for scans and AWS integration.
Beginner-friendly, but structured for professional use.
"""

import os

# -------------------------------
# Scan Settings
# -------------------------------
DEFAULT_PORTS = [21, 22, 80, 443]  # Common ports to scan
REQUIRED_HEADERS = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
] 
TIMEOUT = 2  

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "your-pentest-reports-bucket")
ENABLE_S3_UPLOAD = os.getenv("ENABLE_S3_UPLOAD", "False").lower() == "true"

REPORT_FILE = os.getenv("REPORT_FILE", "reports/report.json")
LOG_FILE = os.getenv("LOG_FILE", "logs/runtime.log")

# -------------------------------
# Helper Function
# -------------------------------
def show_config():
    """Print current configuration (safe values only)."""
    print("=== Pentest Framework Configuration ===")
    print(f"Default Ports: {DEFAULT_PORTS}")
    print(f"Required Headers: {REQUIRED_HEADERS}")
    print(f"Timeout: {TIMEOUT}s")
    print(f"AWS Region: {AWS_REGION}")
    print(f"S3 Bucket: {S3_BUCKET_NAME}")
    print(f"S3 Upload Enabled: {ENABLE_S3_UPLOAD}")
    print(f"Report File: {REPORT_FILE}")
    print(f"Log File: {LOG_FILE}")
    print("=======================================")


if __name__ == "__main__":
    # Quick check when running directly
    show_config()