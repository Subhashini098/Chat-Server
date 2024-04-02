import sys
import socket
import datetime
import threading


def send(soc):
    # Handles sending messages to the server
    while flagThread:
        try:
            msg = input()
            #deleteLastLine()
            soc.send(msg.encode("utf8"))
        except:
            print("Encountered an error when while trying to send a message!")
            break

def receive(soc):
    # Handles receiving messages from the server
    while flagThread:
        try:
            msg = soc.recv(2048).decode()
            if msg:
                print("{}".format(msg))
            else:
                # When the server closes the socket, messages received are empty
                break
        except:
            print("Encountered an error when trying to reach the server!")
            break

def main():
    # main() will refer to threadFlag as to the global variable defined globally
    global flagThread
    # The host and port of the chat server
    print("Enter server's IP address")  #127.0.0.1
    host = input()
    port = 27000
    # Creates the socket for a TCP application
    socket_Fam = socket.AF_INET
    Type = socket.SOCK_STREAM
    client_Sock = socket.socket(socket_Fam, Type)
    # Connects to the server
    client_Sock.connect((host, port))
    # Creates two threads for sending and receiving messages from the server
    sending_Thread = threading.Thread(target=send, args=(client_Sock,))
    receiving_Thread = threading.Thread(target=receive, args=(client_Sock,))
    # Start those threads
    receiving_Thread.start()
    sending_Thread.start()
    # Checks if both threads are alive for handling their termination
    while receiving_Thread.is_alive() and sending_Thread.is_alive():
        continue
    flagThread = False
    # Finally closes the socket object connection
    client_Sock.close()
    print("\nThe application can be closed now.")

# Flag used for threads termination
flagThread = True

if __name__ == "__main__":
    main()
    pass