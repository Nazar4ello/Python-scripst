import socket                                                                    
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                                                    
host = "192.168.241.105"                                                                    
port = 9100                                                                                                         
                                                                                                                      
try:                                                                                         
  mysocket.connect((host, port)) #connecting to host                                                                        
  for i in range(1):          
      userId = str(i)                                                                              
      layout = (f"""                                                                                  
      ^XA^CI28^PW500^FS                                                                                                           
      ^RW24,26,A2^FS                                                                                                                
      ^RS8,B13,100,1,E^FS                                                                                                           
      ^RB96,8,3,3,24,58^FS                                                                                                           
      ^RFW,E^FD52,0,5,1234567,{userId},^FS        
      ^FN3^RFR,H^FS                                                                                                                    
      ^HV3                                                                                                                             
      ^FWN^FO90, 15^AD,90,22^FDCompanyName^FS                                                                                          
      ^FT90,110^A0N,25,25^FH^FDUSER:{userId},^FS    
       ^FS^XZ                                                                                                                          
      """)                                                                                                               
      mysocket.send(bytes(layout,"utf-8"))                                                    
  mysocket.close () #closing connection                                                                              
except:                                                                            
  print("Error with the connection")      