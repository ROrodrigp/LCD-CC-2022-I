import os 
from multiprocessing import Process 

"""
print('module name: ', __name__)
print('parent process: ',os.getppid())
print('process id: ',os.getpid())
"""




def info(titulo):
	print(titulo)
	print('module name: ', __name__)
	print('parent process: ',os.getppid())
	print('process id: ',os.getpid())

def f(nombre):
	info('function f')
	print('hello', nombre)
	print('---------')


if __name__ == '__main__':
	
	info('Primera linea') #Proceso padre 
	p = Process(target=f, args=('Rodrigo',)) #El padre llama a otro proceso para que ejecute la función f 
	p.start()
	p.join()
