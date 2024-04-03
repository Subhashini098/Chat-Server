# Chat-Server

TCP/IP protocol is used for socket communication. I am working on server client communication. A server has a bind () method that connects it
to a specific IP address and port so that it can listen for incoming requests on that address and
port. Following that, a server has a listen () method that puts the server in listen mode. This
enables the server to monitor incoming connections. Finally, a server has accept () and close ()
methods. The accept method establishes a connection with the client, and the close method
terminates the connection. Next, we are building client that can connect to server. The socket.
connect (hostname, port) method establishes a TCP connection to hostname on port. Once a
socket is open, you can read from it just like any other IO object. 


##  Client-Server communication architecture ##

Implemented a multi-threaded server that accepts multiple client connections and
multithreading is also implemented in the client side to send and receive messages.
A thread is a set of such operations within a program that can run independently of other
programs. A multithreaded program is made up of two or more components that can execute at
the same time. Each component of such a program is referred to as a thread, and each thread
defines a distinct route of execution. A Multithreaded Socket Server may connect with more than
one client in the same network at the same time, as defined by Multithreaded Socket
Programming.
## The Commands ##
### 1.User command (Syntax- /users) ###
This command requests list of users who are currently active from server and then it prints out
their names
### 2.Help command (Syntax-/help) ###
This command prints out list of all supported commands and their behaviors
### 3.Quit command (Syntax-/quit) ###
It disconnects clients from the server. Before disconnecting, it sends message to the server that
the client is disconnecting.
### 4.Direct message command (Syntax-/dm username “message”) ###
This command sends the message between quotes to the specified user.
### 5.Broadcast command (Syntax-/bc “message”) ###
This command sends message between quotes to all other connected users.When a client disconnects without using /quit command, all the connected users get the message
that the specified user lost its connection.

<img width="693" alt="Screen Shot 2022-04-29 at 11 10 31 AM" src="https://github.com/Subhashini098/Chat-Server/assets/109629881/ce55b643-05a2-446e-ad24-941fe427aa22">

