import socket  # noqa: F401
import sys

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    server.accept() # wait for client

    message_size = 000000000
    correlation_id = 00000007
    

    
    #server.bind(9092)
    #server.listen(5)




if __name__ == "__main__":
    main()
