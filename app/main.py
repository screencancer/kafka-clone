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

def message_init(msg, correlation_id, api_ver, api_key, error_code):
    
    msg_size = msg.to_bytes(4, byteorder="big", signed=True)
    cid = correlation_id.to_bytes(4, byteorder="big")
    error_code = error_code.to_bytes(4, byteorder="big")
    #key = api_key.to_bytes(4, byteorder="big")

    
    #To get find offset
    #corr_id = correlation_id.to_bytes(4, byteorder="big", signed=True)
    return(msg_size+cid + error_code)

def client_handling(client):
    request = client.recv(1024)

    cid_bytes = int.from_bytes(request[8:12], byteorder="big", signed=True)
    api_ver = int.from_bytes(request[6:8], byteorder="big", signed=True)
    api_key = int.from_bytes(request[4:6])
    error_code = 0
    print(api_ver)
    if api_ver not in [range(5)]:
        print(api_ver)
        api_ver=4
        error_code = 35

    client.sendall(message_init(0,cid_bytes, api_ver, api_key, error_code))
    client.close


if __name__ == "__main__":
    main()
