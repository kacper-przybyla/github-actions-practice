from app import add, greet, is_positive

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_greet():
    assert greet("Kacper") == "Hello, Kacper!"
    assert greet("World") == "Hello, World!"

def test_is_positive():
    assert is_positive(1) == True
    assert is_positive(-1) == False
    assert is_positive(0) == False