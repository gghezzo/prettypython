# Playing with Threads  
# From : http://pythonprogramming.net/threading-tutorial-python/
# NOT From http://www.java2s.com/Code/Python/Thread/Start10copiesofafunctionrunninginparallel.htm
# Typer: Ginny C Ghezzo 
# What I learned: 

import threading 
from queue import Queue 
import time 

def exampleJob(worker):
	time.sleep(.5) 				# Pretend to work 
	print_lock = threading.Lock()
	with print_lock:
		print(threading.current_thread().name, worker)

# The threader thread pulls an worker from the queue and processes it 
def threader():
	while True:
		#get an worker from the queue
		worker = q.get()
		# Run the example job with the avail worker in queue (thread)
		exampleJob(worker)
		#complete with the job 
		q.task_done()

q = Queue()
start = time.time()
for x in range(10):
	t = threading.Thread(target=threader)
	# classifying as a daemon, so they will die when the main dies 
	t.daemon = True 
	# begins, must come after daemon definition 
	t.start()

# 20 jobs assigned 
for worker in range(20): 
	q.put(worker)
# wait until the thread terminates
q.join()
# with 10 workers and 20 tasks, with each tasks being .5 seconds, then the completed job 
# is 1 second using threading, normally 20 tasks with .5 seconds each would take 10 seconds
print('Entire Job took: ', time.time() - start)