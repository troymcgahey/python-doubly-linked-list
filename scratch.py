from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

letters.append("A")
letters.append("B")

for value in letters.forward_traversal():
    print(f"Value: {value}")

try:
    letters.insert_before("D", "C")
except ValueError as e:
    print(e)

print("After Insert Before")

for value in letters.forward_traversal():
    print(f"Value: {value}")
