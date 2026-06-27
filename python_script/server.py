import socket
server=socket.socket()
server.bind(('localhost',9999))
server.listen(1)
print("server is waiting for connections...")
conn, addr=server.accept()
print("connected with", addr)

#chat loop
while True:
    message=conn.recv(1024).decode()
    if message.lower()=='quit':
        break
    print("client:", message)
    reply=input("server: ")
    conn.send(bytes(reply, 'utf-8'))
conn.close()
print("connection closed")