#
# A test of `multiprocessing.Pool` class
#

import multiprocessing
import time
import random
import sys
import csv
from functools import partial
import time
import timeit 

def start_main(args):
    return main_function(*args)
    
def main_function(a, b,savefile):
    time.sleep(0.5)
    result =  a * b
    name = multiprocessing.current_process().name
    try:
        #lock.acquire()                                      # start lock when trying to write to common csv file
        with open(savefile, "ab") as f:                     # get ride of new line
            writer = csv.writer(f)
            writer.writerows([[name,result]])
        #lock.release()                                      # strop the lock when finished
        return 'Success'
        
    except:
        print 'Can not write to csv file!'
        lock.release()
        return 'Failed'
        
def init(l):
    global lock
    lock = l

## first way of running multi process    
def multi_p1():
    # this will count the number of cores taht are available in the machines 
    #print 'cpu_count() = %d' % multiprocessing.cpu_count()
    # create pools 
    l = multiprocessing.Lock()
    PROCESSES = 8
    pool = multiprocessing.Pool(initializer=init, initargs=(l,), processes =PROCESSES)
    TASKS = [(i, 7,'results.csv') for i in range(100)]
    #use pool.map to start multi process 
    status = pool.map(start_main, TASKS)
    #print len(status)


## second way of running multi proecess,using partial 
def multi_p2():
    l = multiprocessing.Lock()
    PROCESSES = 80
    pool = multiprocessing.Pool(initializer=init, initargs=(l,), processes =PROCESSES)
    p_main_function = partial(main_function,b=7,savefile='resullts')          # use partial to construct the function with args
    status = pool.map(p_main_function, range(100)) 
    
def multi_cleanup():
    l = multiprocessing.Lock()
    PROCESSES = 80
    pool = multiprocessing.Pool(initializer=init, initargs=(l,), processes =PROCESSES)
    p_main_function = partial(main_function,b=7,savefile='resullts')
    status = pool.map(p_main_function, range(1000)) 
    print len(status)
    
    # test clean up functionalities
    print pool._cache           # this will print out remain taskes in the pool
    pool.close()                # close and clean up 
    pool.join()
    for worker in pool._pool:   # workers shoud be closed, all values are false
        print worker.is_alive()
    pool = None                 # collect grabages of using pool 


if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    multi_cleanup()
    
    
    