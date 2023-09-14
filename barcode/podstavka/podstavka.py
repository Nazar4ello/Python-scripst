import socket
from zebra import Zebra
nomer = int(input('nomer: '))
# 1 etiketka
layout = (f"""^XA^FO 80,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
z = Zebra('ZDesigner ZD410-203dpi ZPL')
z.output(layout)
