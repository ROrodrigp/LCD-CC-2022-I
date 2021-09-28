from multiprocessing import Process, Pipe

def worker(conn):
    print(conn.recv())
    time.sleep(1.8)
    conn.send("sent from child process")
    conn.close()

conn1, conn2 = multiprocessing.Pipe() #Devuelve dos objetos, la conexión del padre al hijo y la conexión del hijo al padre
process = multiprocessing.Process(target=worker, args=(conn2,))
process.start()

conn1.send("sent from main process")
print(conn1.recv())
process.join()
