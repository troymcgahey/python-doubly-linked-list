from doubly_linked_list.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.value
            
            current = current.next

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"

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

    def insert_before(self, target_value, new_value):
        target_node = self.find(target_value)

        if target_node is None:
            raise ValueError(f"Target value '{target_value}' not found.")
        
        new_node = Node(new_value)

        new_node.next = target_node
        new_node.prev = target_node.prev

        if self.head == target_node:
            self.head = new_node
        else: 
            target_node.prev.next = new_node

        target_node.prev = new_node
        self.size += 1

    def insert_after(self, target_value, new_value):
        target_node = self.find(target_value)

        if target_node is None:
            raise ValueError(f"Target value '{target_value}' not found.")

        new_node = Node(new_value)

        new_node.prev = target_node
        new_node.next = target_node.next

        if target_node.next is not None:
            target_node.next.prev = new_node
        else:
            self.tail = new_node

        target_node.next = new_node
        self.size += 1

        return new_node

    def delete(self, value):

        delete_node = self.find(value)

        if delete_node is None:
            raise ValueError(f"Delete value '{value}' not found.")
        
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        if self.head == delete_node:
            delete_node.next.prev = None
            self.head = delete_node.next
        elif self.tail == delete_node:
            delete_node.prev.next = None
            self.tail = delete_node.prev
        else:
            delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev

        self.size -= 1

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current

            current = current.next

        return None

    def contains(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            
            current = current.next

        return False

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
