import socket 

IP = socket.gethostbyname(socket.gethostname())
PORT = 4443
ADDR = (IP, PORT)
DISCONNECT_MSG = "DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("Enter a message: ")

        client.send(msg.encode("utf-8"))
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(1024).decode("utf-8")
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()

