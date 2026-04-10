def hello (func):
  def wapper ():
    return "hello world"+ func()
  return wapper
@hello 
def task ():
  return " task is done"
print (task())
