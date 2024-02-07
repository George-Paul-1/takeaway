from lib.dishes import *
from lib.receipt import receipt
from lib.sms_sender import sms 

class Order(): 
    def __init__(self):
        self.order_list = []
        self.dishes = Dishes()
    
    def show_menu(self):
        self.menu = self.dishes.menu()
        return self.menu
    
    def add_item(self, name): 
        for item in self.dishes.dishlist: 
            if item["name"] == name:
                self.order_list.append(item)

    def remove_item(self, name):
        for item in self.order_list: 
            if item["name"] == name: 
                self.order_list.remove(item)

    def order_food(self, phone):
        receipt_ = receipt(self.order_list)
        sms(phone) 
        return receipt_
