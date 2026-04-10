def delete_value(self, value):
    if self.head is None:
        return

    curr = self.head
    prev = None

    while True:
        if curr.data == value:
            if prev:
                prev.next = curr.next
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = curr.next
                self.head = curr.next
            return

        prev = curr
        curr = curr.next

        if curr == self.head:
            break
