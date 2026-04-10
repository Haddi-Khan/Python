class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def delete_value(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.display()
ll.delete_value(20)
ll.display()
