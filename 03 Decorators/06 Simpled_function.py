def dec(func):
    def wrapper ():
        print ("before functions runs")
        func()
        print ("After functions runs ")
    return wrapper 

def say_whee():
    print ("whEEE!")

say_whee = dec(say_whee)
say_whee ()


