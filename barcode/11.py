import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.241.105"
port = 9100
nomer = int(input('nomer: '))
print(nomer)
#i = 0
try:
	mysocket.connect((host, port)) #connecting to host
	for nomer in range(nomer,nomer+1):
        layout = (f"""
        ^XA
		^FO 0,50
		^BY3
		^BCN,150,Y,N,N
		^FD{nomer}^FS
		^XZ""")
		mysocket.send(bytes(layout,"utf-8"))
        print(nomer)
	mysocket.close () #closing connection
except:
	print("Error with the connection")