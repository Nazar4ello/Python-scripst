import socket                                                                    
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                                                    
host = "192.168.241.105"                                                                    
port = 9100                                                                                                         
                                                                                                                      
try:                                                                                         
  mysocket.connect((host, port)) #connecting to host                                                                        
          
                                                                          
  layout = (f"""
  ^XA
  ^FO 0,10
  ^GB632,0,2^FS
  ^FO0,25
  ^FB632,1,0,C,0
  ^ASN,70,70
  ^FDWAR INC.^FS
  ^FO0,100
  ^GB632,0,2^FS
  ^FO0,120
  ^FB632,1,0,C,0
  ^ASN,60,60
  ^FDGoose^FS
  ^FO0,180
  ^FB632,1,0,C,0
  ^ASN,60,60
  ^FDWild^FS
  ^FO0,240
  ^GB632,0,2^FS
  ^FO120,260
  ^BY2
  ^BCN,70,N,N,N
  ^FD123456789123^FS - 
  ^XZ""")                                                                                                               
  mysocket.send(bytes(layout,"utf-8"))                                                    
  mysocket.close () #closing connection                                                                              
except:                                                                            
  print("Error with the connection")      