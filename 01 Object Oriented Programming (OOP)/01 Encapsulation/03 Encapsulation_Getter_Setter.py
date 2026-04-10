class Student:
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name
s= Student("haddi")
print(s.get_name())    
s.set_name("Ali")
print(s.get_name())