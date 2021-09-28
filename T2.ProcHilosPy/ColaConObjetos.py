# -*- coding: utf-8 -*-
import multiprocessing
#En esta clase no hay ningun tipo de herencia 
class MyWorker():
    def __init__(self, x):
        self.x = x

    def process(self):
        pname = multiprocessing.current_process().name
        print('Starting process %s for number %i...' % (pname, self.x))

        
def work(q):
    worker = q.get()
    worker.process()

if __name__ == '__main__':
    my_queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=work, args=(my_queue,))
    p.start()

    my_queue.put(MyWorker(3)) #Se pone en la cola un objeto de tipo myWorker que guarda el número 1

    my_queue.close()
    my_queue.join_thread()   ## investigar ...
    p.join()

    print('Done.')