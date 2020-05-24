
### generator############
import time
def get_fibbo(n):
    
    a,b=0,1
    cnt=0
    
    while (cnt<n):
        a,b=b,a+b
        yield a
        cnt+=1
        

start=time.time()    
for gen in get_fibbo(100):
    print(gen)

print("total time taken in sec :",time.time()-start)

    
