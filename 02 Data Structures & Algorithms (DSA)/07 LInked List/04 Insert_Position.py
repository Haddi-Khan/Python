# def insert_at_position(self, data, position):
#     if position == 0:
#         self.insert_at_beginning(data)
#         return

#     new_node = Node(data)
#     temp = self.head

#     for _ in range(position - 1):
#         if temp is None:
#             return
#         temp = temp.next

#     new_node.next = temp.next
#     temp.next = new_node
