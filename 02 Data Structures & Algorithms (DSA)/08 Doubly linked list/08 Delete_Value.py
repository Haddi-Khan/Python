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
