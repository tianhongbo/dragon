# Echo client program
import socket

# The IPv4 Address of OpenStack Controller node
HOST = '10.145.90.128'

# The Port of Quantum API
PORT = 9696

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print 'Connecting to OpenStack Controller...'
s.sendall('Hello, world')
data = s.recv(1024)
print 'sending data to Quantum Server...'
s.close()
print 'Received', repr(data)
