from src.doubly_linked_list.decorators import repeat

@repeat(3)
def greet():
    print("Hello")

greet()
