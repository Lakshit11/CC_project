# Introduction:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Chatrooms allow team members to communicate in real-time, share files, and collaborate more effectively. With the rise of remote work, chatrooms have become even more essential 
for teams to communicate and collaborate efficiently. Python, a high-level programming language, has become a popular choice for building chatrooms due to its simplicity, scalability,
and wide range of libraries and frameworks. 
In this project, we have developed a private organization chatroom using Python. The chatroom is designed to support secure and real time messaging among members of a private 
organization, with features such as message saving (only on server side), message forwarding. The chatroom is built using WebSocket technology, multithreading concept and port 
message forwarding to provide real-time messaging. For backend we use Comma Separated Values File (CSV) to store credentials and use panda’s library of Python to manipulate 
this CSV file.
 
One of the main advantages of using Python for building a private organization chatroom is its simplicity and ease of use. Python is known for its readability and concise syntax, 
making it easy to write and maintain code. Additionally, Python has a wide range of libraries and frameworks that can be used to build complex applications quickly and efficiently. 
This makes it an ideal choice for building a chatroom that requires real-time messaging and secure communication. 

In summary, we have implemented private organization chatroom using Python, which is a secure and efficient platform for team members to communicate and collaborate. 
Using WebSocket technology, the chatroom provides real-time messaging. With Python's simplicity, scalability, and wide range of libraries and frameworks, the chatroom can be easily
scaled up to handle a growing number of users and messages.

# Technologies used:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Chatroom is built using Python Programming language and its libraries. The libraries that were used in the project are as follows: 

1. socket – The library that helps in socket programming. 
2. time – The library will be used by server to store the logs of messages at what time the messages were sent. 
3. csv – Basic library that is used for writing data into CSV files. 
4. subprocess and os– Used for opening the viewing of chats window when client script is executed. The os library is used for exiting the command prompt window upon disconnecting 
5. pandas – The file is used in the script where we display the chats of the room on each client machine. 

The application is built using python programming and successfully runs on command line interface. Initially, the application was built to create clients on localhost that is we were
able to create clients on machines that are connected to router which in turn is connected to the server machine. 
Once the application was performing as needed on the localhost, we decided to use public IP address generated by the private organization so that the application is not just limited to 
local machines.  After we get IP address, we deployed the project on Linode and made the project working based on that public IP address. 

 # Working of the project:
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The execution of the project starts with client sending a particular message by running the client.py file and then the message is received at the server, which stores the message into 
messages.csv file and then this file distributes the messages to all the active clients. 

The working of application is made possible by using TCP/IP protocol that simply forwards the data in the form of packets and streams. The application also uses the concept of 
multi-threading. Multi-threading is here used to create threads whenever a new user is connected to the server. With the help of multi-threading, the load on the server is extremely 
reduced and the application becomes cost-effective as well. There is also a concept of port forwarding where we specify a particular port in the code and then the machine will know 
which port to use to send and receive messages. 

The working of application with respect to code can be explained as follows: 
There are total 4 python files they are server.py, client.py, list_messages.py and message_logs.py. Each file serves the purpose as the name suggests. The CSV files used are messages.csv 
used to store the messages and data.csv that stores client’s IP address, their thread number and name of client. 

# Actual Working: 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. We run server.py file and then the server starts. 
2. After that, when clients are created by running client.py file, server is prompted with their IP address and corresponding thread number and with messages if any. 
3. The client then can interact with the other employees by sending messages and those messages will be delivered in real-time. 
4. The list_messages.py file can be thought of as an GUI file where the messages will be in a proper human readable format. 
5. message_logs.py file is used to simply display logs of the messages in the backend of every device so that we can see what is happening. 

Every time a client is created, the system creates a thread and assigns a unique thread number to that user. With the help of multithreading, the load on the system gets reduced and 
the server can be used more efficiently.

# Implementation and deployment :
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The application is implemented by using an online cloud service provider known as Linode. Linode is a cloud hosting provider that offers virtual private servers, managed Kubernetes 
services, and other cloud infrastructure services. It provides a reliable and secure platform for hosting websites, applications, and databases. With datacentres located in different regions
around the world, Linode offers low-latency connectivity to users and a high degree of flexibility and scalability for businesses.
The reason Linode is used is for getting public IP address so that the application is just not limited to local network. The process of getting public IP was simple. We just have to create 
linode account, pay for the services we are thinking of using and that is it.
After getting the public IP, we just SSH into the VM instance by using IP address using Putty. Then we login as root user and create a new file called server.py and simply put all the 
server-side code in that file (with Public IP address where address is to be specified).
Then we run the server.py file on the server and our server starts and clients could connect with that server for messaging.
Upon performing all the necessary steps of setting up server and creating clients, the application runs successfully and can transfer message with ease.
