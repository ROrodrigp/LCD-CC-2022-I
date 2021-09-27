import multiprocessing 
import time 


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




