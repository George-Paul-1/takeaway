from lib.dishes import Dishes
from lib.order import Order 
from lib.receipt import receipt 

def test_integration_1():
    order = Order()
    order.dishes.add("sushi", 50)
    order.add_item("sushi")
    order.add_item("burger")
    res = order.order_food("07791805061")
    assert res == "ITEMS: sushi, burger TOTAL: £53"

    