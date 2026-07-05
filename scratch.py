from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

letters.append("A")
letters.append("C")

try:
    letters.insert_after("D", "B")
except ValueError as e:
    print(e)

print("\nForward Traversal")
print(letters.forward_traversal())
print("Pretty Printing")

for value in letters.forward_traversal():
    print(f"Value: {value}")
