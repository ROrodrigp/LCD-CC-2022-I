import multiprocessing 
import time 
"""
Con el método cpu_count() se muestra el número de procesadores del sistema que se está utilizando 
"""

print(multiprocessing.cpu_count())

"""
El identificador del proceso actual se accede por medio de current_process()
"""
#PID del proceso actual 
print(multiprocessing.current_process().pid) #Este es el pid del proceso que está invocando al current process



def TareaHijo():
	print('Proceso Hijo con PID: {} '.format(multiprocessing.current_process().pid))
	time.sleep(3)
	print('Fin del proceso hijo')

def main():
	print('Proceso Padre con PID: {} '.format(multiprocessing.current_process().pid))
	miproceso = multiprocessing.Process(target=TareaHijo)
	miproceso.start()
	miproceso.join()

print('Fin del proceso padre')

if __name__ == '__main__':
	main()




