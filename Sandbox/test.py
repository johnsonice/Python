########
#Array
########

import os
import sys
box = 'C:\Users\chuang\Box Sync\Python\Udemy\\1_PythonBootcamp'
os.chdir(box)
cwd = os.getcwd()
mPath = box + '\Custom_Module'

if not mPath in sys.path: #add modules path to sys path
    sys.path.insert(1,mPath)
del mPath

#####
####  jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser 
####  http://python-c9-johnsonice.c9users.io:8080
####

###############
### once in vim mode use control + x to exit
##############