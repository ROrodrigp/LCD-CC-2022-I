from multiprocessing import Process, Pipe

nombres = ["Carlos", "Renata", "Rebeca", "Sandra", "END"]

def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
    conn.close()
    
def recv_msgs(conn):
    
    while 1: #Necesitamos iterar sobre el arreglo
        msg = conn.recv()
        if msg == "END":
            break
        print(msg)
        
parent_conn, child_conn = Pipe() #Conexión del padre y conexión del hijo 

p1 = Process(target=send_msgs, args=(parent_conn, nombres)) #Proceso que envía el arreglo con nombres 
p2 = Process(target=recv_msgs, args=(child_conn,))

p1.start()
p2.start()

p1.join()
p2.join()