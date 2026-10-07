from teenager import is_teenager

def test_isTeenager():
    assert is_teenager(15)==True

def test_isTeenager1():
    assert is_teenager(13)==True

def test_isTeenager():
    assert is_teenager(19)==True

def test_isyoung():
    assert is_teenager(12)==False

def test_isold():
    assert is_teenager(50)==False

def test_zero():
    assert is_teenager(0)==False

def test_negative():
    assert is_teenager(-5)==False