import socket
import socketserver


class Server:
    sock = socket()  # Sockets power the cloud
    TCPserver = socketserver.TCPServer  # Gotta host the game

    def initiate(self):  # Called on startup
        print("Server initialized")
        # self.TCPserver.
        # menu()
        pass

    def settings(self):  # User wants control
        userInput = input("Host Server(1)\nClose server(2)\nExit(0)")

        # Adjust so they can't write anything but what's asked
        # while userInput.type != int:
        try:
            userInput = int(userInput)
        except:
            print("Try again")  #

        # if userInput =

    def status(self):
        return
        # self.TCPserver.


class Client:
    sock = socket()

    def initiate(self):
        return
        # self.sock.
