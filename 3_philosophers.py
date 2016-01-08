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

def leftHandedMain(i,MCount):
    global forks
    state = 0
    for m in range(0,MCount):
        sleep(rng.random()/100)
        if(state == 0):
            if i == 0:	
                forks[left_fork(i)].acquire()
                forks[right_fork(i)].acquire()
                state = 1
            else:
                forks[right_fork(i)].acquire()	
                forks[left_fork(i)].acquire()
                state = 1
        else:
            if i == 0:	
                forks[left_fork(i)].release()
                forks[right_fork(i)].release()
                state = 0
            else:
                forks[right_fork(i)].release()	
                forks[left_fork(i)].release()
                state = 0

def left_fork(id):
    return id

def right_fork(id):
    return (id+1) % PCount

def tb_test(i):
    global state
    if state[i] == 'hungry' and state[tnbm_left_fork(i)] != 'eating' and state[tnbm_right_fork(i)] != 'eating':
        state[i] = 'eating'
        sem[i].release()

def tb_get_fork(i):
    global mutex
    global state
    global sem

    mutex.acquire()
    state[i] = 'hungry'
    tb_test(i)
    mutex.release()
    sem[i].acquire()

def tb_put_fork(i):
    global mutex
    global state
    global sem

    mutex.acquire()
    state[i] = 'thinking'
    tb_test(tnbm_right_fork(i))
    tb_test(tnbm_left_fork(i))
    mutex.release()

def tannenbaumMain(i,MCount):
    for m in range(0,MCount):
        tb_get_fork(i)
        sleep(rng.random()/100)        
        tb_put_fork(i)

def tnbm_right_fork(id):
    return (id+1) % PCount

def tnbm_left_fork(id):
    return (id+PCount-1) % PCount

def footmanRun():
    global PCount
    global MCount
    fthrds = [Thread(target=footmanMain, args=(i,MCount)) for i in range(PCount)]
    for t in fthrds: t.start()
    for t in fthrds: t.join()

def leftHandedRun():
    global PCount
    global MCount
    lthrds = [Thread(target=leftHandedMain, args=(i,MCount)) for i in range(PCount)]
    for t in lthrds: t.start()
    for t in lthrds: t.join()

def tannenbaumRun():
    global PCount
    global MCount
    tthrds = [Thread(target=tannenbaumMain, args=(i,MCount)) for i in range(PCount)]
    for t in tthrds: t.start()
    for t in tthrds: t.join()

