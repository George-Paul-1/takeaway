class Dishes(): 
    def __init__(self):
        self.dishlist = [{"name": "burger", "price": 3, "number": 1}, {"name": "pizza", "price": 4, "number": 2}, {"name": "ramen", "price": 5, "number": 3}]
        self.count = 3
    
    def add(self, dish, price):
        self.count += 1
        self.dishlist.append({"name": dish, "price": price, "number": self.count})
    
    def update_price(self, name, price): 
        for dish in self.dishlist: 
            if dish["name"] == name: 
                dish["price"] = price
    
    def menu(self):
        menu = ""
        for item in self.dishlist: 
            menu = menu + f"{str(item['number'])}. {item['name']}, £{item['price']}| "
        menu.strip()
        return menu

