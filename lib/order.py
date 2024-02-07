from lib.dishes import *
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

    

