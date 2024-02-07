from lib.dishes import Dishes 
import pytest
@pytest.mark.skip(reason="no need rn")
def tests_initialised_dishes_without_dict():
    dishes = Dishes()
    assert dishes.dishlist == []
@pytest.mark.skip(reason="no need rn")
def tests_initialised_dishes_and_adds_dict():
    dishes = Dishes()
    dishes.add("dish", 10)
    assert dishes.dishlist == [{"name": "dish", "price": 10, "number": 1}]
@pytest.mark.skip(reason="no need rn")
def test_dishes_add_more_and_count(): 
    dishes = Dishes() 
    dishes.add("dish1", 3)
    dishes.add("dish2", 4) 
    dishes.add("dish3", 5) 
    res = dishes.dishlist
    assert res == [{"name": "dish1", "price": 3, "number": 1}, {"name": "dish2", "price": 4, "number": 2}, {"name": "dish3", "price": 5, "number": 3}]
@pytest.mark.skip(reason="no need rn")  
def test_dishes_update_price(): 
    dishes = Dishes()
    dishes.add("dish", 10)
    dishes.update_price("dish", 20)
    assert dishes.dishlist == [{"name": "dish", "price": 20, "number": 1}]
@pytest.mark.skip(reason="no need rn")
def test_dishes_menu(): 
    dishes = Dishes()
    res = dishes.menu()
    assert res == "1. dish, £10| "