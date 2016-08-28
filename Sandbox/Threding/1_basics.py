## Python multi threading

import threading

####################################
def do_this():
    global stop2                                            # Use global variable as start and stop switch for thread
    print 'This is a seperate thread! \n'
    while(stop2==False):                                    # If switch is false, keep going
        pass    
    else:                                                   # If switch is true, stop the thread
        print 'Thread2 stopped as stop2 is assigned to true.'
###################################
def do_this2():
    x = 0 
    while (x<300):
        x+=1
    print x 
###################################
def do_after():
    x = 0 
    while (x<600):
        x+=1
    print x 
##################################




def main():
    
    # global switch to stop a thread
    global stop2                                        # Use global variable as start and stop switch for thread
    stop2 = False
    
    # start antoher thred
    second_thread = threading.Thread(target=do_this,name='2-thread')    # create a new thread and pass through a function 
    second_thread.start()                                               # start rnn the thread in a seperate process
    # start a third thred 
    third_thread = threading.Thread(target=do_this2(),name='3-thread')      # create a new thread and pass through a function 
    third_thread.start()                                                    # start rnn the thread in a seperate process
        # thread.join will make the next thread to wait for the thread to finish, it actually joined two thread into one
    third_thread.join()                                                     
    # start a third thred 
    forth_thread = threading.Thread(target=do_after(),name='4-thread')    # create a new thread and pass through a function 
    forth_thread.start() 
    
    
    # some status check functions 
    print threading.active_count()          # number of thread
    print threading.enumerate()             # list of all the thread
    print threading.currentThread()         # current thread 
    print second_thread.is_alive()          # check see if the thread is alive 
    print second_thread.ident               # even if thread is stopped, the id remains
    
    stop2 = True                            # Use global variable as start and stop switch for thread
    
    
if(__name__=="__main__"):
    main()
    
    