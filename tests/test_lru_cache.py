import pytest

from doubly_linked_list.lru_cache import LRUCache, LRUNode

def test_lru_cache_requires_positive_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)

def test_add_to_front_adds_first_node_as_head_and_tail():
    cache = LRUCache(2)
    node = LRUNode("A", 100)

    cache._add_to_front(node)

    assert cache.head is node
    assert cache.tail is node
    assert node.prev is None
    assert node.next is None

def test_add_front_adds_node_before_existing_head():
    cache = LRUCache(2)
    a = LRUNode("A", 100)
    b = LRUNode("B", 200)

    cache._add_to_front(a)
    cache._add_to_front(b)

    assert cache.head is b
    assert cache.tail is a
    assert b.next is a
    assert a.prev is b
