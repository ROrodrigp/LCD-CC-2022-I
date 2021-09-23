import multiprocessing as mp 
import time 	


	

def calc_cuad(numeros,val):
	for idx, n in enumerate(numeros):
			#result.append(n*n)	
		result[idx] = n * n 
	print('Resultado del proceso', result[:])



result = mp.Array('i',10)
nums = range(10)
t = time.time()
	#val = mp.Value('d',0.0)

if __name__ == '__main__':
	
	p1 = mp.Process(target=calc_cuad, args=(nums,result))
	p1.start()
	p1.join()

		#print('Resultado fuera del proceso ',val.value)
	print('Resultado fuera del proceso ', result[:])	#Puedo ver result desde el padre?


	print('Tiempo de ejecución ', time.time()-t)
	print('Finaliza ejecución')







