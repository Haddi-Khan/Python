def hello(func):
    def wrapper():
        return "hello world | " + func()
    return wrapper

@hello
def task():
    return "task is done"

print(task())