from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

letters.append("A")
letters.append("B")
letters.append("C")

print(letters.head.value)
print(letters.head.next.value)
print(letters.tail.value)
print(letters.tail.prev.value)
print(letters.size)

