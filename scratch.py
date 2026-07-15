from src.doubly_linked_list.lru_cache import LRUCache


cache = LRUCache(2)

cache.put("A", 100)
cache.put("B", 200)

print("Peek; ", cache.peek("B"))

print(cache)

for key, value in cache:
    print(f"Key: {key} Value: {value}")

