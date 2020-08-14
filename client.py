import socket
import threading

nickName = input("Choose your Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickName.encode("ascii"))
            else:
                print(message)
        except:
            print("An error ocurred!")
            client.close()
            break


def write():
    while True:
        message = "{}: {}".format(nickName, input(""))
        client.send(message.encode("ascii"))


receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
