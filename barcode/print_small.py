import os
from PIL import Image
from os import startfile
import zpl

l = zpl.Label(100,60)
height = 0
l.origin(22, height)
l.write_barcode(height=70, barcode_type='U', check_digit='Y')
l.write_text('07000002198')
l.endorigin()
print(l.dumpZPL())
#l.preview()
#os.startfile(l.dumpZPL(), "print")
f = open('xyz.zpl','w')  # открытие в режиме записи
f.write(l.dumpZPL())  # запись Hello World в файл
f.close()  # закрытие файла
os.startfile('xyz.zpl', "print")