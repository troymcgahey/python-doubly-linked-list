from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

print("\nSearching for value: Z")
print(letters.contains("Z"))

letters.append("B")
letters.append("C")
letters.prepend("A")

print("\nForward Traversal")
print(letters.forward_traversal())
print("Pretty Printing")

for value in letters.forward_traversal():
    print(f"Value: {value}")

print("\nBackward Traversal")
print(letters.backward_traversal())
print("Pretty Printing")

for value in letters.backward_traversal():
    print(f"Value: {value}")

print("\nSearching for value: B")
print(letters.contains("D"))
