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
    
    Refer programme Fibbonaci_generator vs Fibbonaci_function to shows the effectiveness of generator vs function for fabbonaci number calculation.
    
3. Decorator:
	1. Decorators allow us to wrap another function in order to extend the behaviour of wrapped function, without permanently modifying it.
	2. Functions are taken as the argument into another function and then called inside the wrapper function.
	
	Syntax:
	@decorator()
	def func_name():
    	''' Function implementation'''
	
	Usage: Decorator helps us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. It is used extensively in python projects.
	
	Refer program decorators.py to see the usage.
	
	
4. Closures:
	Closure is when some data gets attached to the code. So, this value is remembered even when the variable goes out of scope, or the function is removed from the namespace
	For a closure:
	1. We must have a nested function.
	2.This nested function must refer to a variable nonlocal to it(a variable in the scope enclosing it).
	3.The enclosing scope must return this function.


	Usage:
	No need to use global values, it retain the state of variable.
	A closure lets us invoke Python function outside its scope.
	
	Refer program closure.py to see the usage.
	

5. Context Managers: 
	Context manager is a powerful tool, which helps in allocating and releasing resources precisely. 
	A ‘with’ statement is used as context manager.
	
	Usage:
	It Ensures error and exceptions are handled correctly.
	It Essential in concurrent and parallel programming.
	
	Refer program ContextManager.py to understand the effectiveness with usage of context manager.
	
	

	

	
	
	
	

    
    
    
    
    



    
    
