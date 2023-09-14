import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.241.105"
port = 9100
kol = input('ведите количество этикеток: ')               
try:
	mysocket.connect((host, port)) #connecting to host
	for i in range(kol):
		layout = (f"""
		^XA
		^FO 0,50
		^BY3
		^BCN,150,Y,N,N
		^FD123456789123^FS
		^XZ""")
        mysocket.send(bytes(layout,"utf-8"))
        mysocket.close () #closing connection
except:
	print("Error with the connection")      