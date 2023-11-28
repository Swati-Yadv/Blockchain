import socket 
import threading 

IP = socket.gethostbyname(socket.gethostname())
PORT = 4443
ADDR = (IP, PORT)
DISCONNECT_MSG = "DISCONNECT"

def handle_client(conn, addr):
    print(f"New connection {addr} connected.\n")
    connected = True
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        print(f"Message received from [{addr}] :- {msg}")
        msg = msg.upper()
        if msg == DISCONNECT_MSG:
            print(msg)
            connected = False
        print(f"Message sent to [{addr}] :- {msg}")

        msg = f"Msg received: {msg}"
        conn.send(msg.encode("utf-8"))

    conn.close()

def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening on {IP}: {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()