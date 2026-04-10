def delete_beginning(self):
    if self.head is None:
        return

    self.head = self.head.next

    if self.head:
        self.head.prev = None
