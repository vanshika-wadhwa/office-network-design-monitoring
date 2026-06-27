import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(('localhost', 9999))
print("Connected to Server!")

# Chat loop
while True:
    message = input("You: ")
    client.send(message.encode())
    if message == 'quit':
        break
    reply = client.recv(1024).decode()
    print(f"Server: {reply}")

client.close()
print("Disconnected!")