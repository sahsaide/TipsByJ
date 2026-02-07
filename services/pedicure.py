from .service import Service

class Pedicure(Service):
    def __init__(self):
        super().__init__("Pedicure", 35)

    def get_details(self):
        return f"{self.name} - Foot care and polish (${self.price})"
