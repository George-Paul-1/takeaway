def receipt(order): 
    items = []
    total = 0
    for item in order: 
        items.append(item["name"])
        total += item["price"]
    return f"ITEMS: {', '.join(items)} TOTAL: £{total}"