import os
import sys
from zebra import Zebra
#nomer = int(sys.argv[1])
nomer = int(input('nomer: '))
layout = (f"""^XA^FO 10,50^BY2^BCN,50,Y,N,N^FD{nomer}^FS^XZ""")
z = Zebra('ZDesigner ZD410-203dpi ZPL')
z.output(layout)