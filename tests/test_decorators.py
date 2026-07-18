import pytest 

from doubly_linked_list.lru_cache import LRUCache
from doubly_linked_list.decorators import retry

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
        attempts += 1

        if attempts < 3:
            raise ConnectionError("Temporary Failure")

        return "Downloaded"

    result = download()

    assert result == "Downloaded"
    assert attempts == 3

def test_retry_does_not_retry_after_success():
    attempts = 0

    @retry(3)
    def download():
        nonlocal attempts
        attempts += 1
        return "Downloaded"

    result = download()
    assert attempts == 1

def test_retry_raises_after_max_attempts():
    attempts = 0

    @retry(3)
    def download():
        nonlocal attempts
        attempts += 1
        raise ConnectionError("Service unavailable")

    with pytest.raises(ConnectionError, match="Service unavailable"):
        download()

    assert attempts == 3

def test_retry_handles_configured_exception():
    attempts = 0

    @retry(
        max_attempts=3,
        exceptions=(TimeoutError,),
    )
    def call_service():
        nonlocal attempts
        attempts += 1

        if attempts < 2:
            raise TimeoutError("Timed out")

        return "success"

    assert call_service() == "success"
    assert attempts == 2

def test_retry_does_not_handle_unconfigured_exception():
    attempts = 0

    @retry(
        max_attempts=3,
        exceptions=(ConnectionError,),
    )
    def call_service():
        nonlocal attempts
        attempts += 1
        raise ValueError("Bad input")

    with pytest.raises(ValueError, match="Bad input"):
        call_service()

    assert attempts == 1
