import socket
import threading
import Pachet

packet = b'\x40\x01\x04\xD2' + b'\xFF' + \
    b'{"action":"discover","device":"client1"}'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

Server_Ip = socket.gethostbyname(socket.gethostname()) #ia ip-ul hostului, in cazul dat laptopul personal
Server_Port = 5683 # portul predestinat unencrypted CoAP

Socket_Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # setez la transmitere prin UDP
Socket_Server.bind(("0.0.0.0", Server_Port)) # Atasez portul de coap pentru server

client.sendto(packet,("255.255.255.255", Server_Port))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(Server_Ip)

    while True:
        data,addr = Socket_Server.recvfrom(1024)
        header, payload = Pachet.parse_packet(data)
        print("header:",header)
        print("payload:",payload)

