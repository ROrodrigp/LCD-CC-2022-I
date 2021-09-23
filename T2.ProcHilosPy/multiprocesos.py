
###MULTIPROCESSING CON PYTHON ###
"""
Multiprocessing es un paquete de Python que permite la 
creación de procesos y ofrece concurrencia local 
Una manera sencilla de crear un proceso es por medio de la construcción 
de un objeto tipo Process e invocarlo por medio del método start
"""

import multiprocessing as mp
import time

"""
def tarea(cadena):
	print('Hola ',cadena)

if __name__ == '__main__': #Revisa si se esta invocando al programa principal
	p = mp.Process(target = tarea, args=('Rodrigo',))
	p.start() 
	p.join()
"""



#Ejemplo 2 
def calc_cuad(numeros):
	print("Calcula el cuadrado de los números")
	for n in numeros:
		time.sleep(0.5)
		print("cuadrado: ",n*n)

def calc_cubo(numeros):
	print("Calcula el cubo de los números")
	for n in numeros:
		time.sleep(0.5)
		print("Cubo: ", n*n*n)

	
if __name__ == '__main__':

	nums = range(100)
	#Process necesita dos argumentos
	#El target que es lo que va a hacer 
	#y los argumentos
	"""
	t1 = time.time()
	calc_cuad(nums)
	calc_cubo(nums)
	print("Tiempo de ejecución", time.time()-t1)
	"""


	t = time.time()
	p1 = mp.Process(target = calc_cuad, args =(nums,))
	p2 = mp.Process(target = calc_cubo, args = (nums,))
	p1.start() #Salida por terminal concurrente
	p2.start()
	p1.join()
	p2.join()




	print("Tiempo de ejecución", time.time()-t)
	print("Termina la ejecución numérica de ambos procesos")


#Ejemplo 3 
#Crea otro proceso p2 que calcule el cubo de el mismo conjunto de números num 
#y mandalos a escribir





