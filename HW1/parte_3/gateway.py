import socket
import struct
import sys

import protobuf.gateway_pb2 as gateway_pb2
import protobuf.client_pb2 as client_pb2

class Gateway():
    def __init__(self,ip_multicast,port_multicast):
        MCAST_GRP = ip_multicast
        MCAST_PORT = port_multicast
        
        self.multicastsocket = socket.socket(
                                           socket.AF_INET, 
                                           socket.SOCK_DGRAM
                                           )
        self.multicastsocket.setsockopt(
                                      socket.SOL_SOCKET, 
                                      socket.SO_REUSEADDR,2 
                                      )
        
        self.cast_address = (MCAST_GRP,
                            MCAST_PORT)
        
        self.server_socket_1 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)
        
        self.server_socket_2 = socket.socket(socket.AF_INET, 
                                             socket.SOCK_STREAM)

        self.client_vector = []
        self.object_dict = {}
        self.sensor_value = 'NULL'
    
    def send_to_object(self,message,client_id):
        server_request = gateway_pb2.GatewayRequest()
        
        connection = self.object_dict[f'{message.name}']
        server_request.aux =message.aux
        server_request.request_type = message.request_type
        server_request.value = message.value
        server_request.client_id = client_id
        
        connection.send(server_request.SerializeToString())
    def remove_user(self,connection_user):
        for i in range(len(self.client_vector)):
            if self.client_vector[i]==connection_user:
                self.client_vector.pop(i)
    
    def send_to_user(self,connection,message):
        server_response = client_pb2.Response_APP()
        server_response.object_name = message.name
        server_response.object_result = message.result
        server_response.object_status = message.object_status
        if message.object_commands!=[]:
            server_response.object_commands[:] = message.object_commands
        connection.send(server_response.SerializeToString()) 
        
    def find(self):
        message = gateway_pb2.GatewayRequest()
        self.multicastsocket.sendto(
                                 message.SerializeToString(), 
                                 self.cast_address
                                )
