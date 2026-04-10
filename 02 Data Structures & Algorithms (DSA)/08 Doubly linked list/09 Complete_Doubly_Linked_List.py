class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
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
        new_node.prev = temp

    def delete_value(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")


dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.display_forward()

dll.delete_value(20)
dll.display_forward()
