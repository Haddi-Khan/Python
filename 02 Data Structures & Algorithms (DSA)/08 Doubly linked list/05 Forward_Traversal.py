def display_forward(self):
    temp = self.head
    while temp:
        print(temp.data, end=" ⇄ ")
        temp = temp.next
    print("None")
