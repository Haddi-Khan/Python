import socket
Host = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host,PORT))
    s.listen()
    conn,addr = s.accept()
with conn :
    print (f"connected by {addr}")
    while True:
        print("hello")
        data = conn.recv(1024)
        if not data :
            break
        conn.sendall(data)


