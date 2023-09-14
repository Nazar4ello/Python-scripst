import os
import socket
from zebra import Zebra
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.241.105"
port = 9100
mysocket.connect((host, port)) #connecting to host

for i in range (0,100):
    nomer = int(input('nomer: '))
    # 1 etiketka
    layout = (f"""^XA^FO 60,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
    z = Zebra('ZDesigner ZD410-203dpi ZPL')
    z.output(layout)
    # 2 etiketka
    nomer = nomer * 10000
    layout = (f"""^XA^FO 60,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
    z.output(layout)
    # 3 etiketka
    layout = (f"""^XA^FO 60,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
    z.output(layout)
    # 4 etiketka
    nomer = nomer + 101
    layout = (f"""^XA^FO 60,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
    z.output(layout)
    # 5,6 etiketka
    nomer = nomer + 102
    try:
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