import multiprocessing 
import time 

"""
Un proceso que esta en ejecución puede ser cancelado o interrumpido por medio de la función terminate()
"""


def TareaProceso():
	pactual=multiprocessing.current_process()
	print('Proceso hijo pid {}'.format(pactual.pid))
	time.sleep(5)
	print('Continua la ejecución')


if __name__ == '__main__':

	miproceso = multiprocessing.Process(target = TareaProceso)
	miproceso.start() #Si aplicamos el sleep el hijo se ejecuta, si no este no le da tiempo de actuar 
	#time.sleep(10)
	print('Proceso padre ha terminado, termina el proceso main')
	print('Proceso hijo terminando...')
	miproceso.terminate()
	print('Proceso hijo finaliza con éxito')