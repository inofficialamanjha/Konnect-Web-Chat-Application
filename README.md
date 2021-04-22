# Konnect-Socket-Programming-based-group-Chat-web-Application

Socket Programming Based Chat Application

## Tutorial Referred for Making this Project

[Tutorial I](https://www.youtube.com/watch?v=MgkldDDFJF4)
[Tutorial II](https://www.youtube.com/watch?v=i824zN0DGIo)

# INTRODUCTION

A socket-programming based chat application is a python-based application that enables two users to exchange data in the form of messages across a network using the socket module. It is able to send and receive messages with ease and does not require any third-party libraries, modules or applications.

A web chat application is a web-based application built using the Flask framework for back-end implementation and JavaScript for front-end Implementation. The application uses SocketIO, a cross-browser JavaScript library that emulates a persistent, bi-directional communication channel between the client and server.

In this project, I have made two applications that can conduct message transfer in the form of a chat room application as long as both sender and receiver are on the same network and responsive to the network, irrespective of the size and distance of nodes.

Every message transfer and for that matter any data transfer on a network must be governed by some set of rules which specify the packet behaviour and many more such parameters. These are called protocols. Both Application uses TCP (Transmission Control Protocol) to be able to send and receive data.

Thus, in this work, I describe my implementation of Client-Server Interactions based on the approach of socket programming. I create Konnect, a web application created on SocketIO with bootstrap front-end using the Flask framework, HTML tags, and a standard Javascript template customized to our liking.

I also show the implementations of client-server connections using sockets in Python, which are capable of handling multiple clients by broadcasting messages between one-another, and show the peer-to-peer communication between a single client-server connection using a simple application built using sockets and the tkinter API.

# METHODOLOGY

## Client-Server Communication over the TCP/IP Protocol

A Client-Server Network is a computer network in which one centralized, powerful computer (the server) is a hub to which many personal computers or workstations (called clients) are connected. The client runs programs and accesses data that is stored on the server.

Clients and servers exchange messages in a request-response messaging pattern. The client sends a request, and the server returns a response. This exchange of messages is an example of inter-process communication. The architecture is referred to as two-tier architecture means that the clients acts as one tier and the server process acts as the other tier.

The TCP/IP Model is the acronym for the Transmission Control Protocol/Internet Protocol model, and consists of four layers:
- Process/Application Layer
- Host-to-Host/Transport Layer
- Internet Layer
- Network Access/Link Layer

The TCP protocol is responsible for end-to-end communication and error-free delivery of data. It is known to provide reliable and error-free communication between end systems. It is a connectionless-oriented protocol, over which call request and call accept packets are used to establish connection. It also has an acknowledgement feature and controls the flow of the data through a flow control mechanism.

IP protocol stands for the Internet protocol and is responsible for delivering packets from source host to the destination host by looking at the IP addresses in the packet header. In our Application we have used IPv4 protocol.


## Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One Socket (or a node) listens to a particular port at an IP address, while another socket reaches out to the other to form a connection.

The server forms the listener socket while the client reaches out to the server. I am using TCP sockets in my project because they are telephonic, connection-oriented, and reliable. They also have an acknowledgement feature and control the flow of the data through a flow control mechanism.

Server Characteristics:
- Waits for a request from one of the clients
- Replies to the client with requested data
- Processes the data, and communicates with other clients or servers.

Client Characteristics:
- Initiates requests to servers.
- Waits for replies.
- Receives replies from the server.

![Socket Programming](https://user-images.githubusercontent.com/75173703/115769458-32be0500-a3c9-11eb-9379-b4ac1bc3970b.PNG)


## Tkinter and Socket Based Chat Application

The Tkinter and Socket Based Chat Application is based on the use of Python sockets and Multithreading to establish a Client-Server Communication. The GUI is implemented using Tkinter Frameworks from the Python standard library.

**Server Architecture for the Chat Application**

I am using TCP Sockets for setting up our server, and therefore - using importing the AF_INET and SOCK_STREAM flags.

The tasks for the servers are broken into accepting new connections, handling and receiving messages from clients and broadcasting those messages to other clients over the chat application. The server-side script uses Multi-threading to receive the bytes transmitted over the socket buffer continuously.

**Client Architecture for the Chat Application**

The architecture of the functioning of the client is broken down into receiving bytes from the socket buffer (i.e. server), and sending messages to the server. The client-side script also uses Multi-threading to receive the bytes transmitted over the socket buffer continuously.


## Konnect Web-Based Chat Application

I have built a web application using sockets, which have been implemented on both the server and the client level, based on Flask-Sockets (for the Back-end Implementation) and SocketIO - JavaScript (for the Front-End Implementation).

**SocketIO**

SocketIO is a cross-browser JavaScript library that abstracts the client application from the actual transport protocol. It is used to ease the communication between client and server and establish a persistent, bi-directional communication channel.

We have incorporated SocketIO in our JavaScript frontend client file - index.html to establish the connection with the server. To put it simply, Socket.IO allows the front-end in our project to interact with the back-end of our project.

**Flask-SocketIO**

Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server. The client-side application can use any of the SocketIO official client libraries in Javascript, C++, Java and Swift, or any compatible client to establish a permanent connection to the server.

It is primarily used for initialization of the server, and for sending, receiving and broadcasting messages to and from clients.

The Flask templates are rendered using Jinja2. The frontend uses JavaScript framework.

![Client-Sever Interaction](https://user-images.githubusercontent.com/75173703/115769461-33569b80-a3c9-11eb-853a-e3793bf6417b.PNG)

![Directory Structure](https://user-images.githubusercontent.com/75173703/115770450-5afa3380-a3ca-11eb-99bf-ee5a01acbca3.PNG)

**Server-Client Communication**

We interact using channels over a web socket connection. When the client sends a message on the connect channel, our connect channel will handle the process.

Index.js implements the client socket code on the front-end:
- Creates a socket connection application and connects to the Server
- Creates a new user and saves details in database
- Emit messages over ‘event’ channel to the server when ‘submit’ event is executed
- Receives messages over ‘message_response’ channel

After Creation of the JavaScript frontend, Socket handler is declared on the Flask Backend server side.

main,py ( main application file ) implements the server socket establishment code:
- Creates a socket based flask application instance using .env files
- Looks for connection
- Emits message ‘message_response’ channel based on the files parsed over the ‘event’ channel.
- Maintains a database with all the message history details.

 **Application Deployment and Testing**

Import flask, SocketIO and SQLite3 modules for python shell.

- Edit the environment file with your host IP address
- Run main.py file over your Operating system Python Shell.
- Login to the Chat application using the following navigation address in your browser: 0.0.0.0:5000. (“0.0.0.0” is the default Host IP address in the .env file).


# CONCLUSION

Successfully created 2 Chatting application, one using Tkinter and the other using Flask framework.

![Tkinter Based Chat Application](https://user-images.githubusercontent.com/75173703/115769454-32256e80-a3c9-11eb-8a62-c7329f9231bd.PNG)

![Konnect I](https://user-images.githubusercontent.com/75173703/115769450-318cd800-a3c9-11eb-870b-b93bff945b9b.PNG)
![Konnect II](https://user-images.githubusercontent.com/75173703/115769450-318cd800-a3c9-11eb-870b-b93bff945b9b.PNG)

Both my Tkinter application and Web application are working as expected, with the web application also communicating between multiple devices on the same network, like between a phone and a computer. Our Tkinter application has a simple, minimalistic UI, while our web application has a clean UI, in line with top chat applications.
