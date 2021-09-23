import os 
import multiprocessing as mp
import time


nums_res = []

def calc_cuad(numeros):
	global nums_res
	for n in numeros:
		print("cuadrado: ",n*n)
		nums_res.append(n*n)
	print(nums_res)


if __name__ == '__main__':
	
	nums = range(10)

	t = time.time()

	p1 = mp.Process(target=calc_cuad, args=(nums,))
	p1.start()
	p1.join()


	print('Tiempo de ejecucion', time.time()-t)
	print('Resultado del proceso', nums_res) #Cuando creo procesos no es tan sencillo el compartir variables aunque sean globales 

	print('Finaliza la ejecucion')
