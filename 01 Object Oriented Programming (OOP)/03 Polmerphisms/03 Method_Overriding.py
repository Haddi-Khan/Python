class A:
    def dis(self):
        print ("this is a parent class ")\

class B(A):
    def dis (self):
        super().dis()
        print ("this is a child class")
 
obj=B()
obj.dis()