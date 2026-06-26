class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}: ${self.price:.2f}"
    
    def get_total_price(self, quantity):
        total_price = self.price * quantity

        #quantity >= 3 
        if quantity >= 3:
            total_price *= 0.9  # Apply 10% discount

        return round(total_price)