# -*- coding: utf-8 -*-
import os, sys
import multiprocessing

class ChildProcess(multiprocessing.Process):
    
    def __init__(self, pipein): #le mando de argumento un objeto de conexion tipo pipe 
        super(ChildProcess, self).__init__()
        self.pipein = pipein
        
    def run(self):
        print("Intentando iniciar el pipe")
        self.pipein = os.fdopen(self.pipein, 'w')
        self.pipein.write("Mi código es MX317")
        self.pipein.close()
        

def main():
    pipeout, pipein = os.pipe()
    
    child = ChildProcess(pipein) #Le envío un objeto de conexión tipo pipe 
    child.start() #Lo puedo iniciar porque es un objeto que hereda de process 
    child.join()
    
    os.close(pipein) #Se cierra el pipe 
    pipeout = os.fdopen(pipeout) #Abro el canal de comunicación 
    
    pipeContent = pipeout.read() #Leo lo que envia el proceso child 
    print("Pipe: {}".format(pipeContent))
    
if __name__== '__main__':
    main()