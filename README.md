# Python-advance-concepts

1. Functions:
    1. Function is a block of code, which runs on being called.
    2. Functions can be defined inside another function and can also be passed as argument to another function.
    
    Syntax: 
    def functionname(args):
	  pass

    functioname()
    
    Refer example how paramters can be passed in a function.
    
    
2. Generators:
    1. A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield     keyword rather than return.
    2. Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object.
    
    Syntax: 
    def simpleGeneratorFun(): 
    	  yield 1
                  
    x = simpleGeneratorFun() 
    '''x is a generator object'''
    
    print(x.next())
    '''Iterating over the generator object using next'''
    
    Usage:
    Generator are memory efficient they store the latest state of funtion on encountering yield statement. So whenever next statement is called it doesn't reruns the loop like a function rather goes to next operation.
    
    e.g shows the usage of generator vs function for fabbonaci number calculation.
    
    
    
    



    
    
