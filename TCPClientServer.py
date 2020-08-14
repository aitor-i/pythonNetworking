import threading
import socket

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nickNames = []


def broadCast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadCast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickName = nickNames[index]
            broadCast("{nickName} left the chat".encode("ascii"))
            nickNames.remove(nickName)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickName = client.recv(1024).decode("ascii")

        nickNames.append(nickName)
        clients.append(client)

        print(f"Nickname of the client is {nickName}|")
        broadCast(f"{nickName} joined the chat".encode("ascii"))
        client.send("Connected to the server".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print("Server is listening...")

receive()
