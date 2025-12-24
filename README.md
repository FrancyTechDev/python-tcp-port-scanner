# Python TCP Port Scanner

A minimal and reliable TCP port scanner written in Python, designed for
educational use and as a foundational module for security automation pipelines.

## Overview

This tool performs a TCP connect scan against a target host and port.
It is intentionally simple, readable, and auditable, prioritizing clarity
and correctness over raw scanning speed.

The project serves both as a learning resource and as a base component
for more advanced vulnerability assessment tools.

## Features

- TCP connect scan using Python sockets
- Explicit timeout handling
- Command-line interface (CLI)
- Clear exit codes for scripting and automation
- Zero external dependencies

## Use Cases

- Network reconnaissance in controlled environments
- Educational demonstrations of TCP connection behavior
- Pre-scan step in vulnerability assessment workflows
- Base module for security automation tools

## Requirements

- Python 3.9+
- Linux / macOS / Windows

## Example Output

[+] Port 443 is open
[-] Port 22 is closed


## Audit Context

This tool is used as a preliminary step in a non-invasive security audit.
It helps identify exposed services and open ports on public-facing systems
before conducting higher-level vulnerability assessments.


## Installation

```bash
git clone https://github.com/FrancyTechDev/python-tcp-port-scanner.git
cd python-tcp-port-scanner
chmod +x scanner.py

Usage

./scanner.py <host> <port>

Example

./scanner.py google.com 443

Output:

[+] Port 443 is open

Project Structure

.
├── scanner.py
├── README.md
├── LICENSE
├── requirements.txt
└── docs/

Design Notes

    Uses a blocking TCP connect scan for simplicity and reliability

    Explicit timeouts prevent hanging connections

    Minimal codebase to ease auditing and extension

Limitations

    Single-port scanning

    No parallel execution

    No service fingerprinting

These limitations are intentional and documented.
Roadmap

    Multi-port scanning

    Parallel connections

    JSON and HTML report output

    Integration into an automated audit pipeline

Legal Disclaimer

This tool is intended only for educational purposes and for scanning systems
you own or have explicit permission to test. Unauthorized scanning of
third-party systems may be illegal.
Author

FrancyTech
GitHub: https://github.com/FrancyTechDev

LinkedIn: https://www.linkedin.com/in/francesco-macr%C3%AC-61645939a/

