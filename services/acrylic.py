from .service import Service

class AcrylicSet(Service):
    def __init__(self):
        super().__init__("Acrylic Full Set", 85)

    def get_details(self):
        return f"{self.name} - Durable extensions (${self.price})"

