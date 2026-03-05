# modules/port_scan.py - Simple port scanning module (updated for dict output)

import socket
from core.config import DEFAULT_PORTS, TIMEOUT

def scan_ports(target):
    """
    Scans a list of default ports on the target.
    Returns a dict of port statuses (e.g., {"21": "closed", "80": "open"}).
    """
    port_statuses = {}
    print(f"[+] Scanning ports on {target}...")
    for port in DEFAULT_PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                result = s.connect_ex((target, port))
                if result == 0:
                    port_statuses[str(port)] = "open"
                    print(f"[OPEN] Port {port}")
                else:
                    port_statuses[str(port)] = "closed"
        except socket.gaierror:
            print(f"[ERROR] Invalid hostname: {target}")
            port_statuses["error"] = "Invalid hostname"
            break
        except Exception as e:
            print(f"[ERROR] Scanning port {port}: {e}")
            port_statuses[str(port)] = "error"
    return port_statuses

if __name__ == "__main__":
    print(scan_ports("example.com"))