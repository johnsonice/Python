# -*- coding: utf-8 -*-
"""
Fancy system argument handeler 
"""

import sys
import argparse

## set argHandler as dictionary boject 
class argHandler(dict):
    _descriptions = {'help, --h, -h': 'show this super helpful message and exit'}    
    
    def define(self, argName, default, description):
        self[argName] = default
        self._descriptions[argName] = description
    
    ## set up default arguments
    def setDefaults(self):
        self.define('imgdir', './sample_img/', 'path to testing directory with images')
        self.define('binary', './bin/', 'path to .weights directory')
        self.define('config', './cfg/', 'path to .cfg directory')

    ## update default arguments with user passed in arguments 
    def parseArgs(self,arg):
        parser = argparse.ArgumentParser()
        for k in self.keys():
            key = '--' + k
            parser.add_argument(key,default=self[k])
        
        arguments = vars(parser.parse_args())  ## turn parsed arguments into a dictionary
        for k,v in arguments.items():
            self[k] = v
            
#%%

#### this is how you use argHandler, 
#### the returned flags can bue used as a dictionray
FLAGS = argHandler()
FLAGS.setDefaults()
FLAGS.parseArgs(sys.argv)
print(FLAGS)

### in cli you can passing somehting like:
##   python arg_handle --imgdir testing/
