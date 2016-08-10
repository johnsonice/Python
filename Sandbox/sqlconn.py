import MySQLdb

import os
import sys

host = os.getenv('IP')
port = 3306      #default mysql port
user = os.getenv('C9_USER')
password = ''
database = 'test'

db = MySQLdb.connect(user=user,host=host,port=port,passwd=password,db=database)

print 'connect successful'
