

import os
import sys

import os
import sys
box = 'C:\Users\chuang\Box Sync\Python\Udemy\\1_PythonBootcamp'
os.chdir(box)
cwd = os.getcwd()
mPath = box + '\Custom_Module'

if not mPath in sys.path: #add modules path to sys path
    sys.path.insert(1,mPath)
del mPath

l =[1,1,1,1,2,2,2,3,3,3]
x=set(l) #x = {1,2,3}
