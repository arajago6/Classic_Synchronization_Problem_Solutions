from threading import Thread, Semaphore
from collections import deque
from time import sleep
import itertools
import sys	
import random
rng = random.Random()
rng.seed(100)

mutex_local = Semaphore(1)
floor_sem, runnable_sem = Semaphore(0), Semaphore(0)

FIDKeeper, LIDKeeper = deque(), deque()
LdrCount, FlrCount, DncrCount = 0, 0, 0

class FIFOQCreator:
    def __init__(self):
        self.queue = deque()
        self.mutex = Semaphore(1)
        
    def class_wait(self, thread_local_sem):
        self.mutex.acquire()
        self.queue.append(thread_local_sem)
        self.mutex.release()
        thread_local_sem.acquire()
        
    def class_signal(self):
        self.mutex.acquire()
        sem = self.queue.popleft()		
        self.mutex.release()
        sem.release()
