import socket               # Import socket module
import threading

HEADER = 64
PORT = 5050                # Reserve a port for your service.
HOST = socket.gethostname() # Get local machine name
SERVER = socket.gethostbyname(socket.gethostname()) # Get local machine name
# SERVER = "0.0.0.0" #public IP
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT" 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Bind to the port
server.bind(ADDR)

def handle_client(conn, addr):
   print(f"[NEW CONNECTION] {addr} connected.")

   connected = True
   while connected:
      msg_length = conn.recv(HEADER).decode(FORMAT)
      if msg_length:
         msg_length = int(msg_length)
         msg = conn.recv(msg_length).decode(FORMAT)
         if msg == DISCONNECT_MESSAGE:
            connected = False

         print(f"[{addr}] {msg}")
         conn.send("Msg received".encode(FORMAT))

   conn.close()                # Close the connection

def start():
   server.listen()
   print(f"[LISTENING] Server is listening on {SERVER}")
   while True:
      conn, addr = server.accept()
      thread =  threading.Thread(target = handle_client, args = (conn, addr))
      thread.start()
      print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

print("[STARTING] server is starting...")
start()

# server.listen(5)                 # Now wait for client connection.
# while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print('Got connection from', addr)
#    c.send('Thank you for connecting')
#    c.close()                # Close the connection

