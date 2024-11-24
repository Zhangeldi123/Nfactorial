from main import greet

def test_greet():
    assert greet("") == "Hello, !"
    assert greet(1) == "Hello, 1!"
