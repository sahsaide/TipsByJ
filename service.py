from abc import ABC, abstractmethod

# 1. ABSTRACTION
class Service(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self):
        pass

# INHERITANCE: Existing Services
class Manicure(Service):
    def __init__(self):
        super().__init__("Gel Manicure", 45)
    def get_details(self):
        return f"{self.name} - Includes cuticle care and gel polish (${self.price})"

class Pedicure(Service):
    def __init__(self):
        super().__init__("Spa Pedicure", 60)
    def get_details(self):
        return f"{self.name} - Includes massage and scrub (${self.price})"

# INHERITANCE: New Services
class AcrylicSet(Service):
    def __init__(self):
        super().__init__("Acrylic Full Set", 85)
    def get_details(self):
        return f"{self.name} - Durable extensions with powder/liquid (${self.price})"

class PolygelTips(Service):
    def __init__(self):
        super().__init__("Polygel Tips", 95)
    def get_details(self):
        return f"{self.name} - Lightweight, flexible hybrid extension (${self.price})"