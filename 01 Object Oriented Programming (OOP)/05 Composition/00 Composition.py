class Room:
    def __init__(self,name):
        self.name=name
class House:
    def __init__(self):
        self.room = Room("Bedroom")
home = House()
print (home.room.name)