# decorators use for change or modify the function without change the real function 
def hello (func):
    def wapper ():
        return "hello World "+ func()
    return wapper

@hello
def task():
    return "task is done"

print (task()) 