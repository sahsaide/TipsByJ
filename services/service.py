class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name} (${self.price})"

