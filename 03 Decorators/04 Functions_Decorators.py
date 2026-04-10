def greet():
    def word ():
        print("hello")
        
    return word

x=greet()
x()

def say_hi(message):
    return f"Hi,{message}"

def call_func(func):
    print(f"{func("what are you doing ")}")

call_func(say_hi)
