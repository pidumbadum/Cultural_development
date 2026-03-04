from my_math import add

def test_addition():
    assert add(2, 2) == 4
    print("Success")

def test_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(1, 1) == 1
    print("Bug")
    #assert add_with_bug(2, 3) == 5