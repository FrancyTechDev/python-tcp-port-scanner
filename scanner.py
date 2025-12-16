#!/usr/bin/env python3
import socket
import sys

def scan_port(host: str, port: int, timeout: float = 2.0) -> bool:
    """
    Attempts a TCP connection to the given host and port.
    Returns True if the port is open, False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except socket.gaierror:
        print("[-] Hostname resolution failed")
        sys.exit(2)
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]

    try:
        port = int(sys.argv[2])
    except ValueError:
        print("[-] Port must be an integer")
        sys.exit(1)

    if scan_port(host, port):
        print(f"[+] Port {port} is open")
        sys.exit(0)
    else:
        print(f"[-] Port {port} is closed")
        sys.exit(3)

if __name__ == "__main__":
    main()

