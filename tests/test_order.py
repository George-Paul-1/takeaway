from lib.order import Order 
from unittest.mock import Mock
import pytest

def test_return_list(): 
    order = Order() 
    assert order.order_list == []

def tests_return_menu(): 
    order = Order()
    res = order.show_menu()
    assert res == "1. burger, £3| 2. pizza, £4| 3. ramen, £5| " 

def test_add(): 
    order = Order()
    order.add_item("burger")
    res = order.order_list
    assert res == [{"name": "burger", "price": 3, "number": 1}]

def test_add_2(): 
    order = Order()
    order.add_item("burger")
    order.add_item("ramen")
    res = order.order_list
    assert res == [{"name": "burger", "price": 3, "number": 1}, {"name": "ramen", "price": 5, "number": 3}]

def test_remove(): 
    order = Order()
    order.add_item("burger")
    order.remove_item("burger")
    res = order.order_list
    assert res == []

def test_order(): 
    order = Order()
    order.add_item("burger")
    order.add_item("ramen")
    res = order.order_food("07791805061")
    assert res == "ITEMS: burger, ramen TOTAL: £8"