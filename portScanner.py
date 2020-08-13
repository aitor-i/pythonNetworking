import socket
import threading
from queue import Queue

target = "192.168.0.1"
queue = Queue()
openPorts = []


def portScaner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


# for i in range(1, 1022):
#     result = portScaner(i)
#     if result == True:
#         print("Port {} is open".format(i))

#     else:
#         print("port {} is close".format(i))


def fillQueue(portList):
    for port in portList:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portScaner(port):
            print("Port {} is open".format(port))
            openPorts.append(port)


portList = range(1, 1024)
fillQueue(portList)

threadList = []

for t in range(150):
    thread = threading.Thread(target=worker)
    threadList.append(thread)

for thread in threadList:
    thread.start()

for thread in threadList:
    thread.join()


print("open port are: ", openPorts)
