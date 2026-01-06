import socket
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind("/run/p-linux-ai.sock")

while True:
    data = sock.recv(4096)
    event = json.loads(data.decode())

    if event["action"] == "remove":
        print("Dispositivo removido.")