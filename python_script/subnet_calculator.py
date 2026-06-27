import ipaddress

def subnet_calculator(ip, mask):
    try:
        # Create network
        network = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False)
        
        print("\n" + "=" * 40)
        print("      SUBNET CALCULATOR")
        print("=" * 40)
        print(f"\n📌 IP Address:      {ip}")
        print(f"📌 Subnet Mask:     {network.netmask}")
        print(f"📌 Network Address: {network.network_address}")
        print(f"📌 Broadcast:       {network.broadcast_address}")
        print(f"📌 Total Hosts:     {network.num_addresses}")
        print(f"📌 Usable Hosts:    {network.num_addresses - 2}")
        print(f"📌 First Host:      {list(network.hosts())[0]}")
        print(f"📌 Last Host:       {list(network.hosts())[-1]}")
        print(f"📌 CIDR Notation:   {network}")
        
    except Exception as e:
        print(f"Error: {e}")

# Main program
print("=" * 40)
print("      SUBNET CALCULATOR")
print("=" * 40)

ip = input("\nEnter IP Address: ")
mask = input("Enter Subnet Mask or CIDR (e.g. 255.255.255.0 or 24): ")

subnet_calculator(ip, mask)