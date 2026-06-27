import os
import platform # Windows/Linux detection

def ping(ip):
    # -n for windows, -c for linux/mac
    param='-n' if platform.system().lower()=='windows' else '-c'
    # send 1 packet to ip address
    response=os.system(f"ping {param} 1 {ip}")

    if response ==0:
        print(f"\n{ip} is online")
    else:
        print(f"\n{ip} is offline")

print("="*40)
print('          Network Ping Tool')
print("="*40)

ip=input("Enter the IP address to ping: ")
ping(ip)