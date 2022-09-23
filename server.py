''' 
CODE : ANISH M
'''

import socket 
import threading

class server(object):
    port = 5050
    server_ip = socket.gethostbyname(socket.gethostname())
    HEADER=64
    FORMAT = 'utf-8'
    addr_server = (server_ip,port)
    dis_con = "!dis_conserver"
    ser_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    ser_sock.bind(addr_server)
    
    def __init__(self,port=port,HEADER =HEADER,FORMAT=FORMAT,ip=server_ip,soc=ser_sock,dis_con=dis_con,addr=addr_server):

        self.port = port
        self.ip = ip
        self.HEADER=HEADER
        self.FORMAT = FORMAT
        self.addr_server = addr
        self.sock = soc 
        self.dis_con = dis_con
        
    @property
    def start(self):
       
        self.sock.listen()
        while True:
            conn,client_addr = self.sock.accept()
            client_thread = threading.Thread(target=self.handle_client,args=(conn,client_addr))
            client_thread.start()
            count=threading.active_count()
            print(f'active connection are : {int(count)-1}')
    
    def handle_client(self,conn,client_addr):
        print(f" new connection ip : {conn} connected")
        connected = True
        while connected :
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(self.FORMAT)
            if msg == self.dis_con:
                connected =False
            print(f"[{conn}] {msg}")
            conn.send("Msg received".encode(self.FORMAT))

        conn.close()
            

if __name__ == '__main__':
    anish=server()
    print('starting server')
    anish.start

 
 
