"""
Es posible asignar un nombre a un proceso hijo que ha sido creado, por medio del argumento name se asigna el nombre del proceso hijo
"""

import multiprocessing 
import time 

def miproceso():
	print('Proceso con nombre {} y pid: {}'.format(multiprocessing.current_process().name,multiprocessing.current_process().pid))

def main():
	print('Pid del padre: ',multiprocessing.current_process().pid)
	phijo1 = multiprocessing.Process(target=miproceso, name='Proceso_1')
	phijo2 = multiprocessing.Process(target=miproceso, name='Proceso_2')
	phijo3 = multiprocessing.Process(target=miproceso, name='Proceso_3')
	phijo1.start()
	phijo2.start()
	phijo3.start()
	phijo1.join()
	phijo2.join()
	phijo3.join()

if __name__ == '__main__':
	main()


#Ejercicio Crea tres procesos con onmbre, cada proceso escribirá su nombre, su pid y el pid del padre