from socket import *
from time import ctime
import argparse

HOST = ''
PORT = 666
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpServerSock = socket(AF_INET, SOCK_STREAM)
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)

while True:
	print('Waiting for connection...')
	tcpClientSock, addr = tcpServerSock.accept()
	print('...connected from:', addr)

	while True:
		data = tcpClientSock.recv(BUFFSIZE)
		if not data:
			break
		tcpClientSock.send('[%s] %s' % (ctime(), data))

	tcpClientSock.close()
tcpServerSock.close()
