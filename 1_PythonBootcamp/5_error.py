###############################################
####### error handelling ######################
###############################################

############
##try except finally 
############

def askint():
    while True: #this will loop forever 
        try:
            val = int(raw_input('Please enter a integer: '))
        except:
            print 'Looks like you did not enter an integer!'
            continue
        else:
            return val
            break
        finally:
            print 'blook executed' #this will always executed 
            
inputVal = askint()
print inputVal
