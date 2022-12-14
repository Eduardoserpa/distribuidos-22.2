from gateway import Gateway
from _thread import *
import threading

import protobuf.client_pb2 as client_pb2
import protobuf.gateway_pb2 as gateway_pb2

def add_app_users(gateway):
    while True:
        connection,address=gateway.server_socket_1.accept()
        gateway.client_vector.append(connection)
        
        print("Novo Usuário. Endereço: ", address)
        
        start_new_thread(listen_app_users,(connection,address))

def listen_app_users(connection,address):
    while True:
        messagem=connection.recv(1024)
        user_request = client_pb2.Request_APP()
        user_request.ParseFromString(messagem)
        
        if  user_request.request_type<5 and user_request.request_type!=1:
            client_id = gateway.client_vector.index(connection)
            gateway.send_to_object(user_request,client_id)
        
        if user_request.request_type==7:
                gateway.remove_user(connection)
                connection.close()
                break
        
        if user_request.request_type==1:
            server_response = client_pb2.Response_APP()
            if gateway.sensor_value!='NULL':
                server_response.object_name = user_request.name
                server_response.object_result = gateway.sensor_value
                connection.send(server_response.SerializeToString())
            else:
                client_id = gateway.client_vector.index(connection)
                
                gateway.send_to_object(user_request,client_id)
        
        if user_request.request_type==5:
            server_response = client_pb2.Response_APP()
            server_response.object_name = 'LIST OBJECTS'
            server_response.list_object = str(list(gateway.object_dict.keys()))
            connection.send(server_response.SerializeToString())    
        
        if user_request.request_type==6:
            vector = list(gateway.object_dict.keys())
            if user_request.value not in vector:
                server_response = client_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 0
            else:
                server_response = client_pb2.Response_APP()
                server_response.object_name = 'EXISTS'
                server_response.exists = 1
                
            connection.send(server_response.SerializeToString())
            
def add_device(gateway):
    while True:
        messagem = gateway_pb2.DeviceID()
        connection,address=gateway.server_socket_2.accept()
        messagem.ParseFromString(connection.recv(1024))
        print(f'Novo dispositivo. Endereço: {address}. Nome: {messagem.nome}')
        gateway.object_dict[messagem.nome]=connection   
        start_new_thread(listen_device,(connection,))


def listen_device(connection):
    while True:
        messagem = connection.recv(1024)
        object_response = gateway_pb2.DeviceResponse()
        object_response.ParseFromString(messagem)
        if object_response.sensor_id==1:
            gateway.sensor_value = object_response.result
            
        if object_response.sensor_id==0:    
            i = object_response.client_id
            connection_app = gateway.client_vector[i]
            gateway.send_to_user(connection_app,object_response)


gateway = Gateway('228.0.0.8',50000)

gateway.server_socket_2.bind(('127.0.0.1',65432))
gateway.server_socket_2.listen(1)

gateway.server_socket_1.bind(('127.0.0.1',65433))
gateway.server_socket_1.listen(1)

gateway.find()

t_1 = threading.Thread(target = add_device,args=(gateway,))
t_2 = threading.Thread(target = add_app_users,args=(gateway,))

t_1.start() 
t_2.start()
