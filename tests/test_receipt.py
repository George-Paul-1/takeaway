from lib.receipt import receipt 

order = [{"name": "burger", "price": 3, "number": 1}, {"name": "ramen", "price": 5, "number": 3}]

def test_receipt():
    res = receipt(order)
    assert res == "ITEMS: burger, ramen TOTAL: £8"

def test_receipt_2(): 
    res = receipt([])
    assert res == "ITEMS:  TOTAL: £0"