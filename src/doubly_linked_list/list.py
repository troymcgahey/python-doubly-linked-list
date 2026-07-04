from src.doubly_linked_list.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node

        self.size += 1

    def insert_after(self, target_value, new_value):


    def contains(self, value):
        value_found = False

        current = self.head

        while current is not None:
            if current.value == value:
                value_found = True
                break
            
            current = current.next

        return value_found

    def forward_traversal(self):
        values = []

        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def backward_traversal(self):
        values = []

        current = self.tail

        while current is not None:
            values.append(current.value)
            current = current.prev

        return values
