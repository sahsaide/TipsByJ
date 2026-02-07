from .service import Service

class Manicure(Service):
    def __init__(self):
        super().__init__("Manicure", 25)

    def get_details(self):
        return f"{self.name} - Nail shaping and cuticle care (${self.price})"
