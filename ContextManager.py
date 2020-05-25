### context manager


##Run example 1 first and comment 2, to understand process without context manager
##Run example 2, and comment 1st to understand the process closure handled by context manage


##################Example 1 ####################
##
''' this is to show without context manager '''
files=[]
for i in range(0,10000):

    path='H:\\context managers\\Temp\\'
        
    files.append(open(path+"file%i" %i, 'w'))
    


###################### Example 2 ###############

''' this is with context manager '''

files=[]
for i in range(0,10000):

    
	path='H:\\context managers\\Temp\\'
        
    with (open(path+"file%i" %i, 'w')) as fl:
        files.append(fl)


    

