# IP Freely - Network Scanner

## Overview

The `IP Freely` tool is a simple Python-based network scanner that scans IP addresses within a given network range. It takes CIDR notation (e.g., `192.168.1.0/24`) as input, calculates the valid host addresses in that range, and checks which IPs respond to a ping request. This tool is useful for detecting active devices within your network.

## Features

- Takes CIDR notation as input (e.g., `192.168.1.0/24`).
- Calculates the network range and iterates through all valid host addresses.
- Pings each IP address and reports the status (UP/DOWN/Error) for each.
- Displays the response time (in milliseconds) for active IPs.
- Provides detailed output, including errors such as timeouts or no response.

## Requirements

- Python 3.x
- Network access for scanning

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ip_freely.git
    cd ip_freely
    ```

2. Ensure you have Python 3.x installed.

3. If needed, create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

4. No additional dependencies are required for this script. It uses Python's built-in `subprocess` and `ipaddress` modules.

## Usage

To run the scanner, use the following command:

```bash
python ip_freely.py <CIDR>
```

Flags and Arguments
<CIDR>: The CIDR notation for the network you want to scan (e.g., 192.168.1.0/24).
Error Handling
The script handles the following errors:

No response: The IP address did not respond to the ping request.
Connection timeout: The ping request timed out.
Invalid CIDR notation: The provided CIDR notation is invalid.
