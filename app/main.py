import socket  # noqa: F401
import sys

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client, address = server.accept() # wait for client

    client_handling(client)
    
    
    
    
    server.close

def message_init(msg, correlation_id):
    msg_size = msg.to_bytes(4, byteorder="big", signed=True)
    cid = correlation_id.to_bytes(4, byteorder="big")
    #To get find offset
    #corr_id = correlation_id.to_bytes(4, byteorder="big", signed=True)
    return(msg_size+cid)

def client_handling(client):
    request = client.recv(1024)
    response = int.from_bytes(request[8:12], byteorder="big")
    client.sendall(message_init(0,response))
    client.close


if __name__ == "__main__":
    main()
