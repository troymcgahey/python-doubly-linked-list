from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

print("Pre Delete")

for value in letters.forward_traversal():
    print(f"Value: {value}")

try:
    letters.delete("A")
except ValueError as e:
    print(e)

print("Post Delete")

for value in letters.forward_traversal():
    print(f"Value: {value}")
