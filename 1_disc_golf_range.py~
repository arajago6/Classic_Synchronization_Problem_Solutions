from threading import Thread, Semaphore
from time import sleep
import sys
import random
rng = random.Random()
rng.seed(100)	

def frolfer_routine(FId):
    global StashSize
    global DiscOnField
    global DiscPrBucket

    while True:
        sleep(rng.random()*10)     
        mutex.acquire()
        print ('Frolfer %d is calling for bucket' % FId)
     
        if StashSize < DiscPrBucket:
            cart_block_sem.release()
            frolf_barr_sem.acquire()
        StashSize -= DiscPrBucket
        print ('Frolfer %d got %d discs; Stash = %d' % (FId,DiscPrBucket,StashSize))
        mutex.release()
        
        
        disk_iter_sem.acquire()
        disk_iter_sem.release()
        for i in range(DiscPrBucket):
            sleep(rng.random())
            DiscOnField += 1
            print ('Frolfer %d threw disc %d' % (FId,i))
