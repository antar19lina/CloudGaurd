# runner.py - Main entry point for the Ethical Pentest Framework with AWS

import sys
import os
import json
import logging
from datetime import datetime

# --------------------------------------------------
# Resolve PROJECT ROOT safely (Windows compatible)
# --------------------------------------------------
CURRENT_FILE = os.path.abspath(__file__)
CORE_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_ROOT = os.path.dirname(CORE_DIR)

# Fix Python imports
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --------------------------------------------------
# Create required directories BEFORE logging
# --------------------------------------------------
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# Absolute file paths
LOG_FILE = os.path.join(LOGS_DIR, "runtime.log")
REPORT_FILE = os.path.join(REPORTS_DIR, "report.json")

# --------------------------------------------------
# Logging Setup (SAFE)
# --------------------------------------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Imports AFTER path setup
# --------------------------------------------------
from modules.port_Scan import scan_ports
from modules.web_check import check_headers
from modules.dir_enum import enumerate_dirs
from modules.vuln_check import check_vulns
from core.config import ENABLE_S3_UPLOAD
from aws.s3_upload import upload_to_s3

# --------------------------------------------------
# Main Function
# --------------------------------------------------
def main():
    print("\n🛡️ Cloud-Enabled Ethical Penetration Testing Tool")
    print("⚠️ LEGAL NOTICE: Educational & authorized use only.\n")

    confirm = input("Do you agree to ethical usage? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("❌ Exiting: Ethical consent not provided.")
        return

    target = input("Enter target (example.com or IP): ").strip()
    if not target:
        print("❌ No target provided.")
        return

    report = {
        "target": target,
        "timestamp": datetime.now().isoformat(),
        "results": {}
    }

    try:
        print("\n🔍 Running Port Scan...")
        report["results"]["port_scan"] = scan_ports(target)

        print("🌐 Checking Security Headers...")
        report["results"]["web_check"] = check_headers(target)

        print("📁 Enumerating Directories...")
        report["results"]["dir_enum"] = enumerate_dirs(target)

        print("🧪 Performing Vulnerability Checks...")
        report["results"]["vuln_check"] = check_vulns(target)

        logging.info(f"Scan completed successfully for {target}")

    except Exception as e:
        logging.error(f"Scan execution error: {e}")
        print(f"⚠️ Scan error occurred: {e}")

    # --------------------------------------------------
    # Save Report
    # --------------------------------------------------
    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"\n✅ Report saved successfully → {REPORT_FILE}")
        logging.info("Report saved successfully")

    except Exception as e:
        logging.error(f"Report save failed: {e}")
        print("❌ Failed to save report")

    # --------------------------------------------------
    # Optional AWS S3 Upload
    # --------------------------------------------------
    if ENABLE_S3_UPLOAD:
        try:
            upload_to_s3(REPORT_FILE)
            print("☁️ Report uploaded to AWS S3")
            logging.info("Report uploaded to S3")
        except Exception as e:
            logging.error(f"S3 upload failed: {e}")
            print("⚠️ AWS S3 upload failed")

    print("\n🎯 Scan completed. Exiting safely.\n")


if __name__ == "__main__":
    main()
# ... (existing imports and path setup remain the same)

# -------------------------------
# Main Function
# -------------------------------
def main():
    print("🛡️ Ethical Pentest Framework with AWS")
    print("⚠️ LEGAL NOTICE: For educational use only. Authorized targets only.")

    confirm = input("Agree to ethical use? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Exiting: You must agree to ethical use.")
        return

    target = input("Target (e.g., example.com): ").strip()
    if not target:
        print("No target provided. Exiting.")
        return

    report = {
        "target": target,
        "timestamp": datetime.now().isoformat(),
        "results": {}
    }

    try:
        # Run scans (now with better error handling in modules)
        report["results"]["port_scan"] = scan_ports(target)
        report["results"]["web_check"] = check_headers(target)
        report["results"]["dir_enum"] = enumerate_dirs(target)
        report["results"]["vuln_check"] = check_vulns(target)

        logging.info(f"Scans completed successfully for {target}")
        print("✅ Scans completed.")
    except Exception as e:
        logging.error(f"Error during scans: {e}")
        print(f"⚠️ Error occurred during scans: {e}")
        report["results"]["error"] = str(e)  # Add error to report

    # Save report (always attempt, even if scans fail)
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(report, f, indent=4)
        print(f"✅ Report saved to {REPORT_FILE}")
    except Exception as e:
        logging.error(f"Error saving report: {e}")
        print(f"⚠️ Could not save report: {e}. Check file permissions or path.")

    # Optional AWS upload
    if ENABLE_S3_UPLOAD:
        try:
            upload_to_s3(REPORT_FILE)
            print("☁️ Report uploaded to S3 successfully.")
        except Exception as e:
            logging.error(f"S3 upload failed: {e}")
            print(f"⚠️ S3 upload failed: {e}")

# ... (if __name__ == "__main__": main() remains the same)