import socket  # noqa: F401
import sys

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client, _ = server.accept() # wait for client

    client.recv(1024)

    message_size = 0
    correlation_id = 7
    
    client.sendall(message_size.to_bytes(4, byteorder="big", signed=True))
    client.sendall(message_size.to_bytes(4, byteorder="big", signed=True))
    
    client.close
    server.close




if __name__ == "__main__":
    main()
