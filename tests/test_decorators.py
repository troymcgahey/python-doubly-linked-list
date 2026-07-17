from doubly_linked_list.lru_cache import LRUCache, retry

def test_log_call_prints_method_name(capsys):
    cache = LRUCache(2)

    cache.put("A", 100)

    captured = capsys.readouterr()

    assert "Calling put" in captured.out
    assert "Finished put" in captured.out

def test_retry_succeeds_after_failures():
    attempts = 0

    @retry(3)
    def download():
        nonlocal attempts
        attemps += 1

        if attempts < 3:
            raise ConnectionError("Temporary Failure")

        return "Downloaded"

    result = dpwnload()

    assert result == "Downloaded"
    assert attempts == 3
