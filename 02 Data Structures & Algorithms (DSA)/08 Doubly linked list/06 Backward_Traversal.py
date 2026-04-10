def display_backward(self):
    temp = self.head
    while temp.next:
        temp = temp.next

    while temp:
        print(temp.data, end=" ⇄ ")
        temp = temp.prev
    print("None")
