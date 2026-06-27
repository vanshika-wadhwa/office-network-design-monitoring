import socket
import os
import platform
from datetime import datetime

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = os.system(f'ping {param} 1 -w 1000 {ip} > nul 2>&1')
    return response == 0

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except:
        return "Unknown"

def scan_network(network):
    print("\n" + "=" * 40)
    print("      NETWORK SCANNER")
    print("=" * 40)
    print(f"Scanning Network: {network}.0/24")
    print(f"Started at: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 40)
    
    active_devices = []
    
    for i in range(1, 255):
        ip = f"{network}.{i}"
        if ping_host(ip):
            hostname = get_hostname(ip)
            active_devices.append(ip)
            print(f"✅ {ip} is ONLINE | Hostname: {hostname}")
    
    print("\n" + "=" * 40)
    print(f"Scan Complete!")
    print(f"Total Active Devices: {len(active_devices)}")
    print(f"Ended at: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 40)

# Main program
print("=" * 40)
print("      NETWORK SCANNER")
print("=" * 40)

network = input("\nEnter Network (e.g. 192.168.1): ")
scan_network(network)