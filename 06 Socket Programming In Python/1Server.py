import selectors
import socket
sel = selectors.DefaultSelector()
HOST = "127.0.0.1"
PORT = 65432
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
print(f"Server listening on {HOST}:{PORT}")
while True:
    events = sel.select()
    for key, mask in events:
        if key.data is None:
            conn, addr = key.fileobj.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ, data=addr)
            print("Connected:", addr)
        else:
            sock = key.fileobj
            addr = key.data
            try:
                data = sock.recv(1024)
                if data:
                    sock.sendall(data)  
                else:
                    print("Disconnected:", addr)
                    sel.unregister(sock)
                    sock.close()
            except ConnectionResetError:
                print("Disconnected forcibly:", addr)
                sel.unregister(sock)
                sock.close()