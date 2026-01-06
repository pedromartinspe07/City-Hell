import pyudev
import json
import socket

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='power')

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.connect("/run/p-linux-ai.sock")

for device in monitor:
    event = {
        "type": "hardware",
        "action": device.action,
        "device": device.sys_name
    }
    sock.send(json.dumps(event).encode())