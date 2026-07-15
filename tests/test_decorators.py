from doubly_linked_list.lru_cache import LRUCache

def test_log_call_prints_method_name(capsys):
    cache = LRUCache(2)

    cache.put("A", 100)

    captured = capsys.readouterr()

    assert "Calling put" in captured.out
    assert "Finished put" in captured.out
