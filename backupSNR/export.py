import telnetlib
from datetime import datetime
import time

current_datetime = datetime.now().date()
filepass = str("D:\Python\/backupSNR\pass.txt")
filesource = str("D:\Python\/backupSNR\source.txt")
print(current_datetime)
#функция чтения из файла
def readfile(par):
    file = open(par)
    onstring = file.read().split("\n")[:-1]
    attrib = dict()
    for item in onstring:
        key = item.split(" ")[0]
        value = item.split(" ")[1:]
        attrib[key] = value
    file.close()
    return (attrib)

#функция нормализации текста
def normal_text(par):
    name = str(par)
    name = name.replace('[', "")
    name = name.replace(']', "")
    name = name.replace("'", "")
    return name
passw_dict = readfile(filepass) #чтение из файла
source_dict = readfile(filesource) #чтение из файла
login = normal_text(passw_dict['username']) #логин
password = normal_text(passw_dict['password']) #пароль
#print(login)
#print(password)
for ip in source_dict:
    path_ftps = 'copy flash:\startup.cfg tftp://192.168.241.88/SNR/'
    name_switch = normal_text(source_dict.get(ip))
    ip_address = ip
#    print(name_switch)
#    print(ip_address)
    path_copy = (str(path_ftps) + name_switch + '/' + str(current_datetime) + '.cfg' + '\n')
    print(path_copy)
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'login:')
    tn.write(login.encode('ascii') + b"\n")
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii') + b"\n")
    tn.read_until(b'#')
    tn.write(path_copy.encode('ascii') + b"\n")
    tn.read_until(b'[Y/N]:')
    tn.write(b'y\n')
    time.sleep(2) #ждем пока, скопируется
    print("done!")