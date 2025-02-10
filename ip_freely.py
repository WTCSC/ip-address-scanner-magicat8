import ipaddress
import subprocess
import sys
import time

def ping_ip(ip):
    """Ping a single IP address and return the result (up/down/error)."""
    try:
        # Ping the IP address using the system ping command.
        # For Windows, the command is 'ping -n 1', for Linux/Mac it's 'ping -c 1'
        response = subprocess.run(
            ['ping', '-c', '1', str(ip)], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            timeout=2
        )
        
        if response.returncode == 0:
            # Parse the response time from the output (Linux/Mac)
            response_time = float(response.stdout.decode().split('time=')[1].split(' ms')[0])
            return (True, response_time)
        else:
            return (False, "No response")
    
    except subprocess.TimeoutExpired:
        return (False, "Connection timeout")
    except Exception as e:
        return (False, str(e))

def scan_network(cidr):
    """Scan the network range based on the CIDR input."""
    network = ipaddress.IPv4Network(cidr, strict=False)
    print(f"Scanning network {cidr}...")
    
    active_hosts = 0
    down_hosts = 0
    error_hosts = 0
    results = []

    # Iterate over all host addresses in the network (excluding network and broadcast addresses)
    for ip in network.hosts():
        print(f"Scanning {ip}...")
        status, message = ping_ip(ip)
        
        if status:
            results.append(f"{ip}   - UP   ({message:.2f}ms)")
            active_hosts += 1
        else:
            if "timeout" in message.lower():
                results.append(f"{ip}   - ERROR ({message})")
                error_hosts += 1
            else:
                results.append(f"{ip}   - DOWN ({message})")
                down_hosts += 1

    print("\nScan complete.")
    print(f"Found {active_hosts} active hosts, {down_hosts} down, {error_hosts} error.")

    for result in results:
        print(result)

if __name__ == "__main__":
    # Check if the script received an argument (CIDR notation)
    if len(sys.argv) != 2:
        print("Usage: python ip_freely.py <CIDR>")
        sys.exit(1)
    
    cidr_input = sys.argv[1]
    
    try:
        # Validate the CIDR notation
        ipaddress.IPv4Network(cidr_input, strict=False)
        scan_network(cidr_input)
    except ValueError:
        print(f"Invalid CIDR notation: {cidr_input}")
        sys.exit(1)
