### closures ###

def outerfunc(x):
    def innerfunc():
        print(x)

    return innerfunc          


myfunc=outerfunc(7)


myfunc()


#############e.g 2 ############3
''' bindling a function with closure '''

def outer(func):
    def inner(msg):
        func(msg)
    return inner

def sayHi(msg):
    print(msg)

    
myfunc=outer(sayHi)
myfunc("Hello")
