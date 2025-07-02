import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"[+] Server listening on {HOST}:{PORT}")

# Broadcast to clients


clients = []  # Store all connected client sockets


def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:  # Optional don't echo back to sender
            try:
                client.sendall(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Handle single client


def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    clients.append(client_socket)  # Add client to list

    try:
        while True:
            data = client_socket.recv(1024)  # <-- typo fixed: .rev -> .recv
            if not data:
                break
            print(f"[{address}] says:", data.decode())
            # Send message to others
            broadcast(data, sender_socket=client_socket)
    except Exception as e:
        print(f"[!] Error with {address}: {e}")
    finally:
        print(f"[-] {address} disconnected")
        client_socket.close()
        if client_socket in clients:
            clients.remove(client_socket)  # Cleanly remove on disconnect


while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client,
                              args=(client_socket, client_address))
    thread.start()
