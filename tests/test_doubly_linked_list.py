import pytest

from doubly_linked_list.list import DoublyLinkedList

def test_len_dunder_method():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    assert len(letters) == 3

def test_append_and_forward_traversal():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    assert letters.forward_traversal() == ["A", "B", "C"]
    assert letters.size == 3

def test_backward_traversal():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    assert letters.backward_traversal() == ["C", "B", "A"]

def test_contains_returns_true_when_value_exists():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")

    assert letters.contains("B") is True

def test_contains_returns_false_when_value_missing():
    letters = DoublyLinkedList()

    letters.append("A")

    assert letters.contains("B") is False

def test_find_returns_node_when_value_exists():
    letters = DoublyLinkedList()
    
    letters.append("A")
    letters.append("B")

    node = letters.find("B")

    assert node is not None
    assert node.value == "B"

def test_find_returns_none_when_value_missing():
    letters = DoublyLinkedList()

    letters.append("A")

    assert letters.find("B") is None

def test_insert_after_middle_node():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    letters.insert_after("B", "X")

    assert letters.forward_traversal() == ["A", "B", "X", "C"]
    assert letters.backward_traversal() == ["C", "X", "B", "A"]
    assert letters.size == 4

def test_insert_after_tail_updates_tail():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")

    letters.insert_after("B", "X")

    assert letters.forward_traversal() == ["A", "B", "X"]
    assert letters.tail.value == "X"
    assert letters.size == 3

def test_insert_after_missing_value_raises_error():
    letters = DoublyLinkedList()

    letters.append("A")

    with pytest.raises(ValueError):
        letters.insert_after("X", "B")

def test_insert_before_middle_node():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    letters.insert_before("B", "X")

    assert letters.forward_traversal() == ["A", "X", "B", "C"]
    assert letters.backward_traversal() == ["C", "B", "X", "A"]
    assert letters.size == 4

def test_insert_before_head_updates_head():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")

    letters.insert_before("A", "X")

    assert letters.forward_traversal() == ["X", "A", "B"]
    assert letters.head.value == "X"
    assert letters.size == 3

def test_delete_middle_node():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")
    letters.append("C")

    letters.delete("B")

    assert letters.forward_traversal() == ["A", "C"]
    assert letters.backward_traversal() == ["C", "A"]
    assert letters.size == 2

def test_delete_head_updates_head():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")

    letters.delete("A")

    assert letters.forward_traversal() == ["B"]
    assert letters.head.value == "B"
    assert letters.head.prev is None
    assert letters.head.next is None
    assert letters.size == 1

def test_delete_tail_updates_tail():
    letters = DoublyLinkedList()

    letters.append("A")
    letters.append("B")

    letters.delete("B")

    assert letters.forward_traversal() == ["A"]
    assert letters.tail.value == "A"
    assert letters.tail.prev is None
    assert letters.tail.next is None
    assert letters.size == 1

def test_delete_only_node_empties_list():
    letters = DoublyLinkedList()

    letters.append("A")

    letters.delete("A")

    assert letters.forward_traversal() == []
    assert letters.backward_traversal() == []
    assert letters.head is None
    assert letters.tail is None
    assert letters.size == 0

def test_delete_missing_value_raises_error():
    letters = DoublyLinkedList()
   
    letters.append("A")

    with pytest.raises(ValueError):
        letters.delete("X")

