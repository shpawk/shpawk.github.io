import socket
import threading

# Config
HOST = '127.0.0.1'
PORT = 5000

# Ask for username
username = input("Enter your username: ")

# Incoming Messages function


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[Server disconnected]")
                break
            print("\nServer:", data.decode())
        except:
            print("[Error receiving data]")
            break


# Create and connect to socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("Failed to connect to server :(")
    exit()

# Start receiving thread
recv_thread = threading.Thread(
    target=receive_messages,
    args=(client_socket,),
    daemon=True  # Exits when main thread exits
)
recv_thread.start()

# Instructions
print("Connected to k-chat. Type messages to send.")
print("Type message to send. Type 'exit' to quit.")

# Message sending loop
while True:
    msg = input("> ")
    if msg.lower() == "exit":
        break
    # Send message prefixed with username
    full_msg = f"{username}: {msg}"
    try:
        client_socket.sendall(full_msg.encode('utf-8'))
    except BrokenPipeError:
        print("Connection lost.")
        break

# Clean shutdown
client_socket.close()
print("Disconnected.")
