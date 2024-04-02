import socket
import threading

def ThreadConn(soc):
    # Accepts a connection request and stores both a socket object and its IP address
    while True:
        try:
            client, addr = soc.accept()
        except:
            print("Error! while accepting the connection incoming. Something is wrong!")
            break
        print("{} has connected to the chat room.".format(addr[0]))
        address[client] = addr
        threading.Thread(target=client_thread, args=(client,)).start()

def client_thread(client):
    # Handles the client
    addr = address[client][0]
    try:
        chat_user = nickname(client)
    except:
        print("Error! during setting the nickname for {}! Something is wrong!".format(addr))
        del address[client]
        client.close()
        return
    print("{} has set the name to {}!".format(addr, chat_user))
    user_list[client] = chat_user
    try:
        client.send("Welcome {}! You are connected to the chat room now!.".format(chat_user).encode("utf8"))
    except:
        print("There is a communication error with {} ({}).".format(addr, chat_user))
        del address[client]
        del user_list[client]
        client.close()
        return
    broadcast_msg("{} has joined the chat room!".format(chat_user))

    # Handles specific messages in a different way (user commands)
    while True:
        try:
            #print("HI")
            message = client.recv(2048).decode("utf8")
            msg_array = message.split()
            if message == "/quit":
                client.send("You left the chat!".encode("utf8"))
                del address[client]
                del user_list[client]
                client.close()
                print("{} has left.".format(chat_user))
                broadcast_msg("{} has left the chat.".format(chat_user))
                break
            elif message == "/users":
                online_Users = ', '.join([chat_user for chat_user in sorted(user_list.values())])
                client.send("Users online are: {}".format(online_Users).encode("utf8"))
            elif message == "/help":
                client.send("/help- gives the help with commands can do".encode("utf8"))
                client.send(
                    "/users-gives the number of clients that are connected to server{}".format('\n').encode("utf8"))
                client.send("/dm User message- Sends direct message to specified user{}".format('\n').encode("utf8"))
                client.send("/bc message- Broadcasts message to all users{}".format('\n').encode("utf8"))
                client.send("/quit-lets the client quit the application".encode("utf8"))
            elif msg_array[0] == "/bc":
                msg_array[0] = ''
                stor = ' '.join(msg_array)
                newstr = eval(stor)
                broadcast_msg(newstr, chat_user)
            elif msg_array[0] == "/dm":
                key_list: list = list(user_list.keys())
                value_list: list = list(user_list.values())
                try:
                  position = value_list.index(msg_array[1])
                  msg_array[0] = ' '
                  msg_array[1] = ' '
                  stre = ' '.join(msg_array)
                  newstre = eval(stre)
                  key_list[position].send("{}:{}".format(chat_user,newstre.strip()).encode("utf"))
                except:
                    print("{} not found".format(msg_array[1]))
            else:
                print("{}: {}".format( chat_user, message))
                broadcast_msg(message, chat_user)
        except:
            print("{} ({}) has left.".format(addr, chat_user))
            del address[client]
            del user_list[client]
            client.close()
            broadcast_msg("{} has left the chat.".format(chat_user))
            break

def nickname(client):
    client.send("Its a successful connection!".encode("utf8"))
    count = threading.active_count() - 2
    username = "User"
    name = username + str(count)
    return name

def broadcast_msg(message, sent_By = ""):
    # Broadcasts a message to all users connected
    try:
        if sent_By == "":
            for chat_user in user_list:
               chat_user.send(message.encode("utf8"))
        else:
            for chat_user in user_list:
                chat_user.send("{}: {}".format(sent_By, message).encode("utf8"))
    except:
        print("Error! during broadcasting a message! Somethig went wrong.")


def main():
    # The host and port for the chat service
    host = "127.0.0.1"
    port = 27000
    # Creates the socket for a TCP application
    socket_Fam = socket.AF_INET
    Type = socket.SOCK_STREAM
    server_Sock = socket.socket(socket_Fam, Type)
    # Binds the serverSocket at the specified port number
    server_Sock.bind((host, port))
    # Enables accepting connections
    server_Sock.listen()
    # Welcome message to the server owner
    print("The server is up and running!")


    # Creates a thread for accepting incoming connections
    conn_Thread = threading.Thread(target=ThreadConn, args=(server_Sock,))
    conn_Thread.start()
    # Waits for it to end
    conn_Thread.join()
    # Performs socket connections cleanup
    # Closes the server socket object connection
    server_Sock.close()
    print(" The server has shut down.")

# Dictionaries of nicknames and addresses with socket object as key
user_list = {}
address = {}

if __name__ == "__main__":
    main()
    pass