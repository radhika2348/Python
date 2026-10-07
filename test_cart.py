from cart import cartCal

def test_delivery():
    assert cartCal(500)==500

def test_Addfee():
    assert cartCal(400)==450

    