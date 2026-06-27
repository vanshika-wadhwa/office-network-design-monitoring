import socket

def scan_port(ip, port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)

        result=sock.connect_ex((ip,port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")
    
def scan_range(ip,start_port, end_port):
    print(f"Scanning ports from {start_port} to {end_port} on {ip}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Main program
print("=" * 40)
print("      PORT SCANNER TOOL")
print("=" * 40)

ip = input("\nEnter IP to scan: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

scan_range(ip, start, end)