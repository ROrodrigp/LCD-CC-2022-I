from multiprocessing import Process, current_process
import time


def f1():
	p = current_process()
	print('Starting process %d, ID %s...' % (p.name, p.pid))
	time.sleep(4)
	print('Exiting process %s, ID %s...' % (p.name, p.pid))


def f2():
	p = current_process()
	print('Starting process %d, ID %s...' % (p.name, p.pid))
	time.sleep(4)
	print('Exiting process %s, ID %s...' % (p.name, p.pid))


if __name__ == '__main__':
	main()