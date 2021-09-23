##COMUNICACION ENTRE PROCESOS##
"""
La principal forma de comunicación entre procesos se lleva a cabo por medio 
de tuberias y colas, entre diferentes procesos. Especificamente brindan opciones de 
transmision de mensajes para facilitar la comuniacion ente procesos: 
Tuberías para conexiones entre dos procesos y colas para múltiples productores y consumidores

Veremos el uso de colas, especificamente la clase Queue del módulo multiprocessing
La implementación de la clasae Queue es segura para subprocesos y procesos 


Se prefiere el uso de las colas de mensjaes para la comunicación entre los procesos en
lugar de compartir recursos ya que si ciertos procesos manejan mal la memoria y la corrompen 
habrá numerosos elementos indeseables y consecuencias impredecibles.
Sin embargo si un proceso no puede manejar su mensaje correctamente otros elementos de la cola 
permanecerán intactos 

Para manejar el objeto 	Queue necesitamos usar dos métodos principales:

-get() regresa el siguiente item de la cola
-put() agrega un item a la cola 
"""

from multiprocessing import Process, Queue 

def worker(num, q): #Recibe dos parámetros, num es un dato numérico y q es una cola 
	print('Se pone en la cola',num*num) 
	q.put(num*num) #Escribe en la cola la multiplicación del valor numérico 

def worker2(num, q):
	print('Se pone en la cola', num+num)
	q.put(num + num )

def worker3(num, q):
	print('Se pone en la cola', num )
	q.put(num)

if __name__ == '__main__':
	#Hago una cola de nombre my_queue
	my_queue = Queue()
	#La envio como argumento hacia la función worker junto con el valor entero 5
	p1 = Process(target=worker, args=(2,my_queue))
	p2 = Process(target=worker2, args=(3,my_queue))
	p3 = Process(target=worker3, args=(5,my_queue))


	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()

	print('Se lee de la cola', my_queue.get())

	print('Se lee de la cola', my_queue.get())

	print('Se lee de la cola', my_queue.get())

	print('Se lee de la cola', my_queue.get())


#3 procesos que cada uno hace un calculo y lo ingresan a la cola y el proceso padre los lee 

