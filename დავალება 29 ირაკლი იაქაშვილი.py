# მოიძიე ინტერნეტში, გაუშვი და დააკომენტარე ჩათის კოდი,
# რომელიც ფუნქციონირებს არა TCP_ის, არამედ UDP_ის გამოყენებით.

# Importing necessary libraries
import socket  # For socket programming
import threading  # For concurrent execution
import queue  # For implementing a queue
import sys  # For system-specific parameters and functions
import random  # For generating random numbers
import os  # For interacting with the operating system

# Client Code
def ReceiveData(sock):
    # Function to receive data from the socket
    while True:
        try:
            # Receive data from the socket
            data, addr = sock.recvfrom(1024)
            # Decode and print the received data
            print(data.decode('utf-8'))
        except:
            pass

def RunClient(serverIP):
    # Function to run the client
    host = socket.gethostbyname(socket.gethostname())  # Get the host IP address
    port = random.randint(6000, 10000)  # Generate a random port number
    print('Client IP->' + str(host) + ' Port->' + str(port))
    server = (str(serverIP), 5000)  # Server address and port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
    s.bind((host, port))  # Bind the socket to the host and port

    name = input('Please write your name here: ')  # Get user's name
    if name == '':  # If name is empty
        name = 'Guest' + str(random.randint(1000, 9999))  # Generate a guest name
        print('Your name is:' + name)
    s.sendto(name.encode('utf-8'), server)  # Send user's name to the server
    threading.Thread(target=ReceiveData, args=(s,)).start()  # Start a thread to receive data

    while True:
        data = input()  # Get user input
        if data == 'qqq':  # If input is 'qqq'
            break
        elif data == '':  # If input is empty
            continue
        data = '[' + name + ']' + '->' + data  # Format user's message
        s.sendto(data.encode('utf-8'), server)  # Send data to the server
    s.sendto(data.encode('utf-8'), server)  # Send final data to the server
    s.close()  # Close the socket
    os._exit(1)  # Exit the program

# Server Code
def RecvData(sock, recvPackets):
    # Function to receive data packets
    while True:
        data, addr = sock.recvfrom(1024)  # Receive data from the socket
        recvPackets.put((data, addr))  # Put the received data in the queue

def RunServer():
    # Function to run the server
    host = socket.gethostbyname(socket.gethostname())  # Get the host IP address
    port = 5000  # Server port number
    print('Server hosting on IP-> ' + str(host))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
    s.bind((host, port))  # Bind the socket to the host and port
    clients = set()  # Set to store client addresses
    recvPackets = queue.Queue()  # Queue to hold received packets

    print('Server Running...')

    threading.Thread(target=RecvData, args=(s, recvPackets)).start()  # Start a thread to receive data

    while True:
        while not recvPackets.empty():
            data, addr = recvPackets.get()  # Get data from the queue
            if addr not in clients:  # If client address is not in the set
                clients.add(addr)  # Add client address to the set
                continue
            clients.add(addr)  # Add client address to the set
            data = data.decode('utf-8')  # Decode the received data
            if data.endswith('qqq'):  # If data ends with 'qqq'
                clients.remove(addr)  # Remove client address from the set
                continue
            print(str(addr) + data)  # Print received data with client address
            for c in clients:
                if c != addr:
                    s.sendto(data.encode('utf-8'), c)  # Send data to other clients
    s.close()  # Close the socket

if __name__ == '__main__':
    # Check command-line arguments to determine whether to run as server or client
    if len(sys.argv) == 1:
        RunServer()  # Run as server
    elif len(sys.argv) == 2:
        RunClient(sys.argv[1])  # Run as client with server IP provided
    else:
        print('Run Server:-> python Chat.py')  # Provide instructions for running the server
        print('Run Client:-> python Chat.py <ServerIP>')  # Provide instructions for running the client
