### decorator
def outer(func):
    def inner():
        print("Inner function Accessing :", 
                func.__name__)
        return func()
    return inner
@outer
def greet():
    print("Inside greet function")
    return 'Hello!'


print (greet())
