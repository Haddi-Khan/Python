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
