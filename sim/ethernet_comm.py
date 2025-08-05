# sim/ethernet_comm.py
import socket

def start_server(host="localhost", port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[SERVER] Listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"[SERVER] Connection from {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode().strip()
        print(f"[SERVER] Received: {command}")

        response = f"ACK: {command}"
        conn.sendall(response.encode())

    conn.close()
    print("[SERVER] Connection closed")

def start_client(host="localhost", port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    commands = [
        "START MOTOR 1 SPEED 500",
        "GET STATUS",
        "STOP MOTOR 1"
    ]

    for cmd in commands:
        print(f"[CLIENT] Sending: {cmd}")
        s.sendall(cmd.encode())
        response = s.recv(1024)
        print(f"[CLIENT] Received: {response.decode()}")

    s.close()
    print("[CLIENT] Connection closed")
