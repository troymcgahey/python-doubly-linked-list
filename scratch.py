from src.doubly_linked_list.list import DoublyLinkedList

letters = DoublyLinkedList()

letters.append("A")
letters.append("B")
letters.append("C")

print(letters)

for letter in letters:
    print(letter)
