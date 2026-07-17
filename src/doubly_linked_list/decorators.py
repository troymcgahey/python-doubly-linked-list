from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
        
    return decorator

def retry(max_attemps):
    def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwards):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except ConnectionError:
                if attempt == max_attempts - 1:
                    raise
        return wrapper
    return decorator
