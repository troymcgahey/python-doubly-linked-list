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

def test_get_returns_none_for_missing_key():
    cache = LRUCache(2)

    assert cache.get("A") is None

def test_get_moves_node_to_front():
    cache = LRUCache(3)

    a = LRUNode("A", 100)
    b = LRUNode("B", 200)
    c = LRUNode("C", 300)

    cache.cache["A"] = a
    cache.cache["B"] = b
    cache.cache["C"] = c

    cache._add_to_front(a)
    cache._add_to_front(b)
    cache._add_to_front(c)

    # Curret Order
    # C -> B -> A

    assert cache.get("A") == 100

    # New Order
    # A -> C-> B

    assert cache.head is a
    assert cache.tail is b

def test_put_adds_new_key():
    cache = LRUCache(2)

    cache.put("A", 100)

    assert cache.get("A") == 100
    assert cache.head.key == "A"
    assert cache.tail.key == "A"
    assert len(cache.cache) == 1

def test_put_updates_existing_key_and_moves_it_to_front():
    cache = LRUCache(3)

    cache.put("A", 100)
    cache.put("B", 200)
    cache.put("C", 300)

    #Current order C -> B -> A
    cache.put("A", 999)

    assert cache.get("A") == 999
    assert cache.head.key == "A"
    assert len(cache.cache) == 3

def test_put_evicts_least_recently_used():
    cache = LRUCache(2)

    cache.put("A", 100)
    cache.put("B", 200)

    #Current order B -> A

    cache.put("C", 300)

    #A should be evicted because it is the least recently used.
    assert cache.get("A") == None
    assert cache.get("B") == 200
    assert cache.get("C") == 300
    assert cache.head.key == "C"
    assert cache.tail.key == "B"
    assert len(cache.cache) == 2

def test_get_changes_which_key_is_evicted():
    cache = LRUCache(2)

    cache.put("A", 100)
    cache.put("B", 200)

    #Current order B -> A
    cache.get("A")

    #New order A -> B
    cache.put("C", 300)

    #B should now be evicted
    assert cache.get("B") == None
    assert cache.get("A") == 100
    assert cache.get("C") == 300
    assert cache.head.key == "C"
    assert cache.tail.key == "A"

def test_len_returns_cache_size():
    cache = LRUCache(2)

    cache.put("A", 100)
    cache.put("B", 200)

    assert len(cache) == 2

def test_contains_checks_for_keys():
    cache = LRUCache(2)
    cache.put("A", 100)

    assert "A" in cache
    assert "B" not in cache

def test_iteration_returns_most_recent_first():
    cache = LRUCache(3)

    cache.put("A", 100)
    cache.put("B", 200)
    cache.put("C", 300)

    assert list(cache) == [
        ("C", 300),
        ("B", 200),
        ("A", 100),
    ]

def test_peek_does_not_change_recenct():
    cache = LRUCache(2)

    cache.put("A", 100)
    cache.put("B", 200)

    #Order: B -> A
    assert cache.peek("A") == 100

    #A should still be least recently used.
    cache.put("C", 300)

    assert "A" not in cache
    assert "B" in cache
    assert "C" in cache

def test_clear_empties_cache():
    cache = LRUCache(2)

    cache.put("A", 100)
    cache.put("B", 200)
    cache.clear()

    assert len(cache) == 0
    assert cache.head is None
    assert cache.tail is None
    assert list(cache) == []
