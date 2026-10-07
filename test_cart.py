from cart import cartCal

def test_delivery():
    assert cartCal(500)==500

def test_Addfee():
    assert cartCal(400)==450

def test_Addfee1():
    assert cartCal(600)==600

def test_fee2():
    assert cartCal(499)==549

def test_fee3():
    assert cartCal(100)==150