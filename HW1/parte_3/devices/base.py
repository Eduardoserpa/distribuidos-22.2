import struct
import socket

import protobuf.gateway_pb2 as gateway_pb2

class BaseDevice():
    def __init__(self,ip_multicast,port_multicast,Nome_Dispositivo,server_ip,server_port):
        MCAST_GRP = ip_multicast
        MCAST_PORT = port_multicast
        self.multicastsocket = socket.socket(socket.AF_INET, 
                                           socket.SOCK_DGRAM)
        self.cast_adress = (MCAST_GRP,
                            MCAST_PORT)
        group = socket.inet_aton(MCAST_GRP)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        
        self.multicastsocket.setsockopt(
                                      socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR,1
                                      )
        
        self.multicastsocket.setsockopt(socket.IPPROTO_IP, 
                                        socket.IP_ADD_MEMBERSHIP,
                                        mreq)

        self.multicastsocket.bind(('',MCAST_PORT))
        
        
        self.ON_OFF =True 
        self.nome = Nome_Dispositivo
        self.server_ip = 'localhost'
        self.server_port = server_port
        
        self.socket = socket.socket(socket.AF_INET, 
                                    socket.SOCK_STREAM)
        try:
            self.TCPConnect()
        except:
            self.MulticastConnect()
        
    def TCPConnect(self):
        self.socket.connect((self.server_ip, self.server_port))
        response = gateway_pb2.DeviceID()
        response.nome = self.nome
        response.ip =   self.server_ip
        response.port = self.server_port
        
        self.socket.send(response.SerializeToString())
    
    def MulticastConnect(self):
        connection_message = self.multicastsocket.recv(1024)
        message = gateway_pb2.GatewayRequest()
        message.ParseFromString(connection_message)
        self.socket.connect((self.server_ip, self.server_port))
        
        response = gateway_pb2.DeviceID()
        response.nome = self.nome
        response.ip =   self.server_ip
        response.port = self.server_port
        
        self.socket.send(response.SerializeToString())
    
    def IsOn(self):
        return self.ON_OFF
