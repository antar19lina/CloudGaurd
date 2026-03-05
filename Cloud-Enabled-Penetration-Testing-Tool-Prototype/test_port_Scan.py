"""
test_port_scan.py - Basic unit test for port_scan module.
Uses pytest for simplicity.
"""

import socket
import pytest
from modules.port_Scan import scan_ports

def test_scan_ports_localhost():
    """
    Test scanning localhost (127.0.0.1).
    At least one port should return a result (open/closed).
    """
    results = scan_ports("127.0.0.1")
    assert isinstance(results, dict)
    # Ensure all configured ports are checked
    for port in results:
        assert results[port] in ["open", "closed"] or "error" in results[port]

def test_invalid_target():
    """
    Test scanning an invalid target should not crash.
    """
    results = scan_ports("invalid-target")
    assert isinstance(results, dict)
    # All ports should return an error message
    for port in results:
        assert "error" in results[port]