from threading import Thread, Semaphore
from time import sleep
from timeit import Timer
import sys
import random
rng = random.Random()
rng.seed(100)		

mutex = Semaphore(1)

def footmanMain(i,MCount):
    global footman
    global forks
    state = 0
    for m in range(0,MCount):
        sleep(rng.random()/100)
        if(state == 0):
            footman.acquire()
            forks[right_fork(i)].acquire()
            forks[left_fork(i)].acquire()
            state = 1
        else:
            forks[right_fork(i)].release()
            forks[left_fork(i)].release()
            state = 0
            footman.release()
