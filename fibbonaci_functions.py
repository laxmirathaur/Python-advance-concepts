## function for fibbonacci series ###

import time

def fibbo(n):

    if (n==1):
        return 0

    elif (n==2):
        return 1

    else:
        return fibbo(n-1)+fibbo(n-2)


start=time.time()
print (fibbo(25))
print("total time taken in sec :",time.time()-start)









