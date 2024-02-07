from lib.dishes import Dishes 


def tests_initialised_dishes_without_dict():
    dishes = Dishes()
    assert dishes.dishlist == [{"name": "burger", "price": 3, "number": 1}, {"name": "pizza", "price": 4, "number": 2}, {"name": "ramen", "price": 5, "number": 3}]

def tests_initialised_dishes_and_adds_dict():
    dishes = Dishes()
    dishes.add("dish", 10)
    assert dishes.dishlist == [{"name": "burger", "price": 3, "number": 1}, {"name": "pizza", "price": 4, "number": 2}, {"name": "ramen", "price": 5, "number": 3}, {"name": "dish", "price": 10, "number": 4}]

def test_dishes_add_more_and_count(): 
    dishes = Dishes() 
    dishes.add("dish1", 3)
    dishes.add("dish2", 4) 
    dishes.add("dish3", 5) 
    res = dishes.dishlist
    assert res == [{"name": "burger", "price": 3, "number": 1}, {"name": "pizza", "price": 4, "number": 2}, {"name": "ramen", "price": 5, "number": 3}, {"name": "dish1", "price": 3, "number": 4}, {"name": "dish2", "price": 4, "number": 5}, {"name": "dish3", "price": 5, "number": 6}]

def test_dishes_update_price(): 
    dishes = Dishes()
    dishes.add("dish", 10)
    dishes.update_price("dish", 20)
    assert dishes.dishlist == [{"name": "burger", "price": 3, "number": 1}, {"name": "pizza", "price": 4, "number": 2}, {"name": "ramen", "price": 5, "number": 3}, {"name": "dish", "price": 20, "number": 4}]

def test_dishes_menu(): 
    dishes = Dishes()
    res = dishes.menu()
    assert res == "1. burger, £3| 2. pizza, £4| 3. ramen, £5| "