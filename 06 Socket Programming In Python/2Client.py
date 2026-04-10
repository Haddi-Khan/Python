import socket
HOST = "127.0.0.1"  
PORT = 65432       
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server. Type messages to send. Type 'quit' to exit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            print("Closing connection...")
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        if not data:
            print("Server closed the connection.")
            break
        print("Server:", data.decode())
