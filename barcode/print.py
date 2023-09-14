import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.241.105"
port = 9100
mysocket.connect((host, port)) #connecting to host
for i in range (0,100):
    try:
        nomer = int(input('nomer: '))
        for nomer in range(nomer,(nomer+2)):
            layout = (f"""
            ^XA
            ^FO 0,50
            ^BY3
            ^BCN,150,Y,N,N
            ^FD{nomer}^FS
            ^XZ""")
            mysocket.send(bytes(layout,"utf-8"))
    except:
        print("Error with the connection")
mysocket.close () #closing connection